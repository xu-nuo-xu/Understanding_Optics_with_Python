# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_rect3D import Ui_MainWindow
from numpy import pi, linspace, meshgrid, sin
import matplotlib.cm as cm


class Rectangular(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        lamda = self.slider_lambda.value() * 1.E-9
        k = (2. * pi) / lamda  # wavelength of light in vaccuum

        b = self.slider_b.value() * 1.E-5
        # dimensions of diffracting rectangular aperture (m)
        h = self.slider_h.value() * 1.E-5
        #b is along (Ox) and h is along (Oy)
        f_2 = self.slider_f2.value()     # f2 is the focal length of the lens L2 (m)
        a = self.slider_a.value() * 1.E-2  # Side of a square-shaped screen (m)
        # The width of the central maximum along (Ox)
        dx = 1.E2 * (2 * lamda * f_2) / b
        self.lineEdit_dx.setText(str("%.3f" % dx))
        # The width of the central maximum along (Oy)
        dy = 1.E2 * (2 * lamda * f_2) / h
        self.lineEdit_dy.setText(str("%.3f" % dy))
        X_Mmax = a / 2.
        X_Mmin = -a / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 200
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        # 2D & 3 D representation
        XX, YY = meshgrid(X, Y)
        B = (k * b * XX) / (2. * f_2 * pi)
        H = (k * h * YY) / (2. * f_2 * pi)  # intermediate variable
        I = ((sin(B) / B)**2) * ((sin(H) / H)**2)
        # 3D
        mpl3d = self.mplwidget3D.canvas
        mpl3d.ax.clear()

        mpl3d.ax.plot_surface(B, H, I, cmap=cm.plasma,
                              alpha=0.8)
        mpl3d.ax.set_zlim3d(0, 1)
        mpl3d.ax.set_xlabel(r'$X \ (m)$', fontsize=12, fontweight='bold')
        mpl3d.ax.set_ylabel(r'$Y \ (m)$', fontsize=12, fontweight='bold')
        mpl3d.ax.set_zlabel(r'$I(X, Y)/I_0$', fontsize=12, fontweight='bold')
        mpl3d.figure.suptitle(
            'Fraunhofer Diffraction of rectangular aperture', fontsize=14, fontweight='bold')
        mpl3d.ax.set_title(r"$\lambda = %.3e \ m, \ b = %.2e \ m, \ h = %.2e \ m, \ f_2 = %.1f \ m$" % (
            lamda, b, h, f_2), fontsize=10)
        mpl3d.draw()

    @pyqtSlot("int")
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_b_valueChanged(self, value):

        self.SpinBox_b.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_h_valueChanged(self, value):

        self.SpinBox_h.setValue(value)
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
    def on_SpinBox_h_valueChanged(self, value):

        self.slider_h.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):

        self.slider_a.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):

        self.slider_f2.setValue(value)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = Rectangular()
    MyApplication.show()
    sys.exit(app.exec_())
