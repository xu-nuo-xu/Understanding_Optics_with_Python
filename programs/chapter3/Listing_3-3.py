# Imports - standard modules
import sys

# Import matplotlib and set it to use Qt5Agg for plotting
import matplotlib as mpl
mpl.use("Qt5Agg")

# Import QtCore QtWidgets from PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Import functions from scipy library for scientific simulation
from scipy import pi, linspace, meshgrid, sin

# Import matplotlib backends
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from matplotlib.figure import Figure

# Import pyplot from matplotlib for plotting
from matplotlib import pyplot as plt

# Create a class derived from the FigureCanvas class. This is the canvas on which the sinewaves will be plotted


class MplCanvas(FC):
    def __init__(self, parent=None, width=8, height=6.5, lamda=555, phi=pi / 4, ampl=1):
        fig = Figure(figsize=(width, height))
        self.ax = fig.add_subplot(111)

        # Clear the axes every time the plot is called
        self.ax.hold(False)

        # Set the figure to the canvas
        FC.__init__(self, fig)

        # Set some standard figure policies
        FC.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FC.updateGeometry(self)

        # Draw the plot
        self.drawPlot(lamda, phi, ampl)

    def drawPlot(self, lamda, phi, ampl):
        x = linspace(0, 0.7, 1024)
        y = ampl * sin(2 * pi * x / (lamda / 1000) + phi)
        self.ax.plot(x, y, 'r')
        self.ax.set_ylim(-2, 2)
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.draw()

# Define the mainwindow class


class MainApp(QMainWindow):
    def __init__(self):
        """ Constructor or the initializer """
        QMainWindow.__init__(self)

        # Set some default attributes of the window
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Waves")

        # define the main widget as self
        self.main_widget = QWidget(self)

        # Add the label widgets and sliders
        # Wavelength
        self.loLambda = QVBoxLayout()
        self.lblLambda = QLabel("Wavelength (nm)", self)
        self.sldLambda = QSlider(Qt.Horizontal)
        self.sldLambda.setMinimum(400)
        self.sldLambda.setMaximum(700)
        self.sldLambda.setValue(700)
        self.sldLambda.setTickPosition(QSlider.TicksBelow)
        self.sldLambda.setTickInterval(5)
        self.edtLambda = QLineEdit(self)
        self.edtLambda.setMaxLength(5)
        self.loLambda.addWidget(self.lblLambda)
        self.loLambda.addSpacing(3)
        self.loLambda.addWidget(self.sldLambda)
        self.loLambda.addSpacing(3)
        self.loLambda.addWidget(self.edtLambda)

        # Initial Phase
        self.loPhase = QVBoxLayout()
        self.lblPhase = QLabel("Initial Phase (rad)", self)
        self.sldPhase = QSlider(Qt.Horizontal)
        self.sldPhase.setMinimum(0)
        self.sldPhase.setMaximum(2 * pi * 100)
        self.sldPhase.setValue(0)
        self.sldPhase.setTickPosition(QSlider.TicksBelow)
        self.sldPhase.setTickInterval(1)
        self.edtPhase = QLineEdit(self)
        self.edtPhase.setMaxLength(5)
        self.loPhase.addWidget(self.lblPhase)
        self.loPhase.addSpacing(3)
        self.loPhase.addWidget(self.sldPhase)
        self.loPhase.addSpacing(3)
        self.loPhase.addWidget(self.edtPhase)

        # Amplitude
        self.loAmpl = QVBoxLayout()
        self.lblAmpl = QLabel("Amplitude", self)
        self.sldAmpl = QSlider(Qt.Horizontal)
        self.sldAmpl.setMinimum(10)
        self.sldAmpl.setMaximum(200)
        self.sldAmpl.setValue(100)
        self.sldAmpl.setTickPosition(QSlider.TicksBelow)
        self.sldAmpl.setTickInterval(1)
        self.edtAmpl = QLineEdit(self)
        self.edtAmpl.setMaxLength(5)
        self.loAmpl.addWidget(self.lblAmpl)
        self.loAmpl.addSpacing(3)
        self.loAmpl.addWidget(self.sldAmpl)
        self.loAmpl.addSpacing(3)
        self.loAmpl.addWidget(self.edtAmpl)

        # Waves Param Layout
        self.loWaveParams = QHBoxLayout()
        self.loWaveParams.addLayout(self.loLambda)
        self.loWaveParams.addStretch()
        self.loWaveParams.addLayout(self.loPhase)
        self.loWaveParams.addStretch()
        self.loWaveParams.addLayout(self.loAmpl)

        # Get the values from the sliders
        lamda = self.sldLambda.value()
        phi = self.sldPhase.value() / 100
        ampl = self.sldAmpl.value() / 100
        self.edtLambda.setText(str(lamda))
        self.edtPhase.setText(str(phi))
        self.edtAmpl.setText(str(ampl))

        # Create an instance of the FigureCanvas
        self.loCanvas = MplCanvas(
            self.main_widget, width=5, height=4, lamda=lamda, phi=phi, ampl=ampl)

        # Set the focus to the main_widget and set it to be central widget
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        # Populate the master layout
        self.loMaster = QVBoxLayout(self.main_widget)
        self.loMaster.addLayout(self.loWaveParams)
        self.loMaster.addWidget(self.loCanvas)

        # Connect slots
        self.sldLambda.valueChanged.connect(self.OnLambdaChanged)
        self.sldPhase.valueChanged.connect(self.OnPhaseChanged)
        self.sldAmpl.valueChanged.connect(self.OnAmplChanged)
        self.edtLambda.editingFinished.connect(self.OnEdtLambdaChanged)
        self.edtPhase.editingFinished.connect(self.OnEdtPhaseChanged)
        self.edtAmpl.editingFinished.connect(self.OnEdtAmplChanged)

    def OnLambdaChanged(self):
        lamda = self.sldLambda.value()
        self.edtLambda.setText(str(lamda))
        self.OnSomethingChanged()

    def OnPhaseChanged(self):
        phi = self.sldPhase.value() / 100
        self.edtPhase.setText(str(phi))
        self.OnSomethingChanged()

    def OnAmplChanged(self):
        ampl = self.sldAmpl.value() / 100
        self.edtAmpl.setText(str(ampl))
        self.OnSomethingChanged()

    def OnEdtLambdaChanged(self):
        lamda = int(self.edtLambda.text())
        self.sldLambda.setValue(lamda)

    def OnEdtPhaseChanged(self):
        phi = self.edtPhase.text()
        self.sldPhase.setValue(float(phi) * 100)

    def OnEdtAmplChanged(self):
        ampl = self.edtAmpl.text()
        self.sldAmpl.setValue(float(ampl) * 100)

    def OnSomethingChanged(self):
        lamda = self.sldLambda.value()
        phi = self.sldPhase.value() / 100
        ampl = self.sldAmpl.value() / 100
        self.loCanvas.drawPlot(lamda, phi, ampl)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApp = MainApp()
    MyApp.show()
    app.exec()
