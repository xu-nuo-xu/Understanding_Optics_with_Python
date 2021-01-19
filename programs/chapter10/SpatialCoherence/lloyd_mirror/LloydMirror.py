# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Ui_LloydMirror import Ui_MainWindow
from numpy import pi, linspace, sin, cos


class LloydMirror(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(LloydMirror, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        Lambda = self.SpinBox_Lambda.value() * 1.E-9  # wavelength of light in vaccuum
        a = self.SpinBox_a.value() * 1.E-3  # distance of the source from the plan
        D = self.SpinBox_D.value()
        b = self.SpinBox_b.value() * 1.E-3
        I0 = 0.25
        e = 1 * 1.E-2  # Side of a square-shaped screen (m)
        X_Mmax = e
        X_Mmin = -e

        N = 1000
        X = linspace(X_Mmin, X_Mmax, N)
        A = 2 * pi * b * X / Lambda / D
        B = 4 * pi * a * X / Lambda / D
        Sinc1 = 2 * I0 * (1 - sin(A) / A)
        Sinc2 = 2 * I0 * (1 + sin(A) / A)
        I = 2 * I0 * (1 - (sin(A) / A) * cos(B))

        Period_X = Lambda * D / 2 / a * 1E3
        self.lineEdit_Period.setText(str("%.3f" % Period_X))
        Contrast_0 = Lambda * D / 2 / b * 1E3
        self.lineEdit_Contrast.setText(str("%.3f" % Contrast_0))

        # figure 1 D
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(X * 1E3, Sinc1, '--b', X * 1E3, Sinc2,
                      '--b', X * 1E3, I, '-r', linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin * 1E3, X_Mmax * 1E3)
        mpl1d.ax.set_ylim(0, 1.01)
        mpl1d.ax.set_xlabel(r'$X (mm)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Lloyd Mirror', fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ b = %.2e \ m, \ a = %.2e \ m, \ D = %.2e \ m$" % (
            Lambda, b, a,  D), fontsize=14)
        mpl1d.ax.annotate(r"$X_{1}$", xy=(0, 0), xytext=(
            0.1, -0.05), fontsize=18, color='red')
        mpl1d.ax.annotate(r"$X_{2}$", xy=(0, 0), xytext=(
            7, -0.05), fontsize=18, color='blue')
        mpl1d.draw()

    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_b_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.fig1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = LloydMirror()
    MainWindow.show()
    sys.exit(app.exec_())
