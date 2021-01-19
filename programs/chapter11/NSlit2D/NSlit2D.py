# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_NSlit2D import Ui_MainWindow
from numpy import pi, linspace, sin, meshgrid
import matplotlib.cm as cm


class NSlit2D(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        lamda = self.slider_lambda.value() * 1.E-9
        k = (2. * pi) / lamda  # wavelength of light in vaccuum
        b = self.slider_b.value() * 1.E-6  # dimensions of diffracting slit (m)
        #b is along (Ox)
        n = self.slider_n.value()  # number of slits
        e = self.slider_e.value() * 1.E-6
        # d=b+e
        f_2 = self.slider_f2.value()     # f2 is the focal length of the lens L2 (m)
        a = self.slider_a.value() * 1.E-3  # Side of a square-shaped screen (m)
        X_Mmax = a / 2.
        X_Mmin = -a / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 800
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        # 2D & 3 D representation
        XX, YY = meshgrid(X, Y)
        B = (k * b * XX) / (2. * f_2)
        A = (k * e * XX) / (2. * f_2)  # intermediate variable
        # 1D representation
        I = (1 / n**2) * ((sin(B) / B)**2) * (sin(n * A) / sin(A))**2
        # figure 2 D
        mpl2d = self.mplwidget2D.canvas
        mpl2d.ax.clear()
        mpl2d.ax.imshow(I, cmap=cm.gray, interpolation='bilinear',
                        origin='lower', vmin=0, vmax=.2)
        mpl2d.ax.set_xlabel(u'$X (m)$', fontsize=12, fontweight='bold')
        mpl2d.ax.set_ylabel(u'$Y (m)$', fontsize=12, fontweight='bold')
        mpl2d.ax.set_xticks(linspace(0, N, 5))
        mpl2d.ax.set_xticklabels(linspace(X_Mmin, X_Mmax, 5),  color='r')
        mpl2d.ax.set_yticks(linspace(0, N, 5))
        mpl2d.ax.set_yticklabels(linspace(Y_Mmin, Y_Mmax, 5),  color='r')
        mpl2d.figure.suptitle('Fraunhofer Diffraction by %s slits' %
                              n, fontsize=14, fontweight='bold')
        mpl2d.ax.set_title(u"$\lambda = %.1e \ m, \ b = %.3e \ m, \ a = %.1e \ m, \ f_2 = %.0f \ m$" % (lamda, b, e, f_2),
                           fontsize=12)
        mpl2d.draw()

    @pyqtSlot("int")
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_b_valueChanged(self, value):
        self.SpinBox_b.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_n_valueChanged(self, value):
        self.SpinBox_n.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_e_valueChanged(self, value):
        self.SpinBox_e.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_f2_valueChanged(self, value):
        self.SpinBox_f2.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_SpinBox_lambda_valueChanged(self, value):
        self.slider_lambda.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_b_valueChanged(self, value):
        self.slider_b.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_n_valueChanged(self, value):
        self.slider_n.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_e_valueChanged(self, value):
        self.slider_e.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.slider_a.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):
        self.slider_f2.setValue(value)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = NSlit2D()
    MyApplication.show()
    sys.exit(app.exec_())
