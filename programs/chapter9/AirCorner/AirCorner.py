# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_AirCorner import Ui_MainWindow

from numpy import pi, sin, cos, linspace


class AirCorner(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(AirCorner, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        Lambda = self.SpinBox_Lambda.value() * 1.E-9  # wavelength of light in vaccum
        AnglCoin = self.SpinBox_CA.value() * 1E-3
        width1 = self.SpinBox_WS1.value() * 1E-3
        width2 = self.SpinBox_WS2.value() * 1E-3
        Dist_Screen = self.SpinBox_D.value()
        Transmit = self.SpinBox_TP.value()
        bb = -4 * pi * sin(AnglCoin) * Dist_Screen / Lambda
        InterFrange = Lambda / 2 / sin(AnglCoin)
        Arg_sinc1 = sin(bb * width1 / 2) / (bb * width1 / 2)
        Arg_sinc2 = sin(bb * width2 / 2) / (bb * width2 / 2)
        contraste = 2 * Transmit / (1 + Transmit * Transmit)
        contraste_1 = contraste * Arg_sinc1
        contraste_2 = contraste * Arg_sinc2
        xmin = 0
        xmax = 10 * InterFrange
        N = 10000
        x = linspace(xmin, xmax, N)
        Intens_1 = 2 * (1 + contraste_1 * cos(2 * pi * x / InterFrange))
        Intens_2 = 2 * (1 + contraste_2 * cos(2 * pi * x / InterFrange))

        # figure 1 D
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(x * 1E6, Intens_1, linestyle='-', color='r', linewidth=2)
        mpl1d.ax.plot(x * 1E6, Intens_2, linestyle='-', color='b', linewidth=2)

        mpl1d.ax.set_xlim(xmin * 1E6, xmax * 1E6)
        mpl1d.ax.set_xlabel(
            r'Position on the screen (10 * Interfrange) (micron)', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'I(x)', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Air Corner', fontsize=14, fontweight='bold')
        mpl1d.draw()

    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_TP_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_WS1_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_WS2_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_CA_valueChanged(self, value):
        self.fig1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = AirCorner()
    MainWindow.show()
    sys.exit(app.exec_())
