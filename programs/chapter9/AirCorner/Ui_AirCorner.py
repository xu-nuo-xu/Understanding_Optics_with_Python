# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AirCorner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 5, 1, 1)
        self.SpinBox_Lambda = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda.setSuffix("")
        self.SpinBox_Lambda.setDecimals(0)
        self.SpinBox_Lambda.setMinimum(100.0)
        self.SpinBox_Lambda.setMaximum(2000.0)
        self.SpinBox_Lambda.setSingleStep(1.0)
        self.SpinBox_Lambda.setProperty("value", 530.0)
        self.SpinBox_Lambda.setObjectName("SpinBox_Lambda")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda, 2, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 5, 1, 1)
        self.SpinBox_D = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D.setSuffix("")
        self.SpinBox_D.setDecimals(3)
        self.SpinBox_D.setMaximum(2.0)
        self.SpinBox_D.setSingleStep(0.01)
        self.SpinBox_D.setProperty("value", 0.1)
        self.SpinBox_D.setObjectName("SpinBox_D")
        self.gridLayout_2.addWidget(self.SpinBox_D, 0, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        self.SpinBox_WS1 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_WS1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_WS1.setDecimals(3)
        self.SpinBox_WS1.setMinimum(0.0)
        self.SpinBox_WS1.setMaximum(10.0)
        self.SpinBox_WS1.setSingleStep(0.1)
        self.SpinBox_WS1.setProperty("value", 1.0)
        self.SpinBox_WS1.setObjectName("SpinBox_WS1")
        self.gridLayout_2.addWidget(self.SpinBox_WS1, 1, 2, 1, 1)
        self.SpinBox_TP = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_TP.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_TP.setDecimals(3)
        self.SpinBox_TP.setMinimum(0.0)
        self.SpinBox_TP.setMaximum(1.0)
        self.SpinBox_TP.setSingleStep(0.01)
        self.SpinBox_TP.setProperty("value", 0.96)
        self.SpinBox_TP.setObjectName("SpinBox_TP")
        self.gridLayout_2.addWidget(self.SpinBox_TP, 0, 2, 1, 1)
        self.SpinBox_WS2 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_WS2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_WS2.setDecimals(3)
        self.SpinBox_WS2.setMinimum(0.0)
        self.SpinBox_WS2.setMaximum(10.0)
        self.SpinBox_WS2.setSingleStep(0.1)
        self.SpinBox_WS2.setProperty("value", 2.0)
        self.SpinBox_WS2.setObjectName("SpinBox_WS2")
        self.gridLayout_2.addWidget(self.SpinBox_WS2, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.SpinBox_CA = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_CA.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_CA.setSuffix("")
        self.SpinBox_CA.setDecimals(2)
        self.SpinBox_CA.setMaximum(20.0)
        self.SpinBox_CA.setSingleStep(0.1)
        self.SpinBox_CA.setProperty("value", 1.0)
        self.SpinBox_CA.setObjectName("SpinBox_CA")
        self.gridLayout_2.addWidget(self.SpinBox_CA, 1, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplwidget = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget.setObjectName("mplwidget")
        self.verticalLayout.addWidget(self.mplwidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Air Corner"))
        self.label_4.setText(_translate("MainWindow", "Distance from the screen (m)"))
        self.label_2.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.label_9.setText(_translate("MainWindow", "Width of source (mrad)"))
        self.label_7.setText(_translate("MainWindow", "Transmission power T (%)"))
        self.label_3.setText(_translate("MainWindow", "Corner angle (mrad)"))
        self.label_8.setText(_translate("MainWindow", "Width of source (mrad)"))

from mplwidget import MPL_WIDGET_2D
