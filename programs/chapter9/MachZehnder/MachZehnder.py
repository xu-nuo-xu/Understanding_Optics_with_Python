# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Ui_MachZehnder import Ui_MainWindow
from numpy import pi,cos,sqrt,tan,arctan


class MachZehnder(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(MachZehnder, self).__init__(parent)
        self.setupUi(self)
        self.fig1()
        
    def fig1(self):
#---------------------- Inputs and Intensity-----------------------------------
        Lambda=self.SpinBox_Lambda.value()*1.E-9   # Wavelength (vaccum)
        ndx=self.SpinBox_ndx.value()               # Refractive index (n)
        WidthBlade=self.SpinBox_WB.value()*1.E-6   # Width blade (e)
        F=self.SpinBox_F.value()                   # Focal length (f)
        DLS=self.SpinBox_DLS.value()*1.E-3         # Lens-1first beam-splitter (d1)
        if self.cbLens.isChecked() == True:        # Choice with or without
            Lens_On_Off=1                          # lens
        else:
            Lens_On_Off=0
        Diametre = 20*1.E-3               # Mirrors & beam-splitter diameter (phi)
        Dscreen = 90*1.E-3                # Screen distance (R)
        Dsource = 60*1.E-3                # Source distance (d)
        Bras_H = 50*1.E-3                 # Horizontal arms (L)
        Bras_V = 40*1.E-3                 # Vertical arms (D)        
        D_Src_Le = DLS + Dsource
        D_S1_S2 = Lens_On_Off*((D_Src_Le)*F/(F-D_Src_Le) - D_Src_Le)
        Cst = Diametre*sqrt(2)/4.
        Gamm = Dscreen+Dsource+Bras_V+Bras_H
        Alpha1 =arctan(Cst/(Dsource+Bras_V+Bras_H + Cst))
        Alpha2 =arctan(Cst/(Dsource+Bras_V+Bras_H - Cst))
        Beta1 =arctan(Cst/(Dsource+Bras_V + Cst))
        Beta2 =arctan(Cst/(Dsource+Bras_V - Cst))
        Lambda1 = Gamm*tan(Alpha1)
        Lambda2 = Gamm*tan(Alpha2)
        LAMBDA = Lambda1 + Lambda2        
        epsilon = D_S1_S2 + (1-1/ndx)*WidthBlade
        Theta1 =arctan(Cst/(Dsource+Bras_V+Bras_H + epsilon + Cst))
        Theta2 =arctan(Cst/(Dsource+Bras_V+Bras_H + epsilon - Cst))    
        Lambda1 = (Gamm+epsilon)*tan(Theta1)
        Lambda2 = (Gamm+epsilon)*tan(Theta2)
        LAMBDA = Lambda1 + Lambda2
        xmin = -Lambda2 - Lambda2/5.
        xmax = Lambda1 + Lambda1/5.
        N=1000
        step= (xmax-xmin)/N
        x,I=[],[]
        for i in range(0,N,1):
            xi= xmin + i*step
            diffmarch = Gamm*epsilon/sqrt(Gamm**2 + xi**2)
            if xi<-Lambda2:
                Intens=0
            elif -Lambda2 <= xi <= Lambda1:
                Intens = 2*(1 + cos(2*pi*(diffmarch/Lambda)))
            elif xi > Lambda1:
                Intens = 0            
            x.append(xi)
            I.append(Intens)


        # −−−−−−−−−−−−−−−−−−−−−− Graph −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
        mpl1d=self.mplwidget.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(x,I,linestyle='-', color='r', linewidth=2)
        
        mpl1d.ax.set_xlim(xmin, xmax)
        mpl1d.ax.set_ylim(min(I), max(I)+.5)
        mpl1d.ax.set_xlabel(r'Position on the screen X(m)',fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'I(X)',fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Mach zehnder',fontsize=14, fontweight='bold')
        mpl1d.draw()
        
    @pyqtSlot("double")
    def on_SpinBox_Lambda_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_ndx_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_F_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_WB_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_DLS_valueChanged(self, value):
        self.fig1()
    @pyqtSlot()
    def on_cbLens_clicked(self):
        self.fig1()       
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MachZehnder()
    MainWindow.show()
    sys.exit(app.exec_())
