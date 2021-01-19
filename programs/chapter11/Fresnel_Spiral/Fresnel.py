# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Ui_Fresnel import Ui_MainWindow
import os
from numpy import loadtxt, pi, linspace, sqrt, double, cos, sin, sign, arange
import matplotlib.pyplot as plt


global Delta_PushButton, P1_old, P2_old
Delta_PushButton = 0

an, bn, cn, dn = loadtxt('coef.dat', comments='#',
                         delimiter=None, usecols=(0, 1, 2, 3), unpack=True)

filename = "Intensity.txt"


class Fresnel(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        global P1_old, P2_old
        super(Fresnel, self).__init__(parent)
        self.setupUi(self)
        P1_old = self.SpinBox_P1.value()
        P2_old = self.SpinBox_P2.value()
        try:
            os.remove(filename)
        except OSError:
            pass
        self.PlotFresnel()

    def ff1(self, x):
        som = 0
        for i in range(len(an)):
            fn = (8 / pi)**(i + 0.5) * dn[i]
            som = som + fn * x**(-2 * i - 1)
        return som

    def gg1(self, x):
        som = 0
        for i in range(len(an)):
            gn = (8 / pi)**(i + 0.5) * cn[i]
            som = som + gn * x**(-2 * i - 1)
        return som

    def ff2(self, x):
        som = 0
        for i in range(len(an)):
            fn = (pi / 8)**(i + 0.5) * bn[i]
            som = som + (fn) * x**(2 * i + 1)
        return som

    def gg2(self, x):
        som = 0
        for i in range(len(an)):
            gn = (pi / 8)**(i + 0.5) * an[i]
            som = som + gn * x**(2 * i + 1)
        return som

    def Fresnel_C(self, x, N):
        pivot = sqrt(8 / double(pi))
        xx = abs(x)
        FC = []
        for i in range(N):
            if xx[i] >= pivot:
                fresnelc = sign(x[i]) * (0.5 + self.ff1(xx[i]) * sin(0.5 * pi *
                                                                     (xx[i]**2)) + self.gg1(xx[i]) * cos((0.5 * pi) * (xx[i]**2)))
            elif xx[i] < pivot:
                fresnelc = sign(x[i]) * (self.ff2(xx[i]) * sin(0.5 * double(pi)
                                                               * (xx[i]**2)) + self.gg2(xx[i]) * cos(0.5 * pi * (xx[i]**2)))
            FC.append(fresnelc)
        return FC

    def Fresnel_S(self, x, N):
        pivot = sqrt(8 / double(pi))
        xx = abs(x)
        FS = []
        for i in range(N):
            if xx[i] >= pivot:
                fresnels = -sign(x[i]) * (-0.5 + self.ff1(xx[i]) * cos(
                    0.5 * pi * (xx[i]**2)) - self.gg1(xx[i]) * sin(0.5 * pi * (xx[i]**2)))
            elif xx[i] < pivot:
                fresnels = -sign(x[i]) * (self.ff2(xx[i]) * cos(0.5 * double(pi)
                                                                * (xx[i]**2)) - self.gg2(xx[i]) * sin(0.5 * pi * (xx[i]**2)))
            FS.append(fresnels)
        return FS

    def PlotFresnel(self):
        global Delta_PushButton, P1_old, P2_old
        '''
        Calculate the Fresnel sine and cosine functions
        '''
        N = 1000
        a = self.SpinBox_a1.value()
        X_Mmax = a / 2.
        X_Mmin = -a / 2.
        x = linspace(X_Mmin, X_Mmax, N)
        FC = self.Fresnel_C(x, N)
        FS = self.Fresnel_S(x, N)

        #-------------- Figure 1 D --------------------------------------------
        mpl1d = self.mplwidget_integral.canvas
        mpl1d.ax.clear()
        mpl1d.ax.grid(True)
        mpl1d.ax.spines['left'].set_position('center')
        mpl1d.ax.spines['right'].set_color('none')
        mpl1d.ax.spines['bottom'].set_position('center')
        mpl1d.ax.spines['top'].set_color('none')
        mpl1d.ax.spines['left'].set_smart_bounds(True)
        mpl1d.ax.spines['bottom'].set_smart_bounds(True)
        mpl1d.ax.xaxis.set_ticks_position('bottom')
        mpl1d.ax.yaxis.set_ticks_position('left')
        mpl1d.ax.plot(x, FC, '-b', linewidth=2)
        mpl1d.ax.plot(x, FS, '-r', linewidth=2)
        mpl1d.ax.axhline(y=.5, color='g', linestyle='--', linewidth=2)
        mpl1d.ax.axhline(y=-.5, color='g', linestyle='--', linewidth=2)
        mpl1d.ax.axvline(x=0, color='k', linestyle=':', linewidth=0.5)
        mpl1d.ax.text(-0.14, 0.8, r'0.5', fontsize=12, fontweight='bold',
                      color='green', transform=mpl1d.ax.transAxes)
        mpl1d.ax.text(-0.14, 0.18, r'-0.5', fontsize=12, fontweight='bold',
                      color='green', transform=mpl1d.ax.transAxes)
        mpl1d.ax.text(0, 0.93, r'C(x)', fontsize=12, fontweight='bold',
                      color='blue', transform=mpl1d.ax.transAxes)
        mpl1d.ax.text(0.1, 0.93, r'S(x)', fontsize=12, fontweight='bold',
                      color='red', transform=mpl1d.ax.transAxes)
        mpl1d.ax.set_xlim(X_Mmin, X_Mmax)
        mpl1d.figure.suptitle('Fresnel integals',
                              fontsize=14, fontweight='bold')
        mpl1d.draw()

        #-------------- Graph of the Spiral -----------------------------------
        mpl1ds = self.mplwidget_spiral.canvas
        mpl1ds.ax.clear()
        mpl1ds.ax.grid(True)
        mpl1ds.ax.spines['left'].set_position('center')
        mpl1ds.ax.spines['right'].set_color('none')
        mpl1ds.ax.spines['bottom'].set_position('center')
        mpl1ds.ax.spines['top'].set_color('none')
        mpl1ds.ax.spines['left'].set_smart_bounds(True)
        mpl1ds.ax.spines['bottom'].set_smart_bounds(True)
        mpl1ds.ax.xaxis.set_ticks_position('bottom')
        mpl1ds.ax.yaxis.set_ticks_position('left')
        mpl1ds.ax.plot(FC, FS, 'k-', label='x=C,   y=S',
                       linewidth=2, alpha=0.8)
        ind = arange(-2., 0, 0.2)
        s_c, s_s = self.Fresnel_C(ind, len(ind)), self.Fresnel_S(ind, len(ind))
        for i in range(len(ind)):
            mpl1ds.ax.annotate("%.4s" % str(ind[i]), xy=(s_c[i], s_s[i]), xycoords='data',
                               xytext=(0, -1), textcoords='offset points',
                               arrowprops=dict(arrowstyle="-"), fontsize=8, color='red',
                               bbox=dict(boxstyle="round", fc=(
                                   1, 1, 1), ec="none", alpha=0.5),
                               horizontalalignment='right', verticalalignment='top')
        ind = arange(0, 2., 0.2)
        s_c, s_s = self.Fresnel_C(ind, len(ind)), self.Fresnel_S(ind, len(ind))
        for i in range(len(ind)):
            mpl1ds.ax.annotate("%.4s" % str(ind[i]), xy=(s_c[i], s_s[i]), xycoords='data',
                               xytext=(0, -1), textcoords='offset points',
                               arrowprops=dict(arrowstyle="-"), fontsize=8, color='red',
                               bbox=dict(boxstyle="round", fc=(
                                   1, 1, 1), ec="none", alpha=0.8),
                               horizontalalignment='right', verticalalignment='top')

        P1 = P1_old + Delta_PushButton
        P2 = P2_old + Delta_PushButton
#        print (P1,P2)
        dP1 = P1 * 1.001
        dP2 = P2 * 1.001
        u1 = linspace(P1, dP1, 1)
        u2 = linspace(P2, dP2, 1)
        FCp1, FSp1 = self.Fresnel_C(u1, 1), self.Fresnel_S(u1, 1)
        FCp2, FSp2 = self.Fresnel_C(u2, 1), self.Fresnel_S(u2, 1)
        Intensity = sqrt((FCp1[0] - FCp2[0])**2 + (FSp1[0] - FSp2[0])**2)
        X_Intensity = (P1 + P2) / 2
#        print(X_Intensity,Intensity)
        self.f = open('Intensity.txt', 'a')
        self.f.write(str(X_Intensity) + ',' + str(Intensity) + '\n')
        self.f.close()
        mpl1ds.ax.plot([FCp1, FCp2], [FSp1, FSp2],
                       linestyle='--', marker='o', markersize=10, markeredgecolor='r')
        mpl1ds.draw()
        P1_old = P1
        P2_old = P2

    def GrapheUpdate(self):
        x, I = loadtxt("Intensity.txt", delimiter=",", unpack=True)
        if plt.fignum_exists(1):
            plt.close()

        fig = plt.figure(figsize=(5, 3))
        fig.canvas.manager.window.move(800, 20)
        fig.canvas.set_window_title('Intensity')
        plt.plot(x, I, linestyle='--', marker='o', color='r',
                 markersize=6, markeredgecolor='b')
        plt.ylim(0, 1.6)
        plt.title('Fresnel diffraction', fontsize=16, weight='bold')
        plt.xlabel('x', fontsize=12, weight='bold')
        plt.ylabel('I (x)', fontsize=12, weight='bold')
        plt.grid()
        plt.show()

    @pyqtSlot("int")
    def on_SpinBox_N1_valueChanged(self, value):
        self.Slider_N1.setValue(value)
        self.PlotFresnel()

    @pyqtSlot("double")
    def on_SpinBox_a1_valueChanged(self, value):
        self.Slider_a1.setValue(value)
        self.PlotFresnel()

    @pyqtSlot("double")
    def on_SpinBox_P1_valueChanged(self, value):
        global Delta_PushButton, P1_old, P2_old
        Delta_PushButton = 0
        P1_old = self.SpinBox_P1.value()
        P2_old = self.SpinBox_P2.value()
        self.PlotFresnel()

    @pyqtSlot("double")
    def on_SpinBox_P2_valueChanged(self, value):
        global Delta_PushButton, P1_old, P2_old
        Delta_PushButton = 0
        P1_old = self.SpinBox_P1.value()
        P2_old = self.SpinBox_P2.value()
        self.PlotFresnel()

    @pyqtSlot("int")
    def on_Slider_N1_valueChanged(self, value):
        self.SpinBox_N1.setValue(value)
        self.PlotFresnel()

    @pyqtSlot("int")
    def on_Slider_a1_valueChanged(self, value):
        self.SpinBox_a1.setValue(value)
        self.PlotFresnel()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        global Delta_PushButton
        Delta_PushButton = 0.1
        self.PlotFresnel()
        self.GrapheUpdate()

    @pyqtSlot()
    def on_Button_reset_clicked(self):
        global Delta_PushButton, P1_old, P2_old
        Delta_PushButton = 0
        P1_old = self.SpinBox_P1.value()
        P2_old = self.SpinBox_P2.value()
        try:
            os.remove(filename)
        except OSError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Fresnel()
    MainWindow.show()
    sys.exit(app.exec_())
