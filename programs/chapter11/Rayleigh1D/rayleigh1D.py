# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_rayleigh1D import Ui_MainWindow
from numpy import pi, linspace
import scipy.special as ss


class Rayleigh1D(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        lamda = self.slider_lambda.value() * 1.E-9
        k = (2. * pi) / lamda  # wavelength of light in vaccuum
        a = self.SpinBox_a.value() * 1.E-6  # radius of the circular aperture (m)
        d = self.SpinBox_d.value() * 1.E-3  # distance of the source from the optic axis
        f_2 = self.slider_f2.value()     # f2 is the focal length of the lens L2 (m)
        e = self.slider_e.value() * 1.E-3  # Side of a square-shaped screen (m)
#        dx =  2*1.22*D*lamda/b*1.E+2
        dx = 1.22 * lamda * f_2 / a * 1.E+2
        self.lineEdit_dx.setText(str("%.4f" % dx))
        X_Mmax = e / 2.
        X_Mmin = -e / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 800
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        # 1D representation
        rm1 = X - d
        A1 = k * a * rm1 / f_2
        I1 = 4 * (ss.jv(1, A1) / A1)**2
        rm2 = X + d
        A2 = k * a * rm2 / f_2
        I2 = 4 * (ss.jv(1, A2) / A2)**2
        I = I1 + I2

        # figure 1 D
        mpl1d = self.mplwidget1D.canvas
        mpl1d.ax.clear()
        l1, l2, l3 = mpl1d.ax.plot(
            X, I1, 'r', X, I2, 'b', X, I, '-k', linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin, X_Mmax)
        mpl1d.ax.set_xlabel(r'$X (m)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X,Y)/I_0$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('The Rayleigh Criterion',
                              fontsize=14, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ a = %.2e \ m, \ d = %.2e \ m, \ f_2 = %.1f \ m$" % (
            lamda, a, d,  f_2), fontsize=10)
        mpl1d.ax.legend((l1, l2, l3), ('I1', 'I2', 'I'))
        mpl1d.draw()

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
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_d_valueChanged(self, value):
        self.slider_d.setValue(value)
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_e_valueChanged(self, value):
        self.slider_e.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):
        self.slider_f2.setValue(value)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = Rayleigh1D()
    MyApplication.show()
    sys.exit(app.exec_())
