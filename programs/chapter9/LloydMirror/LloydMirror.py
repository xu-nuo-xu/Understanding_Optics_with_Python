# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_LloydMirror import Ui_MainWindow
from numpy import pi, linspace, sin, cos


class LloydMirror(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        """
        super(LloydMirror, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        #-------------------- Input parameters ----------------------------------------
        Lambda = self.SpinBox_Lambda.value() * 1.E-9  # wavelength of light in vaccuum
        # distance of the source from the plan
        a = self.SpinBox_a.value() * 1.E-3
        D = self.SpinBox_D.value()
        b = self.SpinBox_b.value() * 1.E-3
        I0 = 0.5
        e = 2 * 1.E-3  # Side of a square-shaped screen (m)
        X_Mmax = e / 2.
        X_Mmin = -e / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 800
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        A = 2 * pi * b * X / Lambda / D
        B = 4 * pi * a * X / Lambda / D
        Sinc1 = 2 * I0 * (1 - sin(A) / A)
        Sinc2 = 2 * I0 * (1 + sin(A) / A)
        I = 2 * I0 * (1 - (sin(A) / A) * cos(B))
#-------------------- Graphs --------------------------------------------------
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(X, Sinc1, '--b', X, Sinc2,
                      '--b', X, I, '-r', linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin, X_Mmax)
        mpl1d.ax.set_xlabel(r'$X (m)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Lloyd Mirror', fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ b = %.3e \ m, \ a = %.3e \ m, \ D = %.3e \ m$" % (
            Lambda, b, a,  D), fontsize=14)
        
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
