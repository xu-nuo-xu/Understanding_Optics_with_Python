# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FresnelEdge.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_Lambda = QtWidgets.QLabel(self.centralWidget)
        self.label_Lambda.setObjectName("label_Lambda")
        self.gridLayout.addWidget(self.label_Lambda, 0, 0, 1, 1)
        self.label_D = QtWidgets.QLabel(self.centralWidget)
        self.label_D.setObjectName("label_D")
        self.gridLayout.addWidget(self.label_D, 0, 2, 1, 1)
        self.SpinBox_D = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D.setDecimals(3)
        self.SpinBox_D.setMinimum(100.0)
        self.SpinBox_D.setMaximum(1000.0)
        self.SpinBox_D.setObjectName("SpinBox_D")
        self.gridLayout.addWidget(self.SpinBox_D, 0, 3, 1, 1)
        self.SpinBox_Lambda = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda.setDecimals(3)
        self.SpinBox_Lambda.setMinimum(200.0)
        self.SpinBox_Lambda.setMaximum(800.0)
        self.SpinBox_Lambda.setProperty("value", 632.0)
        self.SpinBox_Lambda.setObjectName("SpinBox_Lambda")
        self.gridLayout.addWidget(self.SpinBox_Lambda, 0, 1, 1, 1)
        self.Slider_D = QtWidgets.QSlider(self.centralWidget)
        self.Slider_D.setMinimum(100)
        self.Slider_D.setMaximum(1000)
        self.Slider_D.setSingleStep(10)
        self.Slider_D.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_D.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_D.setTickInterval(25)
        self.Slider_D.setObjectName("Slider_D")
        self.gridLayout.addWidget(self.Slider_D, 1, 3, 1, 1)
        self.Slider_Lambda = QtWidgets.QSlider(self.centralWidget)
        self.Slider_Lambda.setMinimum(200)
        self.Slider_Lambda.setMaximum(800)
        self.Slider_Lambda.setProperty("value", 632)
        self.Slider_Lambda.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Lambda.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_Lambda.setTickInterval(25)
        self.Slider_Lambda.setObjectName("Slider_Lambda")
        self.gridLayout.addWidget(self.Slider_Lambda, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.mplwidget = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget.setObjectName("mplwidget")
        self.verticalLayout_2.addWidget(self.mplwidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fresnel Edge"))
        self.label_Lambda.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.label_D.setText(_translate("MainWindow", "Distance from the screen (cm)"))

from mplwidget import MPL_WIDGET_2D
