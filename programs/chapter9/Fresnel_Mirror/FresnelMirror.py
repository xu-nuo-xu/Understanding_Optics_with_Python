# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_FresnelMirror import Ui_MainWindow
from numpy import pi, linspace, cos


class FresnelMirror(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(FresnelMirror, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        #-------------------- Input parameters ----------------------------------------
        Lambda = self.SpinBox_Lambda.value() * 1.E-9  # wavelength of light in vaccuum
        a = self.SpinBox_a.value() * 1.E-3  # distance of the source from the Mirrors
        D = self.SpinBox_D.value()       # Distance screen
        Angle = self.SpinBox_Angle.value() * 1.E-3  # Angles
        Dvirt = D + a
        Champ = D * Angle
        X_Mmax = Champ * (1 + 0.1)
        X_Mmin = -Champ * (1 + 0.1)
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 5000
        X = linspace(X_Mmin, X_Mmax, N)  # coordinates of screen
        I = [0 for x in range(len(X))]
        for xi in range(len(X)):
            if X[xi] < -Champ:
                I[xi] = 0
            elif X[xi] >= -Champ and X[xi] <= Champ:
                I[xi] = 1 + cos(4 * pi * Angle * a * X[xi] / Lambda / Dvirt)
            elif X[xi] > Champ:
                I[xi] = 0

#-------------------- Graphs --------------------------------------------------
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(X * 1E3, I, '-r', linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin * 1E3, X_Mmax * 1E3)
        mpl1d.ax.set_xlabel(r'$X (mm)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Fresnel Mirror', fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ Angle = %3.2f \ mrad, \ a = %4.1f \ mm, \ D = %3.2f \ m$" % (
            Lambda, Angle * 1E3, a * 1E3,  D), fontsize=14)
        mpl1d.draw()

    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Angle_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.fig1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = FresnelMirror()
    MainWindow.show()
    sys.exit(app.exec_())
