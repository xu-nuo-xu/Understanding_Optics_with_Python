# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Ui_PrismaticSlab import Ui_MainWindow
from numpy import pi, cos, linspace, meshgrid, tan
import matplotlib.pyplot as plt
from custom_color import custom_div_cmap


class PrismaticSlab(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(PrismaticSlab, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        global angle, ndx, Lambda1, Lambda2, Lambda3, x, I_R
        global Xmin, Xmax, cbPhi
#--------------------- Inputs + Intensity -------------------------------------
        angle = self.SpinBox_angle.value() * 1.E-3      # Corner angle (theta)
        ndx = self.SpinBox_ndx.value()                # Slab index   (n)
        Lambda1 = self.SpinBox_Lambda1.value() * 1.E-9   # 3 wavelengths depict
        Lambda2 = self.SpinBox_Lambda2.value() * 1.E-9   # the RGB color
        Lambda3 = self.SpinBox_Lambda3.value() * 1.E-9
        Xmin = 0
        Xmax = 1.E-4
        N = 5000
        x = linspace(Xmin, Xmax, N)
        if self.cbPhi.isChecked() == True:           # pi shifting produced
            cbPhi = 1                                  # by reflection
        else:
            cbPhi = 0
        diffmarch1 = 2 * ndx * tan(angle) * x + cbPhi * \
            Lambda1 / 2.  # OPD for Lambda1 (blue)
        I_B = 0.5 * (1 + cos(2 * pi * diffmarch1 / Lambda1)
                     )       # Associated intensity
        diffmarch2 = 2 * ndx * tan(angle) * x + cbPhi * \
            Lambda2 / 2.  # OPD for Lambda1 (green)
        I_G = 0.5 * (1 + cos(2 * pi * diffmarch2 / Lambda2)
                     )       # Associated intensity
        diffmarch3 = 2 * ndx * tan(angle) * x + \
            cbPhi * Lambda3 / 2.  # OPD for Lambda1 (red)
        I_R = 0.5 * (1 + cos(2 * pi * diffmarch3 / Lambda3)
                     )       # Associated intensity
        x = x * 1.E+3

#---------------------  figure 1 D -------------------------------------
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()

        if self.cbr.isChecked() == True:
            mpl1d.ax.plot(x, I_R, linestyle='-', color='r',
                          linewidth=1, picker=0.5)
        else:
            mpl1d.ax.plot([], [])
        if self.cbb.isChecked() == True:
            mpl1d.ax.plot(x, I_B, linestyle='-', color='b', linewidth=1)
        else:
            mpl1d.ax.plot([], [])
        if self.cbg.isChecked() == True:
            mpl1d.ax.plot(x, I_G, linestyle='-', color='g', linewidth=1)
        else:
            mpl1d.ax.plot([], [])

        mpl1d.ax.set_xlim(min(x), max(x))
        mpl1d.ax.set_ylim(0, 1.05)
        mpl1d.ax.set_xlabel(r'$X (mm)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Prismatic Slab', fontsize=14, fontweight='bold')
        mpl1d.ax.plot([0.016, 0.0322], [1, 1], 'g-', lw=2)
        mpl1d.ax.plot([0.016], [1], 'go', markersize=10.)
        mpl1d.ax.plot([0.0322], [1], 'go', markersize=10.)
        mpl1d.ax.annotate(r'$i=16.2 \mu m$', xy=(0.02, 1.01), xytext=(
            0.02, 1.01), fontsize=12, fontweight='bold', color='G')
        mpl1d.draw()

    def figBlue(self):
        global angle, ndx, Lambda1, Lambda2, Lambda3
        global Xmin, Xmax, cbPhi
        N = 200
        x = linspace(Xmin, Xmax, N)
        y = x
        X, Y = meshgrid(x, y)

        diffmarch1 = 2 * ndx * tan(angle) * X + cbPhi * Lambda1 / 2.
        I_B = 0.5 * (1 + cos(2 * pi * diffmarch1 / Lambda1))
        x = x * 1.E+3
        y = x

        self.figB = plt.figure(figsize=(7, 5))
        custom_map = custom_div_cmap(
            100, mincol='k', midcol='darkblue', maxcol='blue')
        plt.imshow(I_B, cmap=custom_map, interpolation='bilinear', origin='lower', vmin=0,
                   vmax=1, extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.xlabel(r'$X (mm)$', fontsize=10)
        plt.ylabel(r'$Y (mm)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figGreen(self):
        global angle, ndx, Lambda1, Lambda2, Lambda3
        global Xmin, Xmax, cbPhi
        N = 200
        x = linspace(Xmin, Xmax, N)
        y = x
        X, Y = meshgrid(x, y)

        diffmarch2 = 2 * ndx * tan(angle) * X + cbPhi * Lambda2 / 2.
        I_G = 0.5 * (1 + cos(2 * pi * diffmarch2 / Lambda2))
        x = x * 1.E+3
        y = x

        self.figG = plt.figure(figsize=(7, 5))
        custom_map = custom_div_cmap(
            50, mincol='k',  midcol='darkgreen', maxcol=(0, 1, 0))
        plt.imshow(I_G, cmap=custom_map, interpolation='bilinear', origin='lower', vmin=0,
                   vmax=1, extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.xlabel(r'$X (mm)$', fontsize=10)
        plt.ylabel(r'$Y (mm)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figRed(self):
        global angle, ndx, Lambda1, Lambda2, Lambda3
        global Xmin, Xmax, cbPhi
        N = 200
        x = linspace(Xmin, Xmax, N)
        y = x
        X, Y = meshgrid(x, y)

        diffmarch3 = 2 * ndx * tan(angle) * X + cbPhi * Lambda3 / 2.
        I_R = 0.5 * (1 + cos(2 * pi * diffmarch3 / Lambda3))
        x = x * 1.E+3
        y = x

        self.figR = plt.figure(figsize=(7, 5))
        custom_map = custom_div_cmap(
            50, mincol='k', midcol='darkred', maxcol='red')
        plt.imshow(I_R, cmap=custom_map, interpolation='bilinear', origin='lower', vmin=0,
                   vmax=1, extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.xlabel(r'$X (mm)$', fontsize=10)
        plt.ylabel(r'$Y (mm)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figWight(self):
        global angle, ndx, Lambda1, Lambda2, Lambda3
        global Xmin, Xmax, cbPhi
        N = 800
        x = linspace(Xmin, Xmax, N)
        y = x
        X, Y = meshgrid(x, y)

        diffmarch1 = 2 * ndx * tan(angle) * X + cbPhi * Lambda1 / 2.
        I_B = 0.5 * (1 + cos(2 * pi * diffmarch1 / Lambda1))
        diffmarch2 = 2 * ndx * tan(angle) * X + cbPhi * Lambda2 / 2.
        I_G = 0.5 * (1 + cos(2 * pi * diffmarch2 / Lambda2))
        diffmarch3 = 2 * ndx * tan(angle) * X + cbPhi * Lambda3 / 2.
        I_R = 0.5 * (1 + cos(2 * pi * diffmarch3 / Lambda3))
        x = x * 1.E+3
        y = x

        self.figW = plt.figure(figsize=(5, 5))
        custom_mapB = custom_div_cmap(
            200, mincol='k', midcol='blue', maxcol='blue')
        custom_mapG = custom_div_cmap(
            200, mincol='k', midcol='green', maxcol='green')
        custom_mapR = custom_div_cmap(
            200, mincol='k', midcol='red', maxcol='red')
        plt.imshow(I_R, cmap=custom_mapR, interpolation='bilinear', alpha=.4, vmin=0.5,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.imshow(I_B, cmap=custom_mapB, interpolation='bilinear', alpha=.4, vmin=0.5,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.imshow(I_G, cmap=custom_mapG, interpolation='bilinear', alpha=.4, vmin=0.5,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.xlabel(r'$X (mm)$', fontsize=10)
        plt.ylabel(r'$Y (mm)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    @pyqtSlot("double")
    def on_SpinBox_Lambda1_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Lambda2_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_Lambda3_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_angle_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_ndx_valueChanged(self, value):
        self.fig1()

    @pyqtSlot()
    def on_pushButton_Lambda1_clicked(self):
        self.figBlue()
        plt.show(self.figB)

    @pyqtSlot()
    def on_pushButton_Lambda2_clicked(self):
        self.figGreen()
        plt.show(self.figG)

    @pyqtSlot()
    def on_pushButton_Lambda3_clicked(self):
        self.figRed()
        plt.show(self.figR)

    @pyqtSlot()
    def on_pushButton_Lambda123_clicked(self):
        self.figWight()
        plt.show(self.figW)

    @pyqtSlot()
    def on_cbr_clicked(self):
        self.fig1()

    @pyqtSlot()
    def on_cbg_clicked(self):
        self.fig1()

    @pyqtSlot()
    def on_cbb_clicked(self):
        self.fig1()

    @pyqtSlot()
    def on_cbPhi_clicked(self):
        self.fig1()
        self.figBlue()
        self.figGreen()
        self.figRed()
        self.figWight()
        plt.close(self.figW)
        plt.close(self.figR)
        plt.close(self.figB)
        plt.close(self.figG)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = PrismaticSlab()
    MainWindow.show()
    sys.exit(app.exec_())
