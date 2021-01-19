# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Ui_DoubleMirror import Ui_MainWindow
from numpy import pi, linspace, cos


class DoubleMirror(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(DoubleMirror, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        D1 = self.SpinBox_D1.value() * 1.E-3  # wavelength of light in vaccuum
        D2 = self.SpinBox_D2.value() * 1.E-3  # wavelength of light in vaccuum
        D3 = self.SpinBox_D3.value() * 1.E-3  # wavelength of light in vaccuum
        Lambda = self.SpinBox_Lambda.value() * 1.E-9  # wavelength of light in vaccuum
        D = self.SpinBox_D.value()            # Distance screen
        a = self.SpinBox_a.value() * 1.E-3      # bi-lenses distance

        arg1 = 2 * pi * a * D1 / Lambda / D
        arg2 = 2 * pi * a * D2 / Lambda / D
        arg3 = 2 * pi * a * D3 / Lambda / D
        arg4 = 4 * pi * a / Lambda / D

        X_Mmin = -1.E-3
        X_Mmax = -1 * X_Mmin
        N = 5000
        X = linspace(X_Mmin, X_Mmax, N)  # coordinates of screen
        I_1 = [0 for x in range(len(X))]
        I_2 = [0 for x in range(len(X))]
        I_3 = [0 for x in range(len(X))]
        for xi in range(len(X)):
            I_1[xi] = 0.5 * (1 + cos(arg1) * cos(arg4 * X[xi]))
            I_2[xi] = 0.5 * (1 + cos(arg2) * cos(arg4 * X[xi]))
            I_3[xi] = 0.5 * (1 + cos(arg3) * cos(arg4 * X[xi]))

        Contrast1 = (max(I_1) - min(I_1)) / (max(I_1) + min(I_1))
        Contrast2 = (max(I_2) - min(I_2)) / (max(I_2) + min(I_2))
        Contrast3 = (max(I_3) - min(I_3)) / (max(I_3) + min(I_3))
        self.lineEdit_D1.setText(str("%.3f" % Contrast1))
        self.lineEdit_D2.setText(str("%.3f" % Contrast2))
        self.lineEdit_D3.setText(str("%.3f" % Contrast3))

        # figure 1 D
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        l1, l2, l3 = mpl1d.ax.plot(
            X * 1E3, I_1, '-r', X * 1E3, I_2, '--g', X * 1E3, I_3, '-b',  linewidth=2)
        mpl1d.figure.legend((l1, l2, l3), ('S1', 'S2', 'S3'),
                            'upper right', fontsize=14)
        mpl1d.ax.set_xlim(X_Mmin * 1E3, X_Mmax * 1E3)
        mpl1d.ax.set_ylim(0, 1.01)
        mpl1d.ax.set_xlabel(r'$X (mm)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Double Mirror', fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m,  \ a = %4.1f \ mm, \ D = %3.2f \ m$" % (
            Lambda, a * 1E3,  D), fontsize=14)
        mpl1d.draw()

    @pyqtSlot("double")
    def on_SpinBox_D1_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D2_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D3_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.fig1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = DoubleMirror()
    MainWindow.show()
    sys.exit(app.exec_())
