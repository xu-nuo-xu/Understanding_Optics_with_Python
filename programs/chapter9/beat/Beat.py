# -*- coding: utf-8 -*-
import sys
# Import Widgets for actually used PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_Beat import Ui_MainWindow
from numpy import linspace
from math import cos, pi, exp
import numpy as np


global iphase_old, vart_old, imax_x_old
iphase_old = 0
vart_old = 0
imax_x_old = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Beat()

    def Beat(self):
        global iphase_old, vart_old, imax_x_old
        # PHYSICS PARAMETERS
        c = 2.99792458 * 1E+8   # 光速
        omega0 = 2 * pi * self.SpinBox_fc.value() * 1.0E+15     # w0
        delta = 2 * pi * self.SpinBox_dFreq.value() * 1.0E+15   # ▲w0
        vart = self.SpinBox_tParam.value() * 1.E-15             # 指示时间
        beta0 = self.SpinBox_k.value() * 1.0E6      # beta == k
        deltabeta = self.SpinBox_dBeta.value() * 1.E6       # ▲k
        varx = self.SpinBox_xParam.value() * 1.E-9     # 指示空间位置
        Vg_I = delta / deltabeta        # 群速度 p196 下面公式
        self.lineEdit_Gv.setText(str("%.2e" % Vg_I))
        Vp_I = omega0 / beta0           # 相速度 p196 上面公式
        self.lineEdit_Pv.setText(str("%.2e" % Vp_I))
        alfa = 0.E-0
        xmin, xmax = 0, 4.5 * 1E-6
        tmin, tmax = 0, 2. * 1E-13

        npasx = 15000
        npast = 5000
        x = linspace(xmin, xmax, 15000)
        t = linspace(tmin, tmax, 5000)
        Vt, Vt_e1, Vt_e2 = [], [], []
        for i in range(len(t)):
            vt = 2 * cos(t[i] * delta - varx * deltabeta) * \
                cos(t[i] * omega0 - varx * beta0)
            vt_e1 = 2 * cos(t[i] * delta - varx * deltabeta)
            vt_e2 = -2 * cos(t[i] * delta - varx * deltabeta)
            Vt.append(vt)
            Vt_e1.append(vt_e1)
            Vt_e2.append(vt_e2)

        Vx, Vx_e1, Vx_e2 = [], [], []
        for j in range(len(x)):
            vx = 2 * exp(-alfa * x[j]) * cos(vart * delta - x[j]
                                             * deltabeta) * cos(vart * omega0 - x[j] * beta0)
            vx_e1 = 2 * exp(-alfa * x[j]) * \
                cos(vart * delta - x[j] * deltabeta)
            vx_e2 = -2 * exp(-alfa * x[j]) * \
                cos(vart * delta - x[j] * deltabeta)
            Vx.append(vx)
            Vx_e1.append(vx_e1)
            Vx_e2.append(vx_e2)
        i = 0
        imin = 0
        imax = 0
        Vg_C = 0
        Vp_C = 0

        while True:
            imin = i
            i = i + 1
            if(i > npasx):
                break
            if not (Vx_e2[i] * Vx_e2[i + 1] > 0):
                break
        i = imin + 1
        while True:
            imax = i + 1
            i = i + 1
            if(i > npasx):
                break
            if not (Vx_e2[i] * Vx_e2[i + 1] > 0):
                break

        imax_x = 0
        vmax_x = 0
        for i in range(imin, imax):
            vmax_x = max(vmax_x, Vx_e2[i])
            if(Vx_e2[i] >= vmax_x):
                imax_x = i

        iphase = imin + 1
        if(iphase_old != 0):
            iphase = iphase_old

        while True:
            iphase = iphase + 1
            if(iphase > npasx):
                break
            if not (abs((Vx[iphase] - Vx_e2[iphase])) > 1E-4 and iphase <= imax):
                break

        if(iphase >= imax):
            iphase = imin

        if((vart - vart_old) != 0):
            Vg_C = abs((x[imax_x] - x[imax_x_old])) / (vart - vart_old)
            Vp_C = abs((x[iphase] - x[iphase_old])) / (vart - vart_old)

        self.lineEdit_GvCurs.setText(str("%.2e" % Vg_C))
        self.lineEdit_PvCurs.setText(str("%.2e" % Vp_C))
        X_points1 = x[imax_x] * 1E6
        Vx_point1 = Vx_e2[imax_x]
        X_points2 = x[iphase] * 1E6
        Vx_point2 = Vx[iphase]
        iphase_old = iphase
        vart_old = vart
        imax_x_old = imax_x

# −−−−−−−−−−−−−−−−−− First plot −−−−−−−−−−−−−−−−−−−−−−−−−
        plt1 = self.mplwidget1.canvas
        plt1.ax.clear()
        plt1.ax.plot(x * 1.E6, Vx,    '-b', linewidth=1)
        plt1.ax.plot(x * 1.E6, Vx_e1, '-r', linewidth=1)
        plt1.ax.plot(x * 1.E6, Vx_e2, '-r', linewidth=1)
        plt1.ax.plot(X_points1, Vx_point1, 'ro', mec="None", ms=12)
        plt1.ax.plot(X_points2, Vx_point2, 'ko', mec="None", ms=12)
        plt1.ax.set_xlim(xmin * 1.E6, xmax * 1.E6)
        plt1.ax.set_ylim(-2.1, 2.2)
        major_ticks = np.arange(xmin * 1.E6, xmax * 1.E6, 1)
        plt1.ax.set_xticks(major_ticks)
        plt1.ax.tick_params(axis='both', which='major', labelsize=9)
        plt1.ax.set_xlabel(r'x(micro)', fontsize=12, fontweight='bold')
        plt1.ax.xaxis.set_label_coords(0.6, -0.04)
        plt1.figure.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
        plt1.draw()

# −−−−−−−−−−−−−−−−−− Second plot −−−−−−−−−−−−−−−−−−−−−−−−−−
        plt2 = self.mplwidget2.canvas
        plt2.ax.clear()
        plt2.ax.plot(t * 1E12, Vt,    '-b', linewidth=1)
        plt2.ax.plot(t * 1E12, Vt_e1, '-r', linewidth=1)
        plt2.ax.plot(t * 1E12, Vt_e2, '-r', linewidth=1)
        plt2.ax.set_xlim(tmin * 1E12, tmax * 1E12)
        plt2.ax.set_ylim(-2.1, 2.2)
        plt2.ax.tick_params(axis='both', which='major', labelsize=9)
        plt2.ax.set_xlabel('t(ps)', fontsize=12, fontweight='bold')
        plt2.ax.xaxis.set_label_coords(.6, -0.04)
        plt2.figure.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)
        plt2.draw()

    @pyqtSlot("double")
    def on_SpinBox_fc_valueChanged(self, value):
        self.Slider_fc.setValue(value)
        self.Beat()

    @pyqtSlot("int")
    def on_Slider_fc_valueChanged(self, value):
        self.SpinBox_fc.setValue(value)
        self.Beat()

    @pyqtSlot("double")
    def on_SpinBox_k_valueChanged(self, value):
        self.Slider_k.setValue(value)
        self.Beat()

    @pyqtSlot("int")
    def on_Slider_k_valueChanged(self, value):
        self.SpinBox_k.setValue(value)
        self.Beat()

    @pyqtSlot("double")
    def on_SpinBox_dFreq_valueChanged(self, value):
        self.Beat()

    @pyqtSlot("double")
    def on_SpinBox_dBeta_valueChanged(self, value):
        self.Beat()

    @pyqtSlot("double")
    def on_SpinBox_xParam_valueChanged(self, value):
        self.Beat()

    @pyqtSlot("double")
    def on_SpinBox_tParam_valueChanged(self, value):
        self.Beat()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
