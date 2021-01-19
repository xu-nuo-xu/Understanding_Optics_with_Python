# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

import numpy as np
from Ui_Gaussian import Ui_MainWindow
from numpy import pi, linspace, cos


class Gaussian(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Gaussian, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        global Lambda_R, Lambda_P, a, D, Angle
        Lambda = self.SpinBox_Lambda.value() * 1.E-9  # Wavelength of light in vaccuum
        b = self.SpinBox_a.value() * 1.E-9      # Width of the ray
        Angle = self.SpinBox_Angle.value()        # Angles
        e = self.SpinBox_e.value() * 1E-6       # Thickness of the blade

        speed = 2.99792458 * 1.E+8
        lambda_i = Lambda - b / 2  # Passer aux frÈquences
        lambda_s = Lambda + b / 2
        alpha = 0.5 * b / np.sqrt(np.log(2)) * speed / lambda_i / lambda_s
        fact2 = speed / np.pi / alpha

        X_Mmin = 0
        # Longueur de cohérence Lc/2 (/2 car diffmarch*2)
        X_Mmax = fact2 * np.sqrt(np.log(2)) / 2
#        print (2*X_Mmax, fact2,alpha)
        N = 10000
        X = linspace(X_Mmin, X_Mmax, N)  # coordinates of screen
        Intens = [0 for x in range(len(X))]
        g_s = [0 for x in range(len(X))]
        g_i = [0 for x in range(len(X))]

        for xi in range(len(X)):
            diffmarch = 2 * X[xi] * cos(Angle)
            X[xi] = diffmarch
            Intens[xi] = 0.5 * (1 + np.exp(-diffmarch**2 / fact2**2)
                                * cos(2 * pi * diffmarch / Lambda))
            g_s[xi] = 0.5 * (1 + np.exp(-diffmarch**2 / fact2**2))
            g_i[xi] = 0.5 * (1 - np.exp(-diffmarch**2 / fact2**2))

        Lc = 2 * X_Mmax * 1E6
        Contraste = (g_s[N - 1] - g_i[N - 1]) / (g_s[N - 1] + g_i[N - 1])
        middle = 0.5 * (g_s[N - 1] + g_i[N - 1])
        self.lineEdit_Lc.setText(str("%.3f" % Lc))
        self.lineEdit_Contraste.setText(str("%.3f" % Contraste))

        # figure 1 D - For the color look at the color table in hexadecimal (#ff0000)
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        l1, l2 = mpl1d.ax.plot(X * 1E+6, Intens, 'r',
                               X * 1E+6, g_s, 'b', linewidth=1)
        mpl1d.ax.set_xlim(X_Mmin * 1E+6, (2 * X_Mmax + X_Mmax / 5) * 1E+6)
        mpl1d.ax.set_ylim(0, 1.015)
        mpl1d.ax.set_xlabel(r'$ODP (\mu m)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(ODP)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Fresnel Mirror', fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ Angle = %3.2f \ mrad, \ e = %4.1f \ \mu m, \ b = %3.2f \ nm$" % (
            Lambda, Angle * 1E3, e * 1E6, b * 1E9), fontsize=14)

        ind = int(N / 2)
        mpl1d.ax.annotate(r'$f(\delta)$',
                          # fraction, fraction
                          xy=(X[ind] * 1E6, 0.5), xytext=(X[ind] * 1E6, 0.5),
                          arrowprops=dict(facecolor='black', shrink=0.05),
                          horizontalalignment='left', verticalalignment='bottom',
                          fontsize=20, fontweight='bold', color='r',
                          bbox=dict(boxstyle="round,pad=0.3",
                                    fc="white", alpha=0.8),
                          )
        ind = int(N / 2)
        mpl1d.ax.annotate(r'$g(\delta)$',
                          # fraction, fraction
                          xy=(X[ind] * 1E6, g_s[ind]), xytext=(X[ind] * 1E6, g_s[ind]),
                          arrowprops=dict(facecolor='black', shrink=0.05),
                          horizontalalignment='left', verticalalignment='bottom',
                          fontsize=20, fontweight='bold', color='b',
                          )
        mpl1d.ax.annotate('', xy=(X[N - 1] * 1E6 + 0.5, g_s[N - 1]), xytext=(X[N - 1] * 1E6 + 0.5, g_i[N - 1]),
                          arrowprops=dict(arrowstyle='<->',
                                          edgecolor='k', lw=3),
                          horizontalalignment='center', verticalalignment='bottom',)
        mpl1d.ax.annotate(r'$\gamma =0.5$',
                          xy=(Lc, 0.5), xytext=(Lc, 0.5),
                          horizontalalignment='right', verticalalignment='center',
                          fontsize=20, fontweight='bold', color='k',
                          bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8),)
        mpl1d.draw()

    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Angle_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.Slider_a.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_Slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_e_valueChanged(self, value):
        self.fig1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Gaussian()
    MainWindow.show()
    sys.exit(app.exec_())
