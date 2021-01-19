# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_ParallelFaces import Ui_MainWindow
import numpy as np
from numpy import pi, cos, sin, arcsin, linspace, meshgrid, tan, arctan, sqrt
import matplotlib.pyplot as plt
from custom_color import custom_div_cmap


class ParallelFaces(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(ParallelFaces, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        #---------------- Input Parameters and Intensity ---------------------------------------
        global thick, ndx, Lambda1, Lambda2, Lambda3, Distance_Screen
        global Xmin, Xmax, cbPhi
        # Parallel faces distance or plate
        thick = self.SpinBox_e.value() * 1.E-6
        ndx = self.SpinBox_ndx.value()               # thickness (e) of (n) index
        Lambda1 = self.SpinBox_Lambda1.value() * 1.E-9  # The 3 wavelengths
        Lambda2 = self.SpinBox_Lambda2.value() * 1.E-9  # representing the
        Lambda3 = self.SpinBox_Lambda3.value() * 1.E-9  # RGB color
        Distance_Screen = 1.                        # Screen distance fixed to 1m
        Xmin = -3E-1                                # Interval of variation for the
        Xmax = -Xmin                                # angle (radian)
        N = 5000
        xi = linspace(Xmin, Xmax, N)
        x = Distance_Screen * np.tan(xi)
        angle_refract = np.arcsin(np.sin(xi) / ndx)   # Refracted angle (r)
        if self.cbPhi.isChecked() == True:          # Relflection shift (pi) 半波损失
            cbPhi = 1
        else:
            cbPhi = 0
        diffmarch1 = 2. * ndx * thick * \
            np.cos(angle_refract) + cbPhi * Lambda1 / 2.  # OPD 1
        I_B = 0.5 * (1. + np.cos(2. * pi * diffmarch1 / Lambda1))  # I(OPD1)    #这个表达式前系数应当是 2 不是 0.5，见P225 I 的公式
        diffmarch2 = 2. * ndx * thick * \
            np.cos(angle_refract) + cbPhi * Lambda2 / 2.  # OPD 2                或者说让I0 =0.25 了
        I_G = 0.5 * (1. + np.cos(2. * pi * diffmarch2 / Lambda2))  # I(OPD2)
        diffmarch3 = 2. * ndx * thick * \
            np.cos(angle_refract) + cbPhi * Lambda3 / 2.  # OPD 3
        I_R = 0.5 * (1. + np.cos(2. * pi * diffmarch3 / Lambda3))  # I(OPD3)
        x = x * 1.E3

        #---------------- Figure 1 D --------------------------------------------------
        mpl1d = self.mplwidget.canvas
        mpl1d.ax.clear()

        if self.cbr.isChecked() == True:
            mpl1d.ax.plot(x, I_R, linestyle='-', color='r', linewidth=1)
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

        mpl1d.ax.set_ylim(0, 1.01)
        mpl1d.ax.set_xlim(min(x), max(x))
        mpl1d.ax.set_xlabel(r'$r (rad)$', fontsize=12, fontweight='bold')   # 我觉得 x 轴应当是距离入射点的横向距离(单位：mm)
        mpl1d.ax.set_ylabel(r'$I(\theta)$', fontsize=12, fontweight='bold') # 可参考 line 35 x 的表达式
        mpl1d.figure.suptitle('Parallel Faces', fontsize=14, fontweight='bold')
        mpl1d.draw()

    def figBlue(self):
        global thick, ndx, Lambda1, Lambda2, Lambda3, Distance_Screen
        global Xmin, Xmax, cbPhi

        N = 400
        xi = linspace(Xmin, Xmax, N)
        yi = xi
#        X,Y=meshgrid(xi,yi)
        x = Distance_Screen * tan(xi)
        y = x
        X, Y = meshgrid(x, y)
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        angle_refract = arcsin(sin(angle_i) / ndx)

        diffmarch1 = 2 * ndx * thick * \
            cos(angle_refract) + cbPhi * Lambda1 / 2.
        I_B = 0.5 * (1 + cos(2 * pi * diffmarch1 / Lambda1))
        self.figB = plt.figure(figsize=(7, 5))
        self.figB.canvas.set_window_title('ParallelFaces: Blue light')
        custom_map = custom_div_cmap(
            50, mincol='k', midcol='darkblue', maxcol='blue')
        plt.imshow(I_B, cmap=custom_map, interpolation='bilinear',
                   origin='lower', vmin=0, vmax=1, extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.colorbar().ax.tick_params(labelsize=8)
        plt.xlabel(r'$X (m)$', fontsize=10)
        plt.ylabel(r'$Y (m)$', fontsize=10)
#        plt.tight_layout(rect=(0.,0.04,1,1))
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figGreen(self):
        global ndx, Lambda1, Lambda2, Lambda3, Distance_Screen
        global Xmin, Xmax, cbPhi
        N = 400
        xi = linspace(Xmin, Xmax, N)
        yi = xi
        x = Distance_Screen * tan(xi)
        y = x
        X, Y = meshgrid(x, y)
        # Dependence of angles
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        # in X and Y (2D)
        angle_refract = arcsin(sin(angle_i) / ndx)
        diffmarch2 = 2 * ndx * thick * \
            cos(angle_refract) + cbPhi * Lambda2 / 2.  # Associated OPD
        I_G = 0.5 * (1 + cos(2 * pi * diffmarch2 / Lambda2))
        self.figG = plt.figure(figsize=(7, 5))
        self.figG.canvas.set_window_title('ParallelFaces: Green light')
        custom_map = custom_div_cmap(
            50, mincol='#000000', midcol='#00b300', maxcol=(0, 1, 0))
        plt.imshow(I_G, cmap=custom_map, interpolation='bilinear',
                   origin='lower', vmin=0, vmax=1, extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.colorbar().ax.tick_params(labelsize=8)
        plt.xlabel(r'$X (m)$', fontsize=10)
        plt.ylabel(r'$Y (m)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figRed(self):
        global thick, ndx, Lambda1, Lambda2, Lambda3, Distance_Screen
        global Xmin, Xmax, cbPhi

        N = 400
        xi = linspace(Xmin, Xmax, N)
        yi = xi
        x = Distance_Screen * tan(xi)
        y = x
        X, Y = meshgrid(x, y)
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        angle_refract = arcsin(sin(angle_i) / ndx)

        diffmarch3 = 2 * ndx * thick * \
            cos(angle_refract) + cbPhi * Lambda3 / 2.
        I_R = 0.5 * (1 + cos(2 * pi * diffmarch3 / Lambda3))
        self.figR = plt.figure(figsize=(7, 5))
        self.figR.canvas.set_window_title('ParallelFaces: Red light')
        custom_map = custom_div_cmap(
            50, mincol='k', midcol='darkred', maxcol=(1, 0, 0))
        plt.imshow(I_R, cmap=custom_map, interpolation='bilinear',
                   origin='lower', vmin=0, vmax=1, extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.colorbar().ax.tick_params(labelsize=8)
        plt.xlabel(r'$X (m)$', fontsize=10)
        plt.ylabel(r'$Y (m)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figWight(self):
        global thick, ndx, Lambda1, Lambda2, Lambda3, Distance_Screen
        global Xmin, Xmax, cbPhi

        N = 1000
        xi = linspace(Xmin, Xmax, N)
        yi = xi
        x = Distance_Screen * tan(xi)
        y = x
        X, Y = meshgrid(x, y)
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        angle_refract = arcsin(sin(angle_i) / ndx)

        diffmarch1 = 2 * ndx * thick * \
            cos(angle_refract) + cbPhi * Lambda1 / 2.
        I_B = 0.5 * (1 + cos(2 * pi * diffmarch1 / Lambda1))
        diffmarch2 = 2 * ndx * thick * \
            cos(angle_refract) + cbPhi * Lambda2 / 2.
        I_G = 0.5 * (1 + cos(2 * pi * diffmarch2 / Lambda2))
        diffmarch3 = 2 * ndx * thick * \
            cos(angle_refract) + cbPhi * Lambda3 / 2.
        I_R = 0.5 * (1 + cos(2 * pi * diffmarch3 / Lambda3))

        self.figW = plt.figure(figsize=(5, 5))
        self.figW.canvas.set_window_title('ParallelFaces: Wight light')
        custom_mapB = custom_div_cmap(
            200, mincol='k', midcol='blue', maxcol='blue')
        custom_mapG = custom_div_cmap(
            200, mincol='k', midcol='green', maxcol='green')
        custom_mapR = custom_div_cmap(
            200, mincol='k', midcol='red', maxcol='red')
        plt.imshow(I_R, cmap=custom_mapR, interpolation='bilinear', alpha=.4, vmin=.0,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.imshow(I_B, cmap=custom_mapB, interpolation='bilinear', alpha=.4, vmin=.0,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.imshow(I_G, cmap=custom_mapG, interpolation='bilinear', alpha=.4, vmin=.0,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.xlabel(r'$X (m)$', fontsize=10)
        plt.ylabel(r'$Y (m)$', fontsize=10)
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
    def on_SpinBox_e_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_ndx_valueChanged(self, value):
        self.fig1()

    @pyqtSlot()
    def on_pushButton_Lambda1_clicked(self):
        self.figBlue()
        # Set the absolute position of the figure on the screen:
        # plt.get_current_fig_manager().window.setGeometry(<x-pos>,<y-pos>,<width>,<height>)
        plt.get_current_fig_manager().window.setGeometry(100, 100, 800, 800)    # 已经得到当前的plt对象
        #plt.show(self.figB) # 报错 show() takes 1 positional arguments but 2 were given。show()不用传self参数
        plt.show()
    @pyqtSlot()
    def on_pushButton_Lambda2_clicked(self):
        self.figGreen()
        plt.get_current_fig_manager().window.setGeometry(100, 100, 800, 800)
        #plt.show(self.figG)
        plt.show()
    @pyqtSlot()
    def on_pushButton_Lambda3_clicked(self):
        self.figRed()
        plt.get_current_fig_manager().window.setGeometry(100, 100, 800, 800)
        #plt.show(self.figR)
        plt.show()
    @pyqtSlot()
    def on_pushButton_Lambda123_clicked(self):
        self.figWight()
        plt.get_current_fig_manager().window.setGeometry(100, 100, 800, 800)
        #plt.show(self.figW)
        plt.show()
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
    MainWindow = ParallelFaces()
    MainWindow.show()
    sys.exit(app.exec_())
