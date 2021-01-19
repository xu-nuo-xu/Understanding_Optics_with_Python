# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from Ui_DoubleSlit2D import Ui_MainWindow
from numpy import pi, linspace, sin, cos, meshgrid
import matplotlib.cm as cm


class DoubleSlit2D(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        #-------------------- Input parameters ----------------------------------------
        lamda = self.slider_lambda.value() * 1.E-9
        k = (2. * pi) / lamda  # wavelength of light in vaccuum

        b = self.slider_b.value() * 1.E-6  # dimensions of diffracting slit (m)
        #b is along (Ox)
        db = self.slider_db.value() * 1.E-6
        b1 = b
        b2 = b + db
        d = self.slider_d.value() * 1.E-6
        f_2 = self.slider_f2.value()     # f2 is the focal length of the lens L2 (m)
        a = self.slider_a.value() * 1.E-2  # Side of a square-shaped screen (m)
        X_Mmax = a / 2.
        X_Mmin = -a / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 400
        X = linspace(X_Mmin, X_Mmax, N)
        Y = X  # coordinates of screen
        # 2D & 3 D representation
        XX, YY = meshgrid(X, Y)
        B = (k * b * XX) / (2. * f_2 * pi)
        A = (k * (b + d) * XX) / (2. * f_2)
        D = (k * db * XX) / (2. * f_2)  # intermediate variable
        I = 1 / 2. * ((sin(B) / B)**2 *
                      ((cos(A + D / 2.)**2 + (cos(A + D)**2))))
        # 这个公式应当是从公式(11.5)带入双缝数据化简而来的
        # 因为 2D 图牵扯meshgrid，因此不能用 1D 作图中numpy带的
        # 虚数处理方法：real, imag, 1j
        # 但具体怎么推的目前不是很清晰
        # 公式展开形式见 formula.jpg
        # 如果双缝一样宽，则(11.5)可推出(11.6)，比上面 I 的形式简便得多

#-------------------- Graphs --------------------------------------------------
        mpl2d = self.mplwidget2D.canvas
        mpl2d.ax.clear()
        mpl2d.ax.imshow(I, cmap=cm.gray, interpolation='bilinear',
                        origin='lower', vmin=0, vmax=.2)
        mpl2d.ax.set_xlabel(u'$X (m)$', fontsize=12, fontweight='bold')
        mpl2d.ax.set_ylabel(u'$Y (m)$', fontsize=12, fontweight='bold')
        mpl2d.ax.set_xticks(linspace(0, N, 5))
        mpl2d.ax.set_xticklabels(linspace(X_Mmin, X_Mmax, 5),  color='r')
        mpl2d.ax.set_yticks(linspace(0, N, 5))
        mpl2d.ax.set_yticklabels(linspace(Y_Mmin, Y_Mmax, 5),  color='r')
        mpl2d.figure.suptitle(
            'Fraunhofer Diffraction of double slits', fontsize=14, fontweight='bold')
        mpl2d.ax.set_title(r"$\lambda = %.3e \ m, \ b1 = %.2e \ m, \ b2 = %.2e \ m, \ d = %.2e \ m, \ f_2 = %.1f \ m$" % (
            lamda, b1, b2, d, f_2), fontsize=10)
        mpl2d.draw()

    @pyqtSlot("int")
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_b_valueChanged(self, value):
        self.SpinBox_b.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_db_valueChanged(self, value):
        self.SpinBox_db.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_d_valueChanged(self, value):
        self.SpinBox_d.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_f2_valueChanged(self, value):
        self.SpinBox_f2.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_SpinBox_lambda_valueChanged(self, value):
        self.slider_lambda.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_b_valueChanged(self, value):
        self.slider_b.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_db_valueChanged(self, value):
        self.slider_db.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_d_valueChanged(self, value):
        self.slider_d.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.slider_a.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):
        self.slider_f2.setValue(value)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = DoubleSlit2D()
    MyApplication.show()
    sys.exit(app.exec_())
