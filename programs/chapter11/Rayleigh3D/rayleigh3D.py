# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_rayleigh3D import Ui_MainWindow
from numpy import pi, linspace, meshgrid
import scipy.special as ss
import matplotlib.cm as cm


class Rayleigh3D(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        lamda = self.slider_lambda.value() * 1.E-9
        k = (2. * pi) / lamda  # wavelength of light in vaccuum

        a = self.slider_a.value() * 1.E-6  # radius of the circular aperture (m)
        d = self.slider_d.value() * 1.E-3  # distance of the source from the optic axis
        f_2 = self.slider_f2.value()     # f2 is the focal length of the lens L2 (m)
        e = self.slider_e.value() * 1.E-2  # Side of a square-shaped screen (m)
        X_Mmax = e / 2.
        X_Mmin = -e / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 200
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        # 2D representation
        XX, YY = meshgrid(X, Y)
        rm1 = ((XX - d)**2 + YY**2)**0.5
        A1 = k * a * rm1 / f_2
        I1 = (ss.jv(1, A1) / A1)**2
        rm2 = ((XX + d)**2 + YY**2)**0.5
        A2 = k * a * rm2 / f_2
        I2 = (ss.jv(1, A2) / A2)**2
        I = I1 + I2
        # figure 3D
        mpl3d = self.mplwidget3D.canvas
        mpl3d.ax.clear()
        mpl3d.ax.plot_surface(XX, YY, I, cmap=cm.plasma,
                              alpha=0.8)
        mpl3d.ax.set_zlim3d(0, .5)
        mpl3d.ax.set_xticks([])
        mpl3d.ax.set_yticks([])
        mpl3d.ax.set_zlabel(r'$I(X, Y)/I_0$', fontsize=12, fontweight='bold')
        mpl3d.figure.suptitle('The Rayleigh Criterion',
                              fontsize=14, fontweight='bold')
        mpl3d.ax.set_title(r"$\lambda = %.3e \ m, \ a = %.2e \ m, \ d = %.2e \ m, \ f_2 = %.1f \ m$" % (
            lamda, a, d,  f_2), fontsize=10)
        mpl3d.draw()

    @pyqtSlot("int")
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_a_valueChanged(self, value):

        self.SpinBox_a.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_d_valueChanged(self, value):

        self.SpinBox_d.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_e_valueChanged(self, value):

        self.SpinBox_e.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_f2_valueChanged(self, value):

        self.SpinBox_f2.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_SpinBox_lambda_valueChanged(self, value):

        self.slider_lambda.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):

        self.slider_a.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_d_valueChanged(self, value):

        self.slider_d.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_e_valueChanged(self, value):

        self.slider_e.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):

        self.slider_f2.setValue(value)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = Rayleigh3D()
    MyApplication.show()
    sys.exit(app.exec_())
