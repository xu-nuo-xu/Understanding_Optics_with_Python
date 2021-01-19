# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FresnelMirror.ui'
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
        self.SpinBox_D = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D.setSuffix("")
        self.SpinBox_D.setDecimals(3)
        self.SpinBox_D.setMaximum(10.0)
        self.SpinBox_D.setSingleStep(0.1)
        self.SpinBox_D.setProperty("value", 1.2)
        self.SpinBox_D.setObjectName("SpinBox_D")
        self.gridLayout_2.addWidget(self.SpinBox_D, 1, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.SpinBox_Angle = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Angle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Angle.setSuffix("")
        self.SpinBox_Angle.setDecimals(3)
        self.SpinBox_Angle.setMaximum(5.0)
        self.SpinBox_Angle.setSingleStep(0.001)
        self.SpinBox_Angle.setProperty("value", 5.0)
        self.SpinBox_Angle.setObjectName("SpinBox_Angle")
        self.gridLayout_2.addWidget(self.SpinBox_Angle, 0, 7, 1, 1)
        self.SpinBox_Lambda = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda.setSuffix("")
        self.SpinBox_Lambda.setDecimals(3)
        self.SpinBox_Lambda.setMinimum(100.0)
        self.SpinBox_Lambda.setMaximum(2000.0)
        self.SpinBox_Lambda.setSingleStep(0.1)
        self.SpinBox_Lambda.setProperty("value", 632.0)
        self.SpinBox_Lambda.setObjectName("SpinBox_Lambda")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda, 0, 2, 1, 1)
        self.SpinBox_a = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_a.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_a.setSuffix("")
        self.SpinBox_a.setDecimals(3)
        self.SpinBox_a.setMaximum(1000.0)
        self.SpinBox_a.setSingleStep(0.05)
        self.SpinBox_a.setProperty("value", 800.0)
        self.SpinBox_a.setObjectName("SpinBox_a")
        self.gridLayout_2.addWidget(self.SpinBox_a, 1, 2, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Fresnel Mirror"))
        self.label_2.setText(_translate("MainWindow", "Angle between mirrors (mrad)"))
        self.label_4.setText(_translate("MainWindow", "Distance from the screen (m)"))
        self.label.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.label_3.setText(_translate("MainWindow", "Distance Source-Mirror (mm)"))

from mplwidget import MPL_WIDGET_2D
