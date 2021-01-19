# Imports - standard modules
import sys

# Import matplotlib and set it to use Qt5Agg for plotting
import matplotlib as mpl
mpl.use("Qt5Agg")

# Import QtCore QtWidgets from PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Import functions from scipy library for scientific simulation
from numpy import pi, linspace, sin, cos, tan, arcsin, arccos, arctan, array, dot

# Import matplotlib backends
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from matplotlib.figure import Figure

# Import pyplot from matplotlib for plotting
from matplotlib import pyplot as plt

def getAngles(EOne, ETwo, delta):
   # Calculate the three parameters for the elliptical polarization
   # Auxillary angle: alpha
   # tan(alpha) = Ey/Ex
   #    Ex = EOne cos(omega t); Let t= 0; therefore 
   #    Ex = EOne
   #    Ey = ETwo cos(omega t + delta)
   #    Ey = ETwo cos(delta)
   alpha = arctan(ETwo*cos(delta)/EOne)
   alphaDeg = alpha*180.0/pi
   
   # gamma: Angle of rotation
   # tan(2 gamma) = tan(2 alpha)*cos(delta)
   gamma = 1.0/2.0*arctan( tan(2*alpha)*cos(delta))
   gammaDeg = gamma*180.0/pi

   # Ellipticity angle: chi
   # sin(2 chi) = sin(2 alpha)* sin(delta)
   chi = 1.0/2.0*arcsin( sin(2*alpha) * sin(delta) )
   chiDeg = chi*180./pi

   # Return the rotation, auxillary and ellipticity angles in that order
   return gammaDeg, alphaDeg, chiDeg

# Create an class derived from the FigureCanvas class. This is the canvas on which the sinewaves will be plotted
class MplCanvas(FC):
   def __init__(self, parent=None, width=8, height=6.5, EOne=2.5, ETwo=1, delta=pi/2):
      fig = Figure(figsize=(width, height))
      self.ax = fig.add_subplot(111)
      
      # Clear the axes every time the plot is called
      #self.ax.hold(False)

      # Set the figure to the canvas
      FC.__init__(self, fig)
      
      # Set some standard figure policies
      FC.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
      FC.updateGeometry(self)
      
      # Draw the plot
      self.drawPlot(EOne, ETwo, delta)


   def drawPlot(self, EOne, ETwo, delta):
      self.ax.clear()      # important ！！！！这句话避免了保留之前绘制的东西 (源代码中这句没写！)

      r = ETwo/EOne

      # We will generate the points on the ellipse manually
      N=1024
      theta = linspace(0,2*pi,N)

      # Get the Cartesian coordinates of the ellipse for these theta values
      x = cos(theta)
      y = r*cos(theta+delta)

      # self.ax.plot(T[0],T[1],'r')
      self.ax.plot(x,y,'k')
      self.ax.set_ylim(-EOne-0.5,EOne+0.5)
      self.ax.set_xticklabels([])
      self.ax.set_yticklabels([])
      self.draw()

# Define the mainwindow class
class MainApp(QMainWindow):
   def __init__ (self):
      """ Constructor or the initializer """
      QMainWindow.__init__ (self)
   
      # Set some default attributes of the window
      self.setAttribute(Qt.WA_DeleteOnClose)
      self.setWindowTitle("Elliptical Polarization")
      
      # define the main widget as self
      self.main_widget = QWidget(self)

      # Add the label widgets and sliders
      # x-Component Amplitude
      self.loEOne = QVBoxLayout()
      self.lblEOne = QLabel("x-Component: E1", self)
      self.sldEOne = QSlider(Qt.Horizontal)
      self.sldEOne.setMinimum(2)
      self.sldEOne.setMaximum(50)
      self.sldEOne.setValue(25)
      self.sldEOne.setTickPosition(QSlider.TicksBelow)
      self.sldEOne.setTickInterval(1)
      self.edtEOne = QLineEdit(self)
      self.edtEOne.setMaxLength(5)
      self.loEOne.addWidget(self.lblEOne)
      self.loEOne.addSpacing(3)
      self.loEOne.addWidget(self.sldEOne)
      self.loEOne.addSpacing(3)
      self.loEOne.addWidget(self.edtEOne)
      
      # Add the label widgets and sliders
      # y-Component Amplitude
      self.loETwo = QVBoxLayout()
      self.lblETwo = QLabel("y-Component: E2", self)
      self.sldETwo = QSlider(Qt.Horizontal)
      self.sldETwo.setMinimum(2)
      self.sldETwo.setMaximum(25)
      self.sldETwo.setValue(12)
      self.sldETwo.setTickPosition(QSlider.TicksBelow)
      self.sldETwo.setTickInterval(1)
      self.edtETwo = QLineEdit(self)
      self.edtETwo.setMaxLength(5)
      self.loETwo.addWidget(self.lblETwo)
      self.loETwo.addSpacing(3)
      self.loETwo.addWidget(self.sldETwo)
      self.loETwo.addSpacing(3)
      self.loETwo.addWidget(self.edtETwo)

      # Phase difference - all absorbed in y-component
      self.loPhase = QVBoxLayout()
      self.lblPhase = QLabel("Phase difference: delta (pi rad)", self)
      self.sldPhase = QSlider(Qt.Horizontal)
      self.sldPhase.setMinimum(0)
      self.sldPhase.setMaximum(20*pi*100)    ########3
      self.sldPhase.setValue(10)
      self.sldPhase.setTickPosition(QSlider.TicksBelow)
      self.sldPhase.setTickInterval(1)
      self.edtPhase = QLineEdit(self)
      self.edtPhase.setMaxLength(5)
      self.loPhase.addWidget(self.lblPhase)
      self.loPhase.addSpacing(3)
      self.loPhase.addWidget(self.sldPhase)
      self.loPhase.addSpacing(3)
      self.loPhase.addWidget(self.edtPhase)
      
      # Waves Param Layout
      self.loWaveParams = QHBoxLayout()
      self.loWaveParams.addLayout(self.loEOne)
      self.loWaveParams.addStretch()
      self.loWaveParams.addLayout(self.loETwo)
      self.loWaveParams.addStretch()
      self.loWaveParams.addLayout(self.loPhase)
      
      # Get the values from the sliders 
      EOne = self.sldEOne.value()/10
      ETwo = self.sldETwo.value()/10
      delta = self.sldPhase.value()/(100*pi) - 10.0
      self.edtEOne.setText(str(EOne))
      self.edtETwo.setText(str(ETwo))
      self.edtPhase.setText(str(delta))

      # Get the rotation, auxillary, and ellipticity angles
      gammaDeg, alphaDeg, chiDeg = getAngles(EOne, ETwo, delta)

      # Create an instance of the FigureCanvas
      self.loCanvas = MplCanvas(self.main_widget, width=5, height=4, EOne=EOne, ETwo=ETwo, delta=delta)

      # Auxillary Angle
      self.loAuxAngle = QHBoxLayout()
      self.lblAuxAngle = QLabel("Auxillary Angle: (deg)", self)
      self.lblAuxAngleVal = QLabel(str("%5.2f" %(alphaDeg)), self)
      self.loAuxAngle.addWidget(self.lblAuxAngle)
      self.loAuxAngle.addSpacing(3)
      self.loAuxAngle.addWidget(self.lblAuxAngleVal)

      # Rotation Angle
      self.loRotAngle = QHBoxLayout()
      self.lblRotAngle = QLabel("Rotation Angle: (deg)", self)
      self.lblRotAngleVal = QLabel(str("%5.2f" %(gammaDeg)), self)
      self.loRotAngle.addWidget(self.lblRotAngle)
      self.loRotAngle.addSpacing(3)
      self.loRotAngle.addWidget(self.lblRotAngleVal)

      # Ellipticity Angle
      self.loEllAngle = QHBoxLayout()
      self.lblEllAngle = QLabel("Ellipticity Angle: (deg)", self)
      self.lblEllAngleVal = QLabel(str("%5.2f" %(chiDeg)), self)
      self.loEllAngle.addWidget(self.lblEllAngle)
      self.loEllAngle.addSpacing(3)
      self.loEllAngle.addWidget(self.lblEllAngleVal)
      
      # Set the focus to the main_widget and set it to be central widget
      self.main_widget.setFocus()
      self.setCentralWidget(self.main_widget)
      
      # Populate the master layout
      self.loMaster = QVBoxLayout(self.main_widget)
      self.loMaster.addLayout(self.loWaveParams)
      self.loMaster.addWidget(self.loCanvas)
      self.loMaster.addLayout(self.loRotAngle)
      self.loMaster.addLayout(self.loAuxAngle)
      self.loMaster.addLayout(self.loEllAngle)
      
      # Connect slots
      self.sldEOne.valueChanged.connect(self.OnEOneChanged)
      self.sldETwo.valueChanged.connect(self.OnETwoChanged)
      self.sldPhase.valueChanged.connect(self.OnPhaseChanged)
      self.edtEOne.editingFinished.connect(self.OnEdtEOneChanged)
      self.edtETwo.editingFinished.connect(self.OnEdtETwoChanged)
      self.edtPhase.editingFinished.connect(self.OnEdtPhaseChanged)
   
   def OnEOneChanged(self):
      EOne = self.sldEOne.value()/10
      self.edtEOne.setText(str(EOne))
      self.sldETwo.setMaximum(EOne*10-1) #####
      self.OnSomethingChanged()
   
   def OnETwoChanged(self):
      ETwo = self.sldETwo.value()/10
      self.edtETwo.setText(str(ETwo))
      self.OnSomethingChanged()
   
   def OnPhaseChanged(self):
      delta = self.sldPhase.value()/(100*pi) - 10.0
      self.edtPhase.setText(str(delta))
      self.OnSomethingChanged()

   def OnEdtEOneChanged(self):
      EOne = self.edtEOne.text()
      self.sldEOne.setValue(float(EOne)*10)
      
   def OnEdtETwoChanged(self):
      ETwo = self.edtETwo.text()
      self.sldETwo.setValue(float(ETwo)*10) ########
      
   def OnEdtPhaseChanged(self):
      delta = self.edtPhase.text()
      self.sldPhase.setValue((float(delta)+10.0)*pi*100.0) #######

   def OnSomethingChanged(self):

      EOne = self.sldEOne.value()/10
      ETwo = self.sldETwo.value()/10
      delta = self.sldPhase.value()/100
      # Get the rotation, auxillary, and ellipticity angles
      gammaDeg, alphaDeg, chiDeg = getAngles(EOne, ETwo, delta)
      self.lblRotAngleVal.setText(str("%.2f" %(gammaDeg)))
      self.lblAuxAngleVal.setText(str("%.2f" %(alphaDeg)))
      self.lblEllAngleVal.setText(str("%.2f" %(chiDeg)))

      self.loCanvas.drawPlot(EOne,ETwo,delta)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   MyApp = MainApp()
   MyApp.show()
   app.exec()
