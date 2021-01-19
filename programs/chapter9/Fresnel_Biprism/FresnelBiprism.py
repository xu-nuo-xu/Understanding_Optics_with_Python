# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Ui_FresnelBiprism import Ui_MainWindow
from numpy import pi, linspace, sin, cos, tan, sinc


class FresnelBiprism(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(FresnelBiprism, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        #-------------------- Input parameters ----------------------------------------
        Slit1_Width = self.SpinBox_Source1.value() * 1.E-6  # Source 1 width (0)
        Slit2_Width = self.SpinBox_Source2.value() * 1.E-6  # Source 2 width (0)
        a = self.SpinBox_a.value() * 1.E-0  # Source-Mirrors distance (d)
        n_Index = self.SpinBox_Index.value()
        Angle = self.SpinBox_Angle.value() * 1.E-3  # Angles (A)
        Height = self.SpinBox_Height.value() * 1.E-2  # Prism Height (h)
        Lambda = self.SpinBox_Lambda.value() * 1.E-9  # Wavelength (vaccuum)
        D = self.SpinBox_D.value()       # Distance screen (D)

        Base_Prism = tan(Angle) * Height
        Distance = a + Base_Prism
        InterFrange = Lambda * (D + Distance) / \
            (2 * Distance * (n_Index - 1) * Angle)
        Arg_sinc1 = sinc(pi * D * Slit1_Width / (InterFrange * Distance))
        Arg_sinc2 = sinc(pi * D * Slit2_Width / (InterFrange * Distance))

        X_Mmin = -D * (n_Index - 1) * Angle
        X_Mmax = -1 * X_Mmin
        N = 5000
        X = linspace(X_Mmin, X_Mmax, N)  # coordinates of screen
        I_1 = [0 for x in range(len(X))]
        I_2 = [0 for x in range(len(X))]
        for xi in range(len(X)):
            I_1[xi] = (1 + Arg_sinc1 * cos(2 * pi * X[xi] / InterFrange))
            I_2[xi] = (1 + Arg_sinc2 * cos(2 * pi * X[xi] / InterFrange))

#-------------------- Graphs --------------------------------------------------
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(X * 1E3, I_1, '-b', linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin * 1E3, X_Mmax * 1E3)
        mpl1d.ax.set_xlabel(r'$X (mm)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle(
            'Fresnel Biprism', fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ Angle = %3.2f \ mrad, \ a = %4.1f \ mm, \ D = %3.2f \ m$" % (
            Lambda, Angle * 1E3, a * 1E3,  D), fontsize=14)
        mpl1d.draw()

    @pyqtSlot("double")
    def on_SpinBox_Source1_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Source2_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Index_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Angle_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Height_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.fig1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = FresnelBiprism()
    MainWindow.show()
    sys.exit(app.exec_())
