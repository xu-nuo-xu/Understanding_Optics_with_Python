# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_rect2D import Ui_MainWindow
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
        N = 400
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        B = (k * b * X) / (2. * f_2)
        H = (k * h * Y) / (2. * f_2)  # intermediate variable
        # 2D & 3 D representation
        BB, HH = meshgrid(B, H)
        I = ((sin(BB) / BB)**2) * ((sin(HH) / HH)**2)

        # figure 2D
        mpl2d = self.mplwidget2D.canvas
        mpl2d.ax.clear()
        mpl2d.ax.imshow(I, cmap=cm.gray, interpolation='bilinear',
                        origin='lower', vmin=0, vmax=0.01)
        mpl2d.ax.set_xlabel(u'$X (m)$', fontsize=12, fontweight='bold')
        mpl2d.ax.set_ylabel(u'$Y (m)$', fontsize=12, fontweight='bold')
        mpl2d.ax.set_xticks(linspace(0, N, 5))
        mpl2d.ax.set_xticklabels(linspace(X_Mmin, X_Mmax, 5),  color='r')
        mpl2d.ax.set_yticks(linspace(0, N, 5))
        mpl2d.ax.set_yticklabels(linspace(Y_Mmin, Y_Mmax, 5),  color='r')
        mpl2d.figure.suptitle(
            'Fraunhofer Diffraction by rectangular aperture', fontsize=14, fontweight='bold')
        mpl2d.ax.set_title(r"$\lambda = %.3e \ m, \ b = %.2e \ m, \ h = %.2e \ m, \ f_2 = %.1f \ m$" % (
            lamda, b, h, f_2), fontsize=10)
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
