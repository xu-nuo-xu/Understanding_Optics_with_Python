# -*- coding: utf-8 -*-
import sys
# Import Widgets for actually used PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_superpose import Ui_MainWindow

import random
import numpy as np
from math import cos, sqrt


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        """
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.superpose()

    def superpose(self):
        # PHYSICS PARAMETTERS
        c = 2.99792458 * 1E+8
        E01 = self.spinBox_amp1.value()
        E02 = self.spinBox_amp2.value()
        Lambda1 = self.spinBox_Lambda1.value() * 1E-9
        Lambda2 = self.spinBox_Lambda2.value() * 1E-9
        F1 = c / Lambda1
        F2 = c / Lambda2
        T1 = 1 / F1
        T2 = 1 / F2
        Omega1 = 2 * np.pi * F1
        Omega2 = 2 * np.pi * F2
        K1 = Omega1 / c
        K2 = Omega2 / c

        # ANGLES
        Alpha = self.spinBox_Alpha.value()
        dAlpha = Alpha * np.pi / 180
        Theta1 = self.spinBox_PhShiftC.value()  # Orientation spatiale quelconque
        Theta2 = self.spinBox_PhShiftR.value()  # Orientation spatiale quelconque
        eps1 = Theta1 * np.pi / 180              # Phase à l'origine
        eps2 = Theta2 * np.pi / 180              # Phase à l'origine
        tmax = self.spinBox_NT.value() * T1
        x = np.linspace(0, self.spinBox_NT.value() * Lambda1, 200)  # 20 倍波长
        t = np.linspace(0, tmax, 5000)      # 20 倍周期
        tstep = t[1]
        wave1 = [[0 for ti in range(len(t))]
                 for xi in range(len(x))]  # wave1(t,x)  (np.array(wave1)).shape == (200, 5000)
        wave2 = [[0 for ti in range(len(t))]
                 for xi in range(len(x))]  # wave2(t,x)
        wave12 = [[0 for ti in range(len(t))]
                  for xi in range(len(x))]  # wave12(t,x)
        table1 = [0 for xi in range(len(x))]  # wave1(t,x)
        table2 = [0 for xi in range(len(x))]  # wave1(t,x)
        table3 = [0 for xi in range(len(x))]  # wave1(t,x)
        CoefCos = cos(dAlpha)

        for xi in range(len(x)):
            table1[xi] = K1 * x[xi]
            table2[xi] = K2 * x[xi]
            table3[xi] = (K2 - K1) * x[xi]

        for ti in range(len(t)):
            dPhi = random.uniform(-eps2, eps2) + eps1

            for xi in range(len(x)):
                wave1[xi][ti] = E01 * cos(Omega1 * t[ti] - table1[xi])
                wave2[xi][ti] = E02 * cos(Omega2 * t[ti] - table2[xi] - dPhi)
                wave12[xi][ti] = E02 * \
                    cos(Omega2 * t[ti] - (table3[xi] + dPhi)) * CoefCos
        Wave1 = []
        Wave2 = []
        Wave12 = []
        ResWave = []
        UpperEnv = []
        LowerEnv = []
        tsel = 1
        for xi in range(len(x)):
            W1 = wave1[xi][tsel]
            W2 = wave2[xi][tsel]
            W12 = wave12[xi][tsel]
            superp_waves = W1 + W2
            env_u = 2 * cos((0.5 * (K2 - K1) * x[xi]))
            env_l = -2 * cos((0.5 * (K2 - K1) * x[xi]))

            Wave1.append(W1)
            Wave2.append(W2)
            Wave12.append(W12)
            ResWave.append(superp_waves)
            UpperEnv.append(env_u)
            LowerEnv.append(env_l)

        I_max = 0
        I_min = 2 * sqrt(E01 * E02) / (E01 + E02)
        Intensity = [0 for xi in range(len(x))]
        fraction = tstep / tmax
        for xi in range(len(x)):
            Moy1 = 0
            Moy2 = 0
            P_Scalar = 0
            for ti in range(len(t)):
                Moy1 = Moy1 + wave1[xi][ti]**2 * fraction
                Moy2 = Moy2 + wave2[xi][ti]**2 * fraction
                P_Scalar = P_Scalar + wave1[xi][ti] * wave12[xi][ti] * fraction

            Intensity[xi] = Moy1 + Moy2 + 2 * P_Scalar       # 式 (9.3)

        contrast = (max(Intensity) - min(Intensity)) / \
            (max(Intensity) + min(Intensity))
        self.lineEdit_contrast.setText(str("%.4f" % contrast))

# −−−−−−−−−−−−−−−−−− First plot −−−−−−−−−−−−−−−−−−−−−−−−−
        plt1 = self.mplwidget1.canvas
        plt1.ax.clear()
        l1, l2 = plt1.ax.plot(x * 1E3, Wave1, '-r', x *
                              1E3, Wave2, '--y', linewidth=2)
        plt1.figure.legend((l1, l2), ('E1', 'E2'), 'upper right', fontsize=18)
        plt1.ax.tick_params(axis='both', which='major', labelsize=14)
        plt1.ax.set_xlabel('x(mm)', fontsize=18)
        plt1.figure.tight_layout(rect=(0., 0.05, 1, 1))
        plt1.draw()

# −−−−−−−−−−−−−−−−−− Second plot −−−−−−−−−−−−−−−−−−−−−−−−−−
        plt2 = self.mplwidget2.canvas
        plt2.ax.clear()
        l3, l4, l5 = plt2.ax.plot(x * 1E3, ResWave, '-b', x * 1E3,
                                  UpperEnv, '--r', x * 1E3, LowerEnv, '--r',  linewidth=2)
        plt2.figure.legend((l3, l4, l5), ('E1+E2', 'Envelop'),
                           'upper right', fontsize=18)
        plt2.ax.tick_params(axis='both', which='major', labelsize=14)
        plt2.ax.set_xlabel('x(mm)', fontsize=18)
        plt2.figure.tight_layout(rect=(0., 0.05, 1, 1))
        plt2.draw()

# −−−−−−−−−−−−−−−−−− Third plot −−−−−−−−−−−−−−−−−−−−−−−−−−−−
        plt3 = self.mplwidget3.canvas
        plt3.ax.clear()
        l6 = plt3.ax.plot(x * 1E3, Intensity /
                          max(Intensity), '-g', linewidth=2)
        plt3.figure.legend((l6), ('Intensity',),
                           loc='upper right', fontsize=18)
        plt3.ax.tick_params(axis='both', which='major', labelsize=14)
        plt3.ax.set_ylim(0, 2)
        plt3.ax.set_xlabel('x(mm)', fontsize=18)
        plt3.figure.tight_layout(rect=(0., 0.05, 1, 1))
        plt3.draw()

    @pyqtSlot("int")
    def on_spinBox_Lambda1_valueChanged(self, value):
        self.superpose()

    @pyqtSlot("int")
    def on_spinBox_Lambda2_valueChanged(self, value):
        self.superpose()

    @pyqtSlot("int")
    def on_spinBox_amp1_valueChanged(self, value):
        self.superpose()

    @pyqtSlot("int")
    def on_spinBox_amp2_valueChanged(self, value):
        self.superpose()

    @pyqtSlot("int")
    def on_spinBox_PhShiftC_valueChanged(self, value):
        self.superpose()

    @pyqtSlot("int")
    def on_spinBox_PhShiftR_valueChanged(self, value):
        self.superpose()

    @pyqtSlot("int")
    def on_spinBox_NT_valueChanged(self, value):
        self.superpose()

    @pyqtSlot("int")
    def on_spinBox_Alpha_valueChanged(self, value):
        self.superpose()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
