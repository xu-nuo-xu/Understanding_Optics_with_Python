# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MachZehnder.ui'
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
        self.SpinBox_Lambda.setProperty("value", 600.0)
        self.SpinBox_Lambda.setObjectName("SpinBox_Lambda")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda, 2, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 5, 1, 1)
        self.SpinBox_F = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_F.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_F.setSuffix("")
        self.SpinBox_F.setDecimals(4)
        self.SpinBox_F.setMaximum(2.0)
        self.SpinBox_F.setSingleStep(0.0001)
        self.SpinBox_F.setProperty("value", 1.032)
        self.SpinBox_F.setObjectName("SpinBox_F")
        self.gridLayout_2.addWidget(self.SpinBox_F, 0, 6, 1, 1)
        self.SpinBox_WB = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_WB.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_WB.setDecimals(3)
        self.SpinBox_WB.setMinimum(0.0)
        self.SpinBox_WB.setMaximum(20000.0)
        self.SpinBox_WB.setSingleStep(0.01)
        self.SpinBox_WB.setProperty("value", 2.0)
        self.SpinBox_WB.setObjectName("SpinBox_WB")
        self.gridLayout_2.addWidget(self.SpinBox_WB, 1, 2, 1, 1)
        self.SpinBox_ndx = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_ndx.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_ndx.setDecimals(3)
        self.SpinBox_ndx.setMinimum(0.0)
        self.SpinBox_ndx.setMaximum(20.0)
        self.SpinBox_ndx.setSingleStep(0.01)
        self.SpinBox_ndx.setProperty("value", 1.5)
        self.SpinBox_ndx.setObjectName("SpinBox_ndx")
        self.gridLayout_2.addWidget(self.SpinBox_ndx, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.SpinBox_DLS = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_DLS.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_DLS.setSuffix("")
        self.SpinBox_DLS.setDecimals(3)
        self.SpinBox_DLS.setMinimum(0.01)
        self.SpinBox_DLS.setMaximum(20.0)
        self.SpinBox_DLS.setSingleStep(0.01)
        self.SpinBox_DLS.setProperty("value", 12.0)
        self.SpinBox_DLS.setObjectName("SpinBox_DLS")
        self.gridLayout_2.addWidget(self.SpinBox_DLS, 1, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.cbLens = QtWidgets.QCheckBox(self.centralWidget)
        self.cbLens.setChecked(True)
        self.cbLens.setObjectName("cbLens")
        self.gridLayout_2.addWidget(self.cbLens, 2, 1, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Mach Zehnder"))
        self.label_4.setText(_translate("MainWindow", "Focal length of the lens (m)"))
        self.label_2.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.label_7.setText(_translate("MainWindow", "Blade Index"))
        self.label_3.setText(_translate("MainWindow", "Distance Lens-Separator (mm)"))
        self.label_8.setText(_translate("MainWindow", "Width of blade (micron)"))
        self.cbLens.setText(_translate("MainWindow", "Lens"))

from mplwidget import MPL_WIDGET_2D
