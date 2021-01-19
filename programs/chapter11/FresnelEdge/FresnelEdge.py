# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_FresnelEdge import Ui_MainWindow
from numpy import loadtxt, pi, sqrt, double, cos, sin, sign, linspace, real, imag
import matplotlib.cm as cm

an, bn, cn, dn = loadtxt('coef.dat', comments='#',
                         delimiter=None, usecols=(0, 1, 2, 3), unpack=True)


class FresnelEdge(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global P1_old, P2_old
        super(FresnelEdge, self).__init__(parent)
        self.setupUi(self)

        self.PlotFresnelEdge()

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

    def PlotFresnelEdge(self):
        '''
        Calculate the Fresnel sine and cosine functions

        '''
        #-------------------- Input parameters ----------------
        Lambda = self.Slider_Lambda.value() * 1.E-09
        D = self.Slider_D.value() * 1.E-02
        N = 1000
        X_Mmin = -5 * 1.E-3
        X_Mmax = 5 * 1.E-3
        coef = -sqrt(2 / Lambda / D)
        x = linspace(X_Mmin, X_Mmax, N)
        x1 = coef * x
        FC = self.Fresnel_C(x1, N)
        FS = self.Fresnel_S(x1, N)

        I = []
        for i in range(N):

            ix = complex(0.5 - FC[i], 0.5 - FS[i])
            Intens = (real(ix)**2 + imag(ix)**2) / 2.
            I.append(Intens)
        I2D_0 = []
        I2D_1 = []
        for i in range(N):
            for j in range(2):
                I2d = I[i]
                I2D_0.append(I2d)
            I2D_1.append(I2D_0)
#-------------------- Graphs --------------------------------------------------
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.imshow(I2D_1, cmap=cm.gray, interpolation='bilinear',
                        origin='lower', extent=[min(x * 100), max(x * 100), min(I), max(I)], aspect='auto')
        mpl1d.ax.plot(x * 100, I, '-r', linewidth=2)
        mpl1d.draw()

    @pyqtSlot("int")
    def on_Slider_Lambda_valueChanged(self, value):
        self.SpinBox_Lambda.setValue(value)
        self.PlotFresnelEdge()

    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.Slider_Lambda.setValue(value)

    @pyqtSlot("int")
    def on_Slider_D_valueChanged(self, value):
        self.SpinBox_D.setValue(value)
        self.PlotFresnelEdge()

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.Slider_D.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = FresnelEdge()
    MainWindow.show()
    sys.exit(app.exec_())
