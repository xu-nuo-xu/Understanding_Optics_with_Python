# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib.cm as cm
import sys
from Ui_DoubleSlit1D import Ui_MainWindow
from numpy import pi, linspace, sin, exp, real, imag


class DoubleSlit1D(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()

    def fig1(self):
        lamda = self.slider_lambda.value() * 1.E-9
        k = (2. * pi) / lamda  # Wavelength
        # Slits width, b is along (Ox)
        b = self.SpinBox_b.value() * 1.E-6
        db = self.slider_db.value() * 1.E-6
        b1 = b
        b2 = b + db
        b_moy = (b1 + b2) / 2
        a = self.SpinBox_a.value() * 1.E-2    # Edge-Slits distance
        # f2=D Lens focal-length(m)
        D = self.slider_D.value()
        # Square-shaped screen (m)
        sx = self.slider_sx.value() * 1.E-3
        # Central maximum width (Ox)
        dx = 1.E2 * (2 * lamda * D) / b
        self.Central_Spot.setText(str("%.4f" % dx))
        # Central maximum width (Oy)
        dy = 1.E2 * (lamda * D) / (a + b_moy)
        self.Internal_Spot.setText(str("%.4f" % dy))
        # X_Mmax = sx / 2.
        # X_Mmin = -sx / 2.
        X_Mmax = sx / 2.
        X_Mmin = -sx / 2.
        Y_Mmax = X_Mmax
        Y_Mmin = X_Mmin
        N = 800
        # Coordinates of screen
        X = linspace(X_Mmin, X_Mmax, N)
        v1 = k * (a + b1) * X / (2 * D)
        v2 = k * b1 * X / (2 * D)
        v3 = k * (a + b2) * X / (2 * D)
        v4 = k * b2 * X / (2 * D)
        Amplitude = exp(1j * v1) * sin(v2) / v2
        Amplitude1 = real(Amplitude)**2
        Amplitude2 = imag(Amplitude)**2
        envelop = Amplitude1 + Amplitude2
        Amplitude = b1 * exp(1j * v1) * sin(v2) / v2 + \
            b2 * exp(-1j * v3) * sin(v4) / v4           # p301 公式(11.5) 沿着 x 轴方向的强度分布
        Amplitude1 = real(Amplitude)**2
        Amplitude2 = imag(Amplitude)**2
        # b_moy Fctor of normalisation
        I = (Amplitude1 + Amplitude2) / 4 / b_moy**2    # 归一化

# ------------------ Figure 1 D ------------------
        mpl1d = self.mplwidget1D.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(X, I, '-r', X, envelop, ":b", linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin, X_Mmax)
        mpl1d.ax.set_xlabel(r'$X (m)$', fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X,Y)/I_0$', fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle(
            'Fraunhofer Double Slits Diffraction', fontsize=14, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ b1 = %.2e \ m, \ b2 = %.2e \ m, \ a = %.2e \ m, \ D = %.1f \ m$" % (
            lamda, b1, b2, a, D), fontsize=10)
        mpl1d.draw()

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
    def on_slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_sx_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_slider_D_valueChanged(self, value):
        self.SpinBox_D.setValue(value)
        self.fig1()

    @pyqtSlot("int")
    def on_SpinBox_lambda_valueChanged(self, value):
        self.slider_lambda.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_b_valueChanged(self, value):
        self.slider_b.setValue(value)
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_db_valueChanged(self, value):
        self.slider_db.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.slider_a.setValue(value)
        self.fig1()

    @pyqtSlot("double")
    def on_SpinBox_sx_valueChanged(self, value):
        self.slider_sx.setValue(value)

    @pyqtSlot("double")
    def on_SpinBox_D_valueChanged(self, value):
        self.slider_D.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = DoubleSlit1D()
    MyApplication.show()
    sys.exit(app.exec_())
