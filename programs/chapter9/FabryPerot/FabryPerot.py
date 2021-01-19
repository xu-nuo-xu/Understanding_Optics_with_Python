# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_FabryPerot import Ui_MainWindow
from numpy import pi, cos, sin, linspace, meshgrid, tan, arctan, sqrt
import matplotlib.pyplot as plt
from custom_color import custom_div_cmap

from matplotlib.ticker import FormatStrFormatter


class FabryPerot(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(FabryPerot, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        # −−−−−−−−−−−−−−−−−−− Inputs and Intensity −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
        global R, A, T, e, DeltaFixe, Theta1, Lambda1, Lambda2, Lambda3, Distance_Screen
        R = self.SpinBox_nr.value()           # Reflection factor (R)
        A = self.SpinBox_na.value()           # Absorption factor (A)
        e = self. SpinBox_e.value() * 1.E-6   # Plates distance (e)
        DeltaFixe = 2 * self.SpinBox_nt.value() * e
        Theta1 = self.SpinBox_angle.value()  # Angle of incidence
        Lambda1 = self.SpinBox_Lambda1.value() * 1.E-9  # 3 wavelengths
        Lambda2 = self.SpinBox_Lambda2.value() * 1.E-9  # depicting the
        Lambda3 = self.SpinBox_Lambda3.value() * 1.E-9  # RGB color
        Distance_Screen = 1  # Screen distance (m)

        A0 = 1
        Theta0 = 0
        T = 1 - R - A
        Imax = (A0 * T / (1 - R))**2
        M = 4 * R / (1 - R)**2
        N = 5000
        Theta = linspace(Theta0, Theta1, N)
        Delta = DeltaFixe * cos(Theta)
        Order1 = Delta / Lambda1
        phi_B = 2 * pi * Order1
        I_B = Imax / (1 + M * (sin(0.5 * phi_B))**2)
        Order2 = Delta / Lambda2
        phi_G = 2 * pi * Order2
        I_G = Imax / (1 + M * (sin(0.5 * phi_G))**2)
        Order3 = Delta / Lambda3
        phi_R = 2 * pi * Order3
        I_R = Imax / (1 + M * (sin(0.5 * phi_R))**2)

        Epsilon = 5.E-4         # Graph with wavenumber abscissa
        LambdaMin = (1 - Epsilon) * Lambda3
        LambdaMax = (1 + Epsilon) * Lambda1
        Sigma1 = 1 / Lambda1
        Sigma2 = 1 / Lambda2
        Sigma3 = 1 / Lambda3
        SigmaMax = 1 / LambdaMin
        SigmaMin = 1 / LambdaMax
        step = (SigmaMax - SigmaMin) / N
        Sigma = linspace(SigmaMin, SigmaMax, N)
        phi_int = 2 * pi * DeltaFixe * Sigma
        Intens = Imax / (1 + M * (sin(0.5 * phi_int))**2)
        X1, X2, X3 = [], [], []
        for i in range(N):
            if Sigma[i] <= Sigma1 < Sigma[i] + step:
                x1 = i
                X1.append(x1)
            if Sigma[i] <= Sigma2 < Sigma[i] + step:
                x2 = i
                X2.append(x2)
            if Sigma[i] <= Sigma3 < Sigma[i] + step:
                x3 = i
                X3.append(x3)

    # −−−−−−−−−−−−−−−−−−− Graph THETA −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
        mpl1d = self.mplwidget1.canvas
        mpl1d.ax.clear()
        if self.cbr.isChecked() == True:
            mpl1d.ax.plot(Theta, I_R, linestyle='-', color='r', linewidth=1)
        else:
            mpl1d.ax.plot([], [])
        if self.cbb.isChecked() == True:
            mpl1d.ax.plot(Theta, I_B, linestyle='-', color='b', linewidth=1)
        else:
            mpl1d.ax.plot([], [])
        if self.cbg.isChecked() == True:
            mpl1d.ax.plot(Theta, I_G, linestyle='-', color='g', linewidth=1)
        else:
            mpl1d.ax.plot([], [])

        mpl1d.ax.set_xlim(min(Theta), max(Theta))
        mpl1d.ax.set_ylim(0, 1.02)
        mpl1d.ax.set_xlabel(r'$\theta (rad)$', fontsize=14, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(\theta)$', fontsize=14, fontweight='bold')

        mpl1d.figure.tight_layout(pad=1.2, h_pad=None, w_pad=None, rect=None)
        mpl1d.draw()

    # −−−−−−−−−−−−−−−−−−− Graph ORDER −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
        mpl1d = self.mplwidget2.canvas
        mpl1d.ax.clear()
        mpl1d.ax.set_xticks([])
        mpl1d.ax.set_yticks([])
        ax1 = mpl1d.figure.add_subplot(3, 1, 1)
        ax2 = mpl1d.figure.add_subplot(3, 1, 2)
        ax3 = mpl1d.figure.add_subplot(3, 1, 3)
        ax1.clear()
        ax2.clear()
        ax3.clear()
        if self.cbb.isChecked() == True:
            ax1.plot(Order1, I_B, linestyle='-', color='b', linewidth=1)
        else:
            ax1.plot([], [])
        if self.cbg.isChecked() == True:
            ax2.plot(Order2, I_G, linestyle='-', color='g', linewidth=1)
        else:
            ax2.plot([], [])
        if self.cbr.isChecked() == True:
            ax3.plot(Order3, I_R, linestyle='-', color='r', linewidth=1)
        else:
            ax3.plot([], [])

        ax1.set_xlim(min(Order1), max(Order1))

        ax1.set_yticklabels(linspace(0, 1, 6), size=8)
        ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax1.tick_params(which='major', labelsize=10)

        ax2.set_xlim(min(Order2), max(Order2))
        ax2.set_yticklabels(linspace(0, 1, 6), size=8)
        ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax2.tick_params(which='major', labelsize=10)

        ax3.set_xlim(min(Order3), max(Order3))
        ax3.set_yticklabels(linspace(0, 1, 6), size=8)
        ax3.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax3.tick_params(which='major', labelsize=10)

        ax3.set_xlabel(r'$(Order)$', fontsize=14, fontweight='bold')
        ax3.set_ylabel(r'$I(Order)$', fontsize=14, fontweight='bold')

        ax3.annotate(r'$\Delta p=0.0335$', xy=(1999.05, 0.56),
                     xytext=(1999.05, .56), fontsize=12)
        ax3.annotate('', xy=(1998.98, 0.5), xytext=(1998.9, .5),
                     fontsize=10, color='k', arrowprops=dict(arrowstyle="->",))
        ax3.annotate('', xy=(1999.02, 0.5), xytext=(1999.1, .5),
                     fontsize=10, color='k', arrowprops=dict(arrowstyle="->",))
        mpl1d.figure.tight_layout(
            pad=1.1, h_pad=None, w_pad=None, rect=[0, 0, 0.95, 1])
        mpl1d.draw()

    # −−−−−−−−−−−−−−−−−−− Graph PHASE −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
        mpl1d = self.mplwidget3.canvas
        mpl1d.ax.clear()
        mpl1d.ax.set_xticks([])
        mpl1d.ax.set_yticks([])
        ax1 = mpl1d.figure.add_subplot(3, 1, 1)
        ax2 = mpl1d.figure.add_subplot(3, 1, 2)
        ax3 = mpl1d.figure.add_subplot(3, 1, 3)
        ax1.clear()
        ax2.clear()
        ax3.clear()
        if self.cbb.isChecked() == True:
            ax1.plot(phi_B, I_B, linestyle='-', color='b', linewidth=1)
        else:
            ax1.plot([], [])
        if self.cbg.isChecked() == True:
            ax2.plot(phi_G, I_G, linestyle='-', color='g', linewidth=1)
        else:
            ax2.plot([], [])
        if self.cbr.isChecked() == True:
            ax3.plot(phi_R, I_R, linestyle='-', color='r', linewidth=1)
        else:
            ax3.plot([], [])

        ax1.set_xlim(min(phi_B), max(phi_B))
        ax1.set_yticklabels(linspace(0, 1, 6), size=8)
        ax1.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax1.tick_params(which='major', labelsize=10)

        ax2.set_xlim(min(phi_G), max(phi_G))
        ax2.set_yticklabels(linspace(0, 1, 6), size=8)
        ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax2.tick_params(which='major', labelsize=10)

        ax3.set_xlim(min(phi_R), max(phi_R))
        ax3.set_yticklabels(linspace(0, 1, 6), size=8)
        ax3.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax3.tick_params(which='major', labelsize=10)
        ax3.set_xlabel(r'$(Phase)$', fontsize=14, fontweight='bold')
        ax3.set_ylabel(r'$I(Phase)$', fontsize=14, fontweight='bold')
        mpl1d.figure.tight_layout(pad=1, h_pad=None, w_pad=None, rect=None)
        mpl1d.draw()

    # −−−−−−−−−−−−−−−−−−− Graph WAVENEMBER−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
        mpl1d = self.mplwidget4.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(Sigma, Intens, linestyle='-', color='r', linewidth=1)
        mpl1d.ax.set_xlim(min(Sigma), max(Sigma))
        mpl1d.ax.set_ylim(0, 1.1)
        mpl1d.ax.set_xlabel(
            r'$\sigma (cm^{-1})$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(\sigma)$', fontsize=12, fontweight='bold')
        mpl1d.figure.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)
        mpl1d.draw()

    def figBlue(self):
        global R, A, T, e, DeltaFixe, Theta1, Lambda1, Lambda2, Lambda3, Distance_Screen
        A0 = 1
        T = 1 - R - A
        Theta0 = -Theta1
        Imax = (A0 * T / (1 - R))**2
        M = 4 * R / (1 - R)**2
        N = 1000
        angle = linspace(Theta0, Theta1, N)
        x = Distance_Screen * tan(angle)
        y = x
        X, Y = meshgrid(x, y)
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        phase = 2 * pi * DeltaFixe * cos(angle_i) / Lambda1
        I_B = Imax / (1 + M * (sin(0.5 * phase))**2)
        self.figB = plt.figure(figsize=(7, 5))
        custom_map = custom_div_cmap(
            200, mincol='k', midcol='blue', maxcol='#413FFF')
        plt.imshow(I_B, cmap=custom_map, interpolation='bilinear',
                   origin='lower', extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.colorbar().ax.tick_params(labelsize=8)
        plt.xlabel(r'$X (m)$', fontsize=10)
        plt.ylabel(r'$Y (m)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figGreen(self):
        global R, A, T, e, DeltaFixe, Theta1, Lambda1, Lambda2, Lambda3, Distance_Screen
        A0 = 1
        Theta0 = -Theta1
        T = 1 - R - A
        Imax = (A0 * T / (1 - R))**2
        M = 4 * R / (1 - R)**2
        N = 1000
        angle = linspace(Theta0, Theta1, N)
        x = Distance_Screen * tan(angle)
        y = x
        X, Y = meshgrid(x, y)
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        phase = 2 * pi * DeltaFixe * cos(angle_i) / Lambda2
        I_G = Imax / (1 + M * (sin(0.5 * phase))**2)

        self.figG = plt.figure(figsize=(7, 5))
        custom_map = custom_div_cmap(
            200, mincol='k', midcol='green', maxcol='#00EF20')
        plt.imshow(I_G, cmap=custom_map, interpolation='bilinear',
                   origin='lower', extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.colorbar().ax.tick_params(labelsize=8)
        plt.xlabel(r'$X (m)$', fontsize=10)
        plt.ylabel(r'$Y (m)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figRed(self):
        global R, A, T, e, DeltaFixe, Theta1, Lambda1, Lambda2, Lambda3, Distance_Screen
        A0 = 1
        Theta0 = -Theta1
        T = 1 - R - A
        Imax = (A0 * T / (1 - R))**2
        M = 4 * R / (1 - R)**2
        N = 1000
        angle = linspace(Theta0, Theta1, N)
        x = Distance_Screen * tan(angle)
        y = x
        X, Y = meshgrid(x, y)
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        phase = 2 * pi * DeltaFixe * cos(angle_i) / Lambda3
        I_R = Imax / (1 + M * (sin(0.5 * phase))**2)

        self.figR = plt.figure(figsize=(7, 5))
        custom_map = custom_div_cmap(
            200, mincol='k', midcol='red', maxcol='#FF3E2F')
        plt.imshow(I_R, cmap=custom_map, interpolation='bilinear',
                   origin='lower', extent=[min(x), max(x), min(y), max(y)])
        plt.tick_params(axis='both', labelsize=8)
        plt.colorbar().ax.tick_params(labelsize=8)
        plt.xlabel(r'$X (m)$', fontsize=10)
        plt.ylabel(r'$Y (m)$', fontsize=10)
        plt.tight_layout(pad=1.5, h_pad=None, w_pad=None, rect=None)

    def figWight(self):
        global R, A, T, e, DeltaFixe, Theta1, Lambda1, Lambda2, Lambda3, Distance_Screen
        A0 = 1
        T = 1 - R - A
        Theta0 = -Theta1
        Distance_Screen = 1  # Distance from the screen (m)
        Imax = (A0 * T / (1 - R))**2
        M = 4 * R / (1 - R)**2
        N = 1000
        angle = linspace(Theta0, Theta1, N)
        x = Distance_Screen * tan(angle)
        y = x
        X, Y = meshgrid(x, y)
        angle_i = arctan(sqrt(X**2 + Y**2) / Distance_Screen)
        phase_B = 2 * pi * DeltaFixe * cos(angle_i) / Lambda1
        I_B = Imax / (1 + M * (sin(0.5 * phase_B))**2)
        phase_G = 2 * pi * DeltaFixe * cos(angle_i) / Lambda2
        I_G = Imax / (1 + M * (sin(0.5 * phase_G))**2)
        phase_R = 2 * pi * DeltaFixe * cos(angle_i) / Lambda3
        I_R = Imax / (1 + M * (sin(0.5 * phase_R))**2)

        self.figW = plt.figure(figsize=(5, 5))
        custom_mapB = custom_div_cmap(
            200, mincol='k', midcol='blue', maxcol='#5F7BFF')
        custom_mapG = custom_div_cmap(
            200, mincol='k', midcol='green', maxcol='#00EF20')
        custom_mapR = custom_div_cmap(
            200, mincol='k', midcol='red', maxcol='#FF2F37')
        plt.imshow(I_R, cmap=custom_mapR, interpolation='bilinear', alpha=.4, vmin=0.,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.imshow(I_B, cmap=custom_mapB, interpolation='bilinear', alpha=.4, vmin=0.,
                   vmax=1., extent=[min(x), max(x), min(y), max(y)])
        plt.imshow(I_G, cmap=custom_mapG, interpolation='bilinear', alpha=.4, vmin=0.,
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
    def on_SpinBox_angle_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_e_valueChanged(self, value):
        self.Slider_e.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_Slider_e_valueChanged(self, value):
        self.SpinBox_e.setValue(value)
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_nr_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_na_valueChanged(self, value):
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_nt_valueChanged(self, value):
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
    MainWindow = FabryPerot()
    MainWindow.show()
    sys.exit(app.exec_())
