# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

import numpy as np
from Ui_FresnelMirror import Ui_MainWindow
from numpy import pi, linspace, sin, cos
import matplotlib
import matplotlib.pyplot as plt


def fig2():
    global Lambda_R,Lambda_P,a,D,Angle

    Dvirt = D+a
    Champ = D*Angle
    speed = 2.99792458E+8
    freq_i = speed/Lambda_R
    freq_s = speed/Lambda_P
    interval_freq= (freq_s - freq_i)/speed
    freq_moy = (freq_s+freq_i)/speed/2

    X_Mmax=D*Angle ; X_Mmin = -D*Angle
    N =5000
    X=linspace(X_Mmin, X_Mmax,N) # coordinates of screen
    delta=[0 for x in range(len(X))]
    Intens=[0 for x in range(len(X))]
    for xi in range(len(X)):
        delta[xi] = 2*Angle*a*X[xi]/Dvirt
        A = pi*delta[xi]*interval_freq 
        B = 2*pi*delta[xi]*freq_moy
        Intens[xi] = 0.5*(1 + sin(A)/A*cos(B))

    fig_numbers = [x.num for x in matplotlib._pylab_helpers.Gcf.get_all_fig_managers()] 

    if 1 in fig_numbers: 
        print ("figure 1 exists") 
        plt.close(1)
    if 2 in fig_numbers: 
        print ("figure 2 exists") 
        plt.close(2)

    figure_1 = plt.figure(figsize=(6,3))
    plt.plot(X*1E3,Intens,'-r', linewidth=1)
    plt.xlabel(r'$X (mm)$',fontsize=12, fontweight='bold', labelpad=-6)
    plt.ylabel(r'$I (u.a.)$',fontsize=12, fontweight='bold')
    plt.plot([-0.311, -0.311], [0, 1], 'k:', lw=1)
    plt.plot([0.311, 0.311], [0, 1], 'k:', lw=1)

    plt.annotate(r"Visibility",xy=(-0.311, 0.1),xytext=(-1., 0.1),
                 fontsize=10,fontweight='bold',)
    plt.annotate(r"White of higher order",xy=(-0.311, 0.1),xytext=(0.4, 0.65),
                 fontsize=10,fontweight='bold',)
    plt.annotate(r" ", xy=(-0.33, 0.1), xytext=(0.35, 0.1),
                 arrowprops=dict(arrowstyle='<->',edgecolor='k'))
    plt.xlim(-1.5, 1.5)    #Zoom

    figure_2 = plt.figure(figsize=(6,3))
    plt.plot(X*1E3,np.asarray(np.abs(delta))*1.E6,'-r', linewidth=1)
    plt.xlabel(r'$X (mm)$',fontsize=12, fontweight='bold', labelpad=-6)
    plt.ylabel(r'$\delta (\mu m)$',fontsize=12, fontweight='bold')
    plt.ylim(0, 2.5)
    plt.plot([-0.311, -0.311], [0, 1.244], 'k:', lw=1)
    plt.plot([0.311, 0.311], [0, 1.244], 'k:', lw=1)
    plt.plot([-6, 6], [1.244, 1.244], 'k:', lw=1)
    plt.annotate(r"$L_{c}$",xy=(5, 1.25),xytext=(5, 1.25),fontsize=16,fontweight='bold',
                 bbox=dict(boxstyle="round", lw=2, alpha=0.5))
    plt.annotate(r"$\delta < L_{c}$",xy=(4.5, 0.5),xytext=(4.5, 0.5),fontsize=12)
    plt.annotate(r"$\delta < L_{c}$",xy=(4.5, 2),xytext=(4.5, 2),fontsize=12)
    plt.annotate(r"$0.311$",xy=(0.4, 0.),xytext=(0.4, -0.1),fontsize=10,fontweight='bold')
    plt.annotate(r"$-0.311$",xy=(-1.5, 0.),xytext=(-1.5, -0.1),fontsize=10,fontweight='bold')
    plt.annotate(r"Visibility",xy=(-0.311, 0.15),xytext=(-2.5, 0.15),
                 fontsize=10,fontweight='bold',)
    plt.annotate(r" ", xy=(-0.4, 0.15), xytext=(0.4, 0.15),
                 arrowprops=dict(arrowstyle='<->',edgecolor='k'))

    plt.show()


class FresnelMirror(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):

        super(FresnelMirror, self).__init__(parent)
        self.setupUi(self)
        self.fig1()

    def onpick(event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        points = tuple(zip(xdata[ind], ydata[ind]))
        print('onpick points:', points)    
        
    def fig1(self):
        global Lambda_R,Lambda_P,a,D,Angle
        Lambda_R=self.SpinBox_LambdaR.value()*1.E-9 #wavelength of light in vaccuum
        Lambda_O=self.SpinBox_LambdaO.value()*1.E-9 #wavelength of light in vaccuum
        Lambda_Y=self.SpinBox_LambdaY.value()*1.E-9 #wavelength of light in vaccuum
        Lambda_G=self.SpinBox_LambdaG.value()*1.E-9 #wavelength of light in vaccuum
        Lambda_B=self.SpinBox_LambdaB.value()*1.E-9 #wavelength of light in vaccuum
        Lambda_P=self.SpinBox_LambdaP.value()*1.E-9 #wavelength of light in vaccuum
        a=self.SpinBox_a.value()*1.E-3  # distance of the source from the Mirrors
        D= self.SpinBox_D.value()       # Distance screen
        Angle = self.SpinBox_Angle.value()*1.E-3 # Angles

        Dvirt = D+a
        Champ = D*Angle

        X_Mmax=Champ*(1+0.1) ; X_Mmin = -Champ*(1+0.1)
        Y_Mmax=X_Mmax ; Y_Mmin =  X_Mmin
        N =5000
        X=linspace(X_Mmin, X_Mmax,N) # coordinates of screen
        I_R=[0 for x in range(len(X))]
        I_O=[0 for x in range(len(X))]
        I_Y=[0 for x in range(len(X))]
        I_G=[0 for x in range(len(X))]
        I_B=[0 for x in range(len(X))]
        I_P=[0 for x in range(len(X))]
        delta=[0 for x in range(len(X))]
        Intens=[0 for x in range(len(X))]
        for xi in range(len(X)):
#            delta[xi] = 2*Angle*a*X[xi]/Dvirt
            I_R[xi] = 0.5*(1 + cos(4*pi*Angle*a*X[xi]/Lambda_R/Dvirt))
            I_O[xi] = 0.5*(1 + cos(4*pi*Angle*a*X[xi]/Lambda_O/Dvirt))
            I_Y[xi] = 0.5*(1 + cos(4*pi*Angle*a*X[xi]/Lambda_Y/Dvirt))
            I_G[xi] = 0.5*(1 + cos(4*pi*Angle*a*X[xi]/Lambda_G/Dvirt))
            I_B[xi] = 0.5*(1 + cos(4*pi*Angle*a*X[xi]/Lambda_B/Dvirt))
            I_P[xi] = 0.5*(1 + cos(4*pi*Angle*a*X[xi]/Lambda_P/Dvirt))
            
        # figure 1 D - For the color look at the color table in hexadecimal (#ff0000)
        mpl1d=self.mplwidget.canvas
        mpl1d.ax.clear()
        l1,l2,l3,l4,l5,l6=mpl1d.ax.plot(X*1E3,I_R,'#ff0000', X*1E3,I_O,'#ffa31a',X*1E3,I_Y,'#ffff00',X*1E3,I_G,'#00cc00',X*1E3,I_B,'#0000ff',X*1E3,I_P,'#9933ff',linewidth=1)
        mpl1d.ax.set_xlim(-1.2, 1.2)
        mpl1d.ax.set_ylim(0, 1.015)
        mpl1d.ax.set_xlabel(r'$X (mm)$',fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X)$',fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Fresnel Mirror',fontsize=16, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ Angle = %3.2f \ mrad, \ a = %4.1f \ mm, \ D = %3.2f \ m$"% (Lambda_R,Angle*1E3,a*1E3,  D),fontsize=14)
        mpl1d.draw()


    @pyqtSlot("double")
    def on_SpinBox_LambdaR_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_LambdaO_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_LambdaY_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_LambdaG_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_LambdaB_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_LambdaP_valueChanged(self, value):
        self.fig1()
    @pyqtSlot("double")
    def on_SpinBox_Angle_valueChanged(self, value):
        self.fig1()  
        fig2()
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
    fig2()
    sys.exit(app.exec_())

