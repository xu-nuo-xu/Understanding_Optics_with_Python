# Imports - standard modules
import sys

# Import matplotlib and set it to use Qt5Agg for plotting
import matplotlib as mpl
mpl.use("Qt5Agg")

# Import QtCore and QtWidgets from PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Import functions from scipy library for scientific simulation
from numpy import pi, linspace, meshgrid, sin, arcsin, cos, tan

# Import matplotlib backends
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from matplotlib.figure import Figure
from matplotlib import lines as mlines

# Import pyplot from matplotlib
from matplotlib import pyplot as plt

# Create an class derived from the FigureCanvas class. This is the canvas on which the sinewaves will be plotted


class MplCanvas(FC):
    def __init__(self, parent=None, width=8, height=6.5, nOne=1.0, nTwo=1.52, incAng=30):
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
        self.drawPlot(nOne, nTwo, incAng)

    def drawPlot(self, nOne, nTwo, incAng):
        self.ax.clear()
        # Angle of reflection
        reflAng = incAng
        # Angle of refraction
        refrAng = 180.0 / pi * arcsin(nOne * sin(pi / 180.0 * incAng) / nTwo)

        # The canvas
        #x = linspace(-3.0, 3.0, 1024)
        #y = linspace(-3.0, 3.0, 1024)
        #X, Y = meshgrid(x, y)
        #y = sin(2 * pi * x / (nOne / 1000) + nTwo)

        # Draw the boundary between the two media (draw a line from (0,-3) to (0,3) )
        bdy = mlines.Line2D([0, 0], [-3, 3], color='b')
        self.ax.add_line(bdy)

        # Draw the normal (draw a line from (-2,0) to (2,0) )
        nml = mlines.Line2D([-2, 2], [0, 0], ls='dashed', color='k')
        self.ax.add_line(nml)

        # Draw the incident and reflected ray
        lIncRay = lRefrRay = lReflRay = 2.8             # length of the Ray
        xIncRay = -lIncRay * cos(pi / 180.0 * incAng)   # x coordination of the Incident Ray
        yIncRay = -lIncRay * sin(pi / 180.0 * incAng)   # y coordination of the Incident Ray
        xReflRay = xIncRay                              # x coordination of the Reflect Ray
        yReflRay = -yIncRay                             # y coordination of the Reflect Ray

        incRay = mlines.Line2D([xIncRay, 0], [yIncRay, 0], color='k')
        self.ax.add_line(incRay)
        # Draw the arrow at the middle of the ray
        self.ax.arrow(xIncRay / 2, yIncRay / 2, 0.05, 0.05 * tan(pi / 180.0 * incAng),
                      length_includes_head=True, head_width=0.1, color='k', shape='full')

        reflRay = mlines.Line2D([xReflRay, 0], [yReflRay, 0], color='k')
        self.ax.add_line(reflRay)
        # Draw the arrow at the middle of the ray
        self.ax.arrow(xReflRay / 2, yReflRay / 2, -0.05, 0.05 * tan(pi / 180.0 * reflAng),
                      length_includes_head=True, head_width=0.1, color='k', shape='full')

        # Draw the refracted ray
        if not isinstance(refrAng, complex):
            xRefrRay = lRefrRay * cos(pi / 180.0 * refrAng)                 # x coordination of the Refract Ray
            yRefrRay = lRefrRay * sin(pi / 180.0 * refrAng)                 # y coordination of the Refract Ray
            refrRay = mlines.Line2D([0, xRefrRay], [0, yRefrRay], color='k')
            self.ax.add_line(refrRay)

            # Draw the arrow at the middle of the ray
            self.ax.arrow(xRefrRay / 2, yRefrRay / 2, 0.05, 0.05 * tan(pi / 180.0 * refrAng),
                          length_includes_head=True, head_width=0.1, color='k', shape='full')

        # Set the axes properties
        self.ax.set_ylim(-3, 3)
        self.ax.set_xlim(-3, 3)
        self.ax.set_xticklabels([])     # set tick label as empty
        self.ax.set_yticklabels([])
        self.ax.text(-2.5, 2.5, 'Medium 1')
        self.ax.text(1.0, 2.5, 'Medium 2')

        # Draw the axes
        self.draw()


# Define the mainwindow class
class MainApp(QMainWindow):
    def __init__(self):
        """ Constructor or the initializer """
        QMainWindow.__init__(self)

        # Set some default attributes of the window
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Reflection and Refraction")

        # define the main widget as self
        self.main_widget = QWidget(self)

        # Add the label widgets and sliders
        # Refractive Index - Object Side
        self.loRIOne = QVBoxLayout()
        self.lblRIOne = QLabel("Refractive Index: n1", self)
        self.sldRIOne = QSlider(Qt.Horizontal)
        self.sldRIOne.setMinimum(100)
        self.sldRIOne.setMaximum(200)
        self.sldRIOne.setValue(100)
        self.sldRIOne.setTickPosition(QSlider.TicksBelow)
        self.sldRIOne.setTickInterval(10)
        self.edtRIOne = QLineEdit(self)
        self.edtRIOne.setMaxLength(5)
        self.loRIOne.addWidget(self.lblRIOne)
        self.loRIOne.addSpacing(3)
        self.loRIOne.addWidget(self.sldRIOne)
        self.loRIOne.addSpacing(3)
        self.loRIOne.addWidget(self.edtRIOne)

        # Refractive Index - Object Side
        self.loRITwo = QVBoxLayout()
        self.lblRITwo = QLabel("Refractive Index: n2", self)
        self.sldRITwo = QSlider(Qt.Horizontal)
        self.sldRITwo.setMinimum(100)
        self.sldRITwo.setMaximum(200)
        self.sldRITwo.setValue(152)
        self.sldRITwo.setTickPosition(QSlider.TicksBelow)
        self.sldRITwo.setTickInterval(10)
        self.edtRITwo = QLineEdit(self)
        self.edtRITwo.setMaxLength(5)
        self.loRITwo.addWidget(self.lblRITwo)
        self.loRITwo.addSpacing(3)
        self.loRITwo.addWidget(self.sldRITwo)
        self.loRITwo.addSpacing(3)
        self.loRITwo.addWidget(self.edtRITwo)

        # Angle of incidence
        self.loIncAng = QVBoxLayout()
        self.lblIncAng = QLabel("Angle of Incidence", self)
        self.sldIncAng = QSlider(Qt.Horizontal)
        self.sldIncAng.setMinimum(0)
        self.sldIncAng.setMaximum(90)
        self.sldIncAng.setValue(30)
        self.sldIncAng.setTickPosition(QSlider.TicksBelow)
        self.sldIncAng.setTickInterval(10)
        self.edtIncAng = QLineEdit(self)
        self.edtIncAng.setMaxLength(2)
        self.loIncAng.addWidget(self.lblIncAng)
        self.loIncAng.addSpacing(3)
        self.loIncAng.addWidget(self.sldIncAng)
        self.loIncAng.addSpacing(3)
        self.loIncAng.addWidget(self.edtIncAng)

        # Angle of refraction
        self.loRefrAng = QHBoxLayout()
        self.lblRefrAng = QLabel("Angle of Refraction", self)
        self.edtRefrAng = QLineEdit(self)
        self.loRefrAng.addWidget(self.lblRefrAng)
        self.loRefrAng.addSpacing(3)
        self.loRefrAng.addWidget(self.edtRefrAng)
        refrAng = 180.0 / pi * arcsin(1.0 * sin(pi / 180.0 * 30) / 1.52)
        self.edtRefrAng.setText(str('%5.3f' % (refrAng)))

        # Waves Param Layout
        self.loRayParams = QHBoxLayout()
        self.loRayParams.addLayout(self.loRIOne)
        self.loRayParams.addStretch()
        self.loRayParams.addLayout(self.loRITwo)
        self.loRayParams.addStretch()
        self.loRayParams.addLayout(self.loIncAng)

        # Get the values from the sliders
        nOne = self.sldRIOne.value() / 100
        nTwo = self.sldRITwo.value() / 100
        incAng = self.sldIncAng.value()
        self.edtRIOne.setText(str(nOne))
        self.edtRITwo.setText(str(nTwo))
        self.edtIncAng.setText(str(incAng))

        # Create an instance of the FigureCanvas
        self.loCanvas = MplCanvas(
            self.main_widget, width=5, height=4, nOne=nOne, nTwo=nTwo, incAng=incAng)

        # Set the focus to the main_widget and set it to be central widget
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        # Populate the master layout
        self.loMaster = QVBoxLayout(self.main_widget)
        self.loMaster.addLayout(self.loRayParams)
        self.loMaster.addWidget(self.loCanvas)
        self.loMaster.addLayout(self.loRefrAng)

        # Connect slots
        self.sldRIOne.valueChanged.connect(self.OnRIOneChanged)
        self.sldRITwo.valueChanged.connect(self.OnRITwoChanged)
        self.sldIncAng.valueChanged.connect(self.OnIncAngChanged)
        self.edtRIOne.editingFinished.connect(self.OnEdtRIOneChanged)
        self.edtRITwo.editingFinished.connect(self.OnEdtRITwoChanged)
        self.edtIncAng.editingFinished.connect(self.OnEdtIncAngChanged)

    def OnRIOneChanged(self):
        nOne = self.sldRIOne.value() / 100
        self.edtRIOne.setText(str(nOne))
        self.OnSomethingChanged()

    def OnRITwoChanged(self):
        nTwo = self.sldRITwo.value() / 100
        self.edtRITwo.setText(str(nTwo))
        self.OnSomethingChanged()

    def OnIncAngChanged(self):
        incAng = self.sldIncAng.value()
        self.edtIncAng.setText(str(incAng))
        self.OnSomethingChanged()

    def OnEdtRIOneChanged(self):
        nOne = self.edtRIOne.text()
        self.sldRIOne.setValue(float(nOne) * 100)

    def OnEdtRITwoChanged(self):
        nTwo = self.edtRITwo.text()
        self.sldRITwo.setValue(float(nTwo) * 100)

    def OnEdtIncAngChanged(self):
        incAng = self.edtIncAng.text()
        self.sldIncAng.setValue(float(incAng))

    def OnSomethingChanged(self):
        nOne = self.sldRIOne.value() / 100
        nTwo = self.sldRITwo.value() / 100
        incAng = self.sldIncAng.value()
        refrAng = 180.0 / pi * arcsin(nOne * sin(pi / 180.0 * incAng) / nTwo)
        if isinstance(refrAng, complex):
            self.edtRefrAng.setText('Total Internal Reflection')
        else:
            self.edtRefrAng.setText(str('%5.3f' % (refrAng)))
        self.loCanvas.drawPlot(nOne, nTwo, incAng)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApp = MainApp()
    MyApp.show()
    app.exec()
