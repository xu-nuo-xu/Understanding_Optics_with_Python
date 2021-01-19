# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_circ3D import Ui_MainWindow
from numpy import pi, linspace, meshgrid
import scipy.special as ss
import matplotlib.cm as cm


class Circular3D(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        lamda = self.slider_lambda.value() * 1.E-9
        k = (2. * pi) / lamda  # wavelength of light in vaccuum

        a = self.slider_a.value() * 1.E-6  # radius of the circular aperture (m)
        f_2 = self.slider_f2.value()     # f2 is the focal length of the lens L2 (m)
        e = self.slider_e.value() * 1.E-2  # Side of a square-shaped screen (m)
        X_Mmax = e / 2.
        X_Mmin = -e / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 200
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        XX, YY = meshgrid(X, Y)
        # 3D representation
        q = (XX**2 + YY**2)**0.5  # intermediate variable
        beta = k * a * q / f_2
        I = (2 * ss.jv(1, beta) / beta)**2
        # figure 3D
        mpl3d = self.mplwidget3D.canvas
        mpl3d.ax.clear()
        mpl3d.ax.plot_surface(XX, YY, I, cmap=cm.jet, vmin=0, vmax=0.1,
                              alpha=0.8)
        mpl3d.ax.set_zlim3d(0, 1)
        mpl3d.ax.set_xticks([])
        mpl3d.ax.set_yticks([])
        mpl3d.ax.set_zlabel(r'$I(X, Y)/I_0$', fontsize=12, fontweight='bold')
        mpl3d.figure.suptitle(
            'Fraunhofer Diffraction of circular aperture', fontsize=14, fontweight='bold')
        mpl3d.ax.set_title(r"$\lambda = %.3e \ m, \ a = %.2e \ m, \ f_2 = %.1f \ m$" % (
            lamda, a, f_2), fontsize=10)
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
    def on_SpinBox_e_valueChanged(self, value):

        self.slider_e.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):

        self.slider_f2.setValue(value)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = Circular3D()
    MyApplication.show()
    sys.exit(app.exec_())
