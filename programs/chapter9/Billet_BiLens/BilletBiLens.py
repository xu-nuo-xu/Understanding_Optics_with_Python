# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_BilletBiLens import Ui_MainWindow
from numpy import pi, linspace, cos


class BilletBiLens(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(BilletBiLens, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        #-------------------- Input parameters ----------------------------------------
        Radius = self.SpinBox_Radius.value() * 1.E-2    # Lens radius
        Focal = self.SpinBox_Focal.value() * 1.E-2     # Focal length
        a = self.SpinBox_a.value() * 1.E-3         # bi-lenses distance
        Lambda = self.SpinBox_Lambda.value() * 1.E-9    # Wavelength (vaccuum)
        D = self.SpinBox_D.value()               # Distance screen
        d1 = a / 2 * Focal / Radius
        d2 = 2 * d1
        InterFrange = Lambda * D / a                      # Fringe width
        x_limit1 = abs(Radius / Focal * D - a / 2)          # Limits of the
        x_limit2 = a / 2                                # observation field
        X_Mmin = -0.75 * a
        X_Mmax = -1 * X_Mmin
        N = 5000
        X = linspace(X_Mmin, X_Mmax, N)  # coordinates of screen
        I = [0 for x in range(len(X))]
        if D < d1:
            for xi in range(len(X)):
                I[xi] = 0
        elif D >= d1 and D < d2:
            for xi in range(len(X)):
                if abs(X[xi]) <= x_limit1:
                    I[xi] = 0.5 * (1 + cos(2 * pi * X[xi] / InterFrange))
        elif D >= d2:
            for xi in range(len(X)):
                if(abs(X[xi]) <= x_limit2):
                    I[xi] = 0.5 * (1 + cos(2 * pi * X[xi] / InterFrange))
        d1 = d1 * 1E3
        d2 = d2 * 1E3
        InterFrange = InterFrange * 1E6
        self.lineEdit_D1.setText(str("%.3f" % d1))  # D1 and D2 and
        self.lineEdit_D2.setText(str("%.3f" % d2))  # fringe width displayed
        self.lineEdit_InterFringe.setText(str("%.3f" % InterFrange))

#-------------------- Graphs --------------------------------------------------
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(X * 1E3, I, '-r', linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin * 1E3, X_Mmax * 1E3)
        mpl1d.ax.set_ylim(0, 1.01)
        mpl1d.ax.set_xlabel(r'$X (mm)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Billet Bi-Lenses',
                              fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ a = %4.3f \ mm, \ D = %3.2f \ m$" % (
            Lambda, a * 1E3,  D), fontsize=14)
        mpl1d.draw()

    @pyqtSlot("double")
    def on_SpinBox_Radius_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Focal_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.fig1()

    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.fig1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = BilletBiLens()
    MainWindow.show()
    sys.exit(app.exec_())
