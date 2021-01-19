# Imports - standard modules
import sys

# Import matplotlib and set it to use Qt5Agg for plotting
# import matplotlib as mpl
# mpl.use("Qt5Agg")

# Import pyqtSlot to connect sliders and DoubleSpinBox signals
from PyQt5.QtCore import *

# Import PyQt Widgets for PyQt5 version
from PyQt5.QtWidgets import *

# Import functions from scipy library for scientific simulation
from scipy import pi, linspace, meshgrid, sin, exp

# Import matplotlib backends
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from matplotlib.figure import Figure

# Import pyplot from matplotlib
from matplotlib import pyplot as plt

# Define the class for the project


class MainApp(QMainWindow):
    def __init__(self):
        """ Constructor or the initializer """
        QMainWindow.__init__(self)

        # Set some default attributes of the window
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle("Radiometry - Photometry Converter")

        # Set some default values
        self.LumQuant = ['Energy', 'Flux', 'Emittance',
                         'Intensity', 'Luminance', 'Illuminance']
        self.RadUnits = ["Joules (J)", "Watts (W)",
                         "W/m^2", "W/Sr", "W/(m^2.Sr)", "W/m^2"]
        self.PhotUnits = ["Talbot (T)", "Lumens (lm)",
                          "lm/m^2", "Candela (cd)", "cd/m^2", "lux"]

        # define the main widget as self
        self.main_widget = QWidget(self)

        # Add the label widgets and sliders
        # Lighting Condition
        self.loCondition = QHBoxLayout()
        self.lblCondition = QLabel("Condition", self)
        self.cmbCondition = QComboBox()
        self.cmbCondition.addItems(["Photopic", "Scotopic"])
        self.loCondition.addStretch()
        self.loCondition.addWidget(self.lblCondition)
        self.loCondition.addSpacing(3)
        self.loCondition.addWidget(self.cmbCondition)
        self.loCondition.addStretch()

        # Wavelength
        self.loWavelength = QHBoxLayout()
        self.lblWavelength = QLabel("Wavelength (nm)", self)
        self.edtWavelength = QLineEdit(self)
        self.edtWavelength.setMaxLength(3)
        self.edtWavelength.setText("555")
        self.loWavelength.addStretch()
        self.loWavelength.addWidget(self.lblWavelength)
        self.loWavelength.addSpacing(3)
        self.loWavelength.addWidget(self.edtWavelength)
        self.loWavelength.addStretch()

        # Radiometric Quantities
        self.loRadQuantTemp = QHBoxLayout()
        self.loRadQuant = QVBoxLayout()
        self.lblRadQuant = QLabel("Radiometric Quantity", self)
        self.cmbRadQuant = QComboBox()
        self.cmbRadQuant.addItems(
            ["Energy", "Flux", "Emittance", "Intensity", "Radiance", "Irradiance"])
        self.edtRadQuant = QLineEdit(self)
        self.edtRadQuant.setMaxLength(7)
        self.edtRadQuant.setText("1")
        self.lblRadQUnit = QLabel(self.RadUnits[0], self)
        self.loRadQuantTemp.addWidget(self.cmbRadQuant)
        self.loRadQuantTemp.addSpacing(4)
        self.loRadQuantTemp.addWidget(self.edtRadQuant)
        self.loRadQuantTemp.addSpacing(4)
        self.loRadQuantTemp.addWidget(self.lblRadQUnit)
        self.loRadQuant.addStretch()
        self.loRadQuant.addWidget(self.lblRadQuant)
        self.loRadQuant.addSpacing(3)
        self.loRadQuant.addLayout(self.loRadQuantTemp)
        self.loRadQuant.addStretch()

        # Photometric Quantities
        self.loPhotQuantTemp = QHBoxLayout()
        self.loPhotQuant = QVBoxLayout()
        self.lblPhotQuant = QLabel("Photometric Quantity", self)
        self.lblPhotQuantName = QLabel(self.LumQuant[0], self)
        self.edtPhotQuant = QLineEdit(self)
        self.edtPhotQuant.setMaxLength(7)
        self.edtPhotQuant.setText("683")
        self.lblPhotQUnit = QLabel(self.PhotUnits[0], self)
        self.loPhotQuantTemp.addWidget(self.lblPhotQuantName)
        self.loPhotQuantTemp.addSpacing(4)
        self.loPhotQuantTemp.addWidget(self.edtPhotQuant)
        self.loPhotQuantTemp.addSpacing(4)
        self.loPhotQuantTemp.addWidget(self.lblPhotQUnit)
        self.loPhotQuant.addStretch()
        self.loPhotQuant.addWidget(self.lblPhotQuant)
        self.loPhotQuant.addSpacing(3)
        self.loPhotQuant.addLayout(self.loPhotQuantTemp)
        self.loPhotQuant.addStretch()

        # Layout of Radiometric and Photometric Quantities
        self.loTemp = QHBoxLayout()
        self.loTemp.addStretch()
        self.loTemp.addLayout(self.loRadQuant)
        self.loTemp.addSpacing(15)
        self.loTemp.addLayout(self.loPhotQuant)
        self.loTemp.addStretch()

        # Master Layout
        self.loMaster = QVBoxLayout(self.main_widget)
        self.loMaster.addLayout(self.loCondition)
        self.loMaster.addSpacing(3)
        self.loMaster.addLayout(self.loWavelength)
        self.loMaster.addSpacing(20)
        self.loMaster.addLayout(self.loTemp)

        # Set focus to the main widget
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        # Connect the slots to the signals
        self.cmbCondition.currentIndexChanged.connect(self.conditionChanged)
        self.cmbRadQuant.currentIndexChanged.connect(self.radQuantChanged)
        self.edtRadQuant.editingFinished.connect(self.radQuantValChanged)
        self.edtPhotQuant.editingFinished.connect(self.photQuantValChanged)
        self.edtWavelength.editingFinished.connect(self.wavelengthChanged)

    def conditionChanged(self):
        condNum = self.cmbCondition.currentIndex()
        pVal = self.getVl(condNum)
        self.edtPhotQuant.setText(str(pVal))

    def radQuantChanged(self):
        indNum = self.cmbRadQuant.currentIndex()
        self.lblRadQUnit.setText(self.RadUnits[indNum])
        self.lblPhotQuantName.setText(self.LumQuant[indNum])
        self.lblPhotQUnit.setText(self.PhotUnits[indNum])

    def radQuantValChanged(self):
        condNum = self.cmbCondition.currentIndex()
        pVal = self.getVl(condNum)
        self.edtPhotQuant.setText(str(pVal))

    def photQuantValChanged(self):
        pVal = float(self.edtPhotQuant.text())
        condNum = self.cmbCondition.currentIndex()
        rVal = self.getVlInv(condNum)
        self.edtRadQuant.setText(str(rVal))

    def wavelengthChanged(self):
        wl = float(self.edtWavelength.text())
        if wl < 400:
            self.edtWavelength.setText("400")
        if wl > 700:
            self.edtWavelength.setText("700")
        condNum = self.cmbCondition.currentIndex()
        pVal = self.getVl(condNum)
        self.edtPhotQuant.setText(str(pVal))

    def getVl(self, i):
        wl = float(self.edtWavelength.text())
        rVal = float(self.edtRadQuant.text())
        # Photopic Vl = exp(-285.4*(wl-0.56)^2)
        if i == 0:
            Vl = 683 * exp(-285.4 * ((wl - 555.0) / 1000)**2) * rVal
        # Scotopic Vl = exp(-321.9*(wl-0.50)^2)
        else:
            Vl = 1704 * exp(-321.9 * ((wl - 507.0) / 1000)**2) * rVal
        return Vl

    def getVlInv(self, i):
        wl = float(self.edtWavelength.text())
        pVal = float(self.edtPhotQuant.text())
        # Photopic Vl = 1.02*exp(-285.4*(wl-0.56)^2)
        if i == 0:
            Vl = 1.0 / 683 * exp(-285.4 * ((wl - 555.0) / 1000)**2) * pVal
        # Scotopic Vl = 0.99*exp(-321.9*(wl-0.50)^2)
        else:
            Vl = 1.0 / 1704 * exp(-321.9 * ((wl - 507.0) / 1000)**2) * pVal
        return Vl


# Implement the main object
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApp = MainApp()
    MyApp.show()
    app.exec()
