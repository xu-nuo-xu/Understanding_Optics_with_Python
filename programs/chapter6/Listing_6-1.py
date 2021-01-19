# Imports - standard modules
import sys

# Import matplotlib and set it to use Qt5Agg for plotting
import matplotlib as mpl
mpl.use("Qt5Agg")

# Import QtCore, QtWidgets from PytQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Import functions from scipy library for scientific simulation
from numpy import pi, linspace, meshgrid, sin, arcsin, cos, tan, arctan2, sqrt, array

# Import matplotlib backends
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from matplotlib.figure import Figure

# Import pyplot, lines and patches from matplotlib
from matplotlib import pyplot as plt
from matplotlib import lines as mlines
from matplotlib import patches as mpatches

# Create an class derived from the FigureCanvas class. This is the canvas on which the diagrams will be drawn


class MplCanvas(FC):
    def __init__(self, parent=None, width=5, height=5, nOne=1.0, nTwo=1.5, rad=30, objDist=50, objHt=5):
        """Note that the radius and object distances should be given in centimeters while the object height in millimeters."""
        fig = Figure(figsize=(width, height))
        self.ax = fig.add_subplot(111, aspect='equal')

        # Clear the axes every time the plot is called
        # self.ax.hold(False)

        # Set the figure to the canvas
        FC.__init__(self, fig)

        # Set some standard figure policies
        FC.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FC.updateGeometry(self)

        # Draw the plot
        self.drawPlot(nOne, nTwo, rad, objDist, objHt)

    def yCoordLine(self, xOne, xTwo, yOne, yTwo, x):
        slope = (yTwo - yOne) / (xTwo - xOne)
        return slope * (x - xOne) + yOne

    def drawPlot(self, nOne, nTwo, rad, objDist, objHt):
        self.ax.clear()

        # Calculate the power, the image distance and image height
        power = (nTwo - nOne) / (rad / 100.0)       # P
        if not power == 0:
            fOne = -nOne / power * 100.0
            fTwo = nTwo / power * 100
        else:
            fOne = -1e10
            fTwo = 1e10
        objVerg = -nOne / (objDist / 100)   # L
        imgVerg = objVerg + power           # L'
        if not imgVerg == 0:
            imgDist = nTwo / (imgVerg) * 100  # value in cm     # l'
            mag = objVerg / imgVerg                         # m
            imgHt = mag * objHt  # It is in the same unit as the object height
        else:
            imgDist = mag = imgHt = 1e10

        # We will use the following scaling for drawing
        # Matplotlib uses inches as native units of measurement for size.
        # So, we need to convert our cm values to inches.
        cm2inch = 1.0 / 2.54

        rad1 = cm2inch * rad
        l = -cm2inch * objDist
        lp = cm2inch * imgDist  # l'
        h = cm2inch * objHt
        hp = cm2inch * imgHt
        f = cm2inch * fOne
        fp = cm2inch * fTwo

        # The canvas
        x = cm2inch * linspace(-200, 400, 1024)
        y = cm2inch * linspace(-100, 100, 1024)
        X, Y = meshgrid(x, y)

        # Draw the optic axis
        optAx = mlines.Line2D([0.95 * x[0], 0.95 * x[-1]], [0, 0], color='k')
        self.ax.add_line(optAx)

        # Draw the surface
        sfc = mpatches.Arc([rad1, 0], 2 * rad1, 2 * rad1,
                           angle=0, theta1=90, theta2=270, color='k')   # 椭圆
        self.ax.add_patch(sfc)

        # We will be using the standard ray diagram principles to identify the image positions.

        # Draw the object.
        self.ax.arrow(l, 0, 0, h, length_includes_head=True,
                      head_width=0.5, color='k', shape='full')
        self.ax.text(l - 7, 0.35 * h, 'h')

        # Draw the incident ray from the object tip - parallel to optic axis
        sag = rad1 - sqrt(rad1**2 - h**2)
        iR1 = mlines.Line2D([l, sag], [h, h], color='k')
        self.ax.add_line(iR1)
        self.ax.arrow(l / 2, h, 2, 0, length_includes_head=True,
                      head_width=1, color='k', shape='full')

        # This ray will pass through the secondary focal point. We want to extend the ray beyond the secondary focal point to beyond the image
        endPtX = 1.4 * lp
        endPtY = self.yCoordLine(sag, fp, h, 0, endPtX)
        rR1 = mlines.Line2D([sag, endPtX], [h, endPtY], color='k')
        self.ax.add_line(rR1)
        arBaseX = (endPtX - sag) / 2
        arBaseY = self.yCoordLine(sag, fp, h, 0, arBaseX)
        dX = 1
        dY = h / (sag - fp)
        self.ax.arrow(arBaseX, arBaseY, dX, dY, length_includes_head=True,
                      head_width=1, color='k', shape='full')

        # The second ray; this ray passes through the primary focal point and emerges parallel to the optic axis
        iR2Slope = (h - 0) / (l - f)
        iR2Intercept = iR2Slope * (-l) + h
        if abs(iR2Intercept) < rad1:
            iR2EndPtY = iR2Intercept
            rR2 = mlines.Line2D(
                [0, 1.4 * lp], [iR2Intercept, iR2Intercept], color='r')
            self.ax.add_line(rR2)
        else:
            iR2EndPtY = iR2Slope * rad1 + iR2Intercept
        iR2 = mlines.Line2D([l, 0], [h, iR2EndPtY], color='r')
        self.ax.add_line(iR2)

        # The third ray that passes through the center of curvature of the lens
        iR3Slope = (h - 0) / (l - rad1)
        iR3Intercept = iR3Slope * (-l) + h
        iR3EndPtX = 1.4 * lp
        iR3EndPtY = iR3Slope * iR3EndPtX + iR3Intercept
        iR3 = mlines.Line2D([l, iR3EndPtX], [h, iR3EndPtY], color='b')
        self.ax.add_line(iR3)

        # Draw the image
        self.ax.arrow(lp, 0, 0, hp, length_includes_head=True,
                      head_width=1, color='k', shape='full')
        self.ax.text(1.025 * lp, 0.5 * hp, 'h\'')

        # Mark the various distances
        irV = mlines.Line2D([0, 0], [0, 0.95 * y[0]], color='k', ls='dashed')
        self.ax.add_line(irV)
        self.ax.arrow(0, -rad1 - 5, f, 0, length_includes_head=True,
                      head_width=1, color='k', shape='full')
        self.ax.text(0.5 * f, -rad1 - 10, 'f')

        self.ax.arrow(0, -rad1 - 20, l, 0, length_includes_head=True,
                      head_width=1, color='k', shape='full')
        self.ax.text(0.5 * l, -rad1 - 25, 'l')

        self.ax.arrow(0, -rad1 + 2.5, rad1, 0, length_includes_head=True,
                      head_width=1, color='k', shape='full')
        self.ax.text(0.5 * rad1, -rad1 + 2.5, 'r')

        self.ax.arrow(0, -rad1 - 12.5, fp, 0, length_includes_head=True,
                      head_width=1, color='k', shape='full')
        self.ax.text(0.5 * fp, -rad1 - 12, 'f\'')

        self.ax.arrow(0, -rad1 - 26.5, lp, 0, length_includes_head=True,
                      head_width=1, color='k', shape='full')
        self.ax.text(0.5 * lp, -rad1 - 26, 'l\'')

        self.ax.set_xlim(x[0], x[-1])
        self.ax.set_ylim(y[0], y[-1])
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])

        self.ax.text(0.75 * x[0], 0.35 * y[-1], str('n1 = %.2f' % (nOne)))
        self.ax.text(0.75 * x[-1], 0.35 * y[-1], str('n2 = %.2f' % (nTwo)))

        self.draw()


# Define the mainwindow class
class MainApp(QMainWindow):
    def __init__(self):
        """ Constructor or the initializer """
        QMainWindow.__init__(self)

        # Set some default attributes of the window
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Refraction")

        # define the main widget as self
        self.main_widget = QWidget(self)

        # Add the label widgets and sliders
        # Refractive Index - Object Side
        self.loRIOne = QVBoxLayout()        # Vertical layout
        self.lblRIOne = QLabel("Refractive Index: n1", self)
        self.sldRIOne = QSlider(Qt.Horizontal)
        self.sldRIOne.setMinimum(100)
        self.sldRIOne.setMaximum(150)
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

        # Refractive Index - Image Side
        self.loRITwo = QVBoxLayout()    # Vertical layout
        self.lblRITwo = QLabel("Refractive Index: n2", self)
        self.sldRITwo = QSlider(Qt.Horizontal)
        self.sldRITwo.setMinimum(100)
        self.sldRITwo.setMaximum(180)
        self.sldRITwo.setValue(150)
        self.sldRITwo.setTickPosition(QSlider.TicksBelow)
        self.sldRITwo.setTickInterval(10)
        self.edtRITwo = QLineEdit(self)
        self.edtRITwo.setMaxLength(5)
        self.loRITwo.addWidget(self.lblRITwo)
        self.loRITwo.addSpacing(3)
        self.loRITwo.addWidget(self.sldRITwo)
        self.loRITwo.addSpacing(3)
        self.loRITwo.addWidget(self.edtRITwo)

        # Radius of curvature
        self.loRad = QVBoxLayout()      # Vertical layout
        self.lblRad = QLabel("Radius of curvature (cm)", self)
        self.sldRad = QSlider(Qt.Horizontal)
        self.sldRad.setMinimum(10)
        self.sldRad.setMaximum(25)
        self.sldRad.setValue(250)
        self.sldRad.setTickPosition(QSlider.TicksBelow)
        self.sldRad.setTickInterval(5)
        self.edtRad = QLineEdit(self)
        self.edtRad.setMaxLength(8)
        self.loRad.addWidget(self.lblRad)
        self.loRad.addSpacing(3)
        self.loRad.addWidget(self.sldRad)
        self.loRad.addSpacing(3)
        self.loRad.addWidget(self.edtRad)

        # Object Distance
        self.loObjDist = QVBoxLayout()      # Vertical layout
        self.lblObjDist = QLabel("Object Distance (cm)", self)
        self.sldObjDist = QSlider(Qt.Horizontal)
        self.sldObjDist.setMinimum(10)
        self.sldObjDist.setMaximum(2000)
        self.sldObjDist.setValue(1250)
        self.sldObjDist.setTickPosition(QSlider.TicksBelow)
        self.sldObjDist.setTickInterval(10)
        self.edtObjDist = QLineEdit(self)
        self.edtObjDist.setMaxLength(8)
        self.loObjDist.addWidget(self.lblObjDist)
        self.loObjDist.addSpacing(3)
        self.loObjDist.addWidget(self.sldObjDist)
        self.loObjDist.addSpacing(3)
        self.loObjDist.addWidget(self.edtObjDist)

        # Object Height
        self.loObjHt = QVBoxLayout()        # Vertical layout
        self.lblObjHt = QLabel("Object Height (cm)", self)
        self.sldObjHt = QSlider(Qt.Horizontal)
        self.sldObjHt.setMinimum(1)
        self.sldObjHt.setMaximum(99)
        self.sldObjHt.setValue(50)
        self.sldObjHt.setTickPosition(QSlider.TicksBelow)
        self.sldObjHt.setTickInterval(10)
        self.edtObjHt = QLineEdit(self)
        self.edtObjHt.setMaxLength(8)
        self.loObjHt.addWidget(self.lblObjHt)
        self.loObjHt.addSpacing(3)
        self.loObjHt.addWidget(self.sldObjHt)
        self.loObjHt.addSpacing(3)
        self.loObjHt.addWidget(self.edtObjHt)

        # Surf Params Layout
        self.loSurfParams = QHBoxLayout()       # Horizontal layout
        self.loSurfParams.addLayout(self.loRIOne)
        self.loSurfParams.addStretch()
        self.loSurfParams.addLayout(self.loRITwo)
        self.loSurfParams.addStretch()
        self.loSurfParams.addLayout(self.loRad)

        # Object/Image Params Layout
        self.loObjParams = QHBoxLayout()        # Horizontal layout
        self.loObjParams.addLayout(self.loObjDist)
        self.loObjParams.addStretch()
        self.loObjParams.addLayout(self.loObjHt)
        self.loObjParams.addStretch()

        # Get the values from the sliders
        nOne = self.sldRIOne.value() / 100
        self.edtRIOne.setText(str(nOne))
        nTwo = self.sldRITwo.value() / 100
        self.edtRITwo.setText(str(nTwo))
        rad = self.sldRad.value()
        self.edtRad.setText(str(rad))
        objDist = self.sldObjDist.value() / 10
        self.edtObjDist.setText(str(objDist))
        objHt = self.sldObjHt.value() / 10
        self.edtObjHt.setText(str(objHt))

        # Calculate the power, the image distance and image height
        power = (nTwo - nOne) / (rad / 100.0)       # P (formula 6.7)
        fOne = -nOne / power * 100.0                # f (formula 6.9)
        fTwo = nTwo / power * 100
        objVerg = -nOne / (objDist / 100)           # L (below formula 6.5)
        imgVerg = objVerg + power                   # L'(formula 6.6)
        imgDist = nTwo / (imgVerg) * 100  # value in cm # l' (below formula 6.5)
        mag = objVerg / imgVerg                     # m (formula 6.14)
        imgHt = mag * objHt  # It is in the same unit as the object height # image height

        # Create an instance of the FigureCanvas
        self.loCanvas = MplCanvas(self.main_widget, width=5, height=5,
                                  nOne=nOne, nTwo=nTwo, rad=rad, objDist=objDist, objHt=objHt)

        # Power
        self.loPower = QHBoxLayout()
        self.lblPower = QLabel("Power of the surface (D)", self)
        self.lblPowerVal = QLabel(str('%.2f' % (power)))
        self.lblfOne = QLabel("Primary focal length (cm)", self)
        self.lblfOneVal = QLabel(str('%.2f' % (fOne)))
        self.lblfTwo = QLabel("Secondary focal length (cm)", self)
        self.lblfTwoVal = QLabel(str('%.2f' % (fTwo)))
        self.loPower.addWidget(self.lblPower)
        self.loPower.addSpacing(3)
        self.loPower.addWidget(self.lblPowerVal)
        self.loPower.addSpacing(7)
        self.loPower.addWidget(self.lblfOne)
        self.loPower.addSpacing(3)
        self.loPower.addWidget(self.lblfOneVal)
        self.loPower.addSpacing(7)
        self.loPower.addWidget(self.lblfTwo)
        self.loPower.addSpacing(3)
        self.loPower.addWidget(self.lblfTwoVal)

        # Image Properties
        self.loImgParams = QHBoxLayout()
        self.lblImgDist = QLabel("Image Distance (cm)", self)
        self.lblImgDistVal = QLabel(str('%.2f' % (imgDist)))
        self.lblImgHt = QLabel("Image Height (mm)", self)
        self.lblImgHtVal = QLabel(str('%.2f' % (imgHt)))
        self.lblMag = QLabel("Magnification", self)
        self.lblMagVal = QLabel(str('%.2f' % (mag)))
        self.loImgParams.addWidget(self.lblImgDist)
        self.loImgParams.addSpacing(3)
        self.loImgParams.addWidget(self.lblImgDistVal)
        self.loImgParams.addSpacing(7)
        self.loImgParams.addWidget(self.lblImgHt)
        self.loImgParams.addSpacing(3)
        self.loImgParams.addWidget(self.lblImgHtVal)
        self.loImgParams.addSpacing(7)
        self.loImgParams.addWidget(self.lblMag)
        self.loImgParams.addSpacing(3)
        self.loImgParams.addWidget(self.lblMagVal)

        # Set the focus to the main_widget and set it to be central widget
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        # Populate the master layout
        self.loMaster = QVBoxLayout(self.main_widget)
        self.loMaster.addLayout(self.loSurfParams)
        self.loMaster.addLayout(self.loObjParams)
        self.loMaster.addWidget(self.loCanvas)
        self.loMaster.addLayout(self.loPower)
        self.loMaster.addLayout(self.loImgParams)

        # Connect slots
        self.sldRIOne.valueChanged.connect(self.OnRIOneChanged)
        self.edtRIOne.editingFinished.connect(self.OnEdtRIOneChanged)

        self.sldRITwo.valueChanged.connect(self.OnRITwoChanged)
        self.edtRITwo.editingFinished.connect(self.OnEdtRITwoChanged)

        self.sldRad.valueChanged.connect(self.OnRadChanged)
        self.edtRad.editingFinished.connect(self.OnEdtRadChanged)

        self.sldObjDist.valueChanged.connect(self.OnObjDistChanged)
        self.edtObjDist.editingFinished.connect(self.OnEdtObjDistChanged)

        self.sldObjHt.valueChanged.connect(self.OnObjHtChanged)
        self.edtObjHt.editingFinished.connect(self.OnEdtObjHtChanged)

    def OnRIOneChanged(self):
        nOne = self.sldRIOne.value() / 100
        self.edtRIOne.setText(str(nOne))
        self.OnSomethingChanged()

    def OnEdtRIOneChanged(self):
        nOne = self.edtRIOne.text()
        self.sldRIOne.setValue(float(nOne) * 100)

    def OnRITwoChanged(self):
        nTwo = self.sldRITwo.value() / 100
        self.edtRITwo.setText(str(nTwo))
        self.OnSomethingChanged()

    def OnEdtRITwoChanged(self):
        nTwo = self.edtRITwo.text()
        self.sldRITwo.setValue(float(nTwo) * 100)
        self.OnSomethingChanged()

    def OnRadChanged(self):
        rad = self.sldRad.value()
        self.edtRad.setText(str(rad))
        self.OnSomethingChanged()

    def OnEdtRadChanged(self):
        rad = self.edtRad.text()
        self.sldRad.setValue(float(rad))
        self.OnSomethingChanged()

    def OnObjDistChanged(self):
        objDist = self.sldObjDist.value() / 10
        self.edtObjDist.setText(str(objDist))
        self.OnSomethingChanged()

    def OnEdtObjDistChanged(self):
        objDist = self.edtObjDist.text()
        self.sldObjDist.setValue(float(objDist) * 10)
        self.OnSomethingChanged()

    def OnObjHtChanged(self):
        objHt = self.sldObjHt.value() / 10
        self.edtObjHt.setText(str(objHt))
        self.OnSomethingChanged()

    def OnEdtObjHtChanged(self):
        objHt = self.edtObjHt.text()
        self.sldObjHt.setValue(float(objHt) * 10)
        self.OnSomethingChanged()

    def OnSomethingChanged(self):
        nOne = self.sldRIOne.value() / 100
        nTwo = self.sldRITwo.value() / 100
        rad = self.sldRad.value()
        objDist = self.sldObjDist.value() / 10
        objHt = self.sldObjHt.value() / 10

        self.sldRITwo.setMinimum(nOne * 100 + 10)

        # Calculate the power, the image distance and image height
        power = (nTwo - nOne) / (rad / 100.0)
        self.lblPowerVal.setText(str('%.2f' % (power)))
        if not power == 0:
            fOne = -nOne / power * 100.0
            self.lblfOneVal.setText(str('%.2f' % (fOne)))
            fTwo = nTwo / power * 100.0
            self.lblfTwoVal.setText(str('%.2f' % (fTwo)))
            self.sldObjDist.setMinimum((abs(fOne) + 0.1) * 10)
        else:
            fOne = -1e10
            self.lblfOneVal.setText('Infinity')
            fTwo = 1e10
            self.lblfTwoVal.setText('Infinity')

        objVerg = -nOne / (objDist / 100)
        imgVerg = objVerg + power
        if not imgVerg == 0:
            imgDist = nTwo / (imgVerg) * 100  # value in cm
            self.lblImgDistVal.setText('%.2f' % (imgDist))
        else:
            imgDist = 1e10
            self.lblImgDistVal.setText('Infinity')

        if not imgVerg == 0:
            mag = objVerg / imgVerg
            imgHt = mag * objHt  # It is in the same unit as the object height
            self.lblImgHtVal.setText(str('%.2f' % (imgHt)))
            self.lblMagVal.setText(str('%.2f' % (mag)))
        else:
            self.lblImgHtVal.setText('Undefined')
            self.lblMagVal.setText('Undefined')

        self.loCanvas.drawPlot(nOne, nTwo, rad, objDist, objHt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApp = MainApp()
    MyApp.show()
    app.exec()
