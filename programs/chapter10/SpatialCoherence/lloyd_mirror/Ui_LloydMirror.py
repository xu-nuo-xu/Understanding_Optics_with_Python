# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_LloydMirror.ui'
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
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 9, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 8, 1, 1)
        self.lineEdit_Period = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Period.setObjectName("lineEdit_Period")
        self.gridLayout_2.addWidget(self.lineEdit_Period, 0, 10, 1, 1)
        self.SpinBox_a = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_a.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_a.setSuffix("")
        self.SpinBox_a.setDecimals(3)
        self.SpinBox_a.setMaximum(50.0)
        self.SpinBox_a.setSingleStep(0.05)
        self.SpinBox_a.setProperty("value", 1.0)
        self.SpinBox_a.setObjectName("SpinBox_a")
        self.gridLayout_2.addWidget(self.SpinBox_a, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 6, 1, 1)
        self.SpinBox_Lambda = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda.setSuffix("")
        self.SpinBox_Lambda.setDecimals(3)
        self.SpinBox_Lambda.setMinimum(100.0)
        self.SpinBox_Lambda.setMaximum(2000.0)
        self.SpinBox_Lambda.setSingleStep(0.1)
        self.SpinBox_Lambda.setProperty("value", 632.0)
        self.SpinBox_Lambda.setObjectName("SpinBox_Lambda")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda, 0, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.SpinBox_D = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_D.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D.setSuffix("")
        self.SpinBox_D.setDecimals(3)
        self.SpinBox_D.setMaximum(50.0)
        self.SpinBox_D.setSingleStep(0.1)
        self.SpinBox_D.setProperty("value", 1.0)
        self.SpinBox_D.setObjectName("SpinBox_D")
        self.gridLayout_2.addWidget(self.SpinBox_D, 2, 7, 1, 1)
        self.SpinBox_b = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_b.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_b.setSuffix("")
        self.SpinBox_b.setDecimals(3)
        self.SpinBox_b.setMaximum(5.0)
        self.SpinBox_b.setSingleStep(0.001)
        self.SpinBox_b.setProperty("value", 0.045)
        self.SpinBox_b.setObjectName("SpinBox_b")
        self.gridLayout_2.addWidget(self.SpinBox_b, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 11, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 9, 1, 1)
        self.lineEdit_Contrast = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Contrast.setObjectName("lineEdit_Contrast")
        self.gridLayout_2.addWidget(self.lineEdit_Contrast, 2, 10, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Lloyd Mirror"))
        self.label_3.setText(_translate("MainWindow", "Distance Source-Plan a(mm)"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0c1d;\">Periode : X1(mm)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Distance from the screen D(m)"))
        self.label.setText(_translate("MainWindow", "Wavelength (nm)"))
        self.label_2.setText(_translate("MainWindow", "Slit width b(mm)"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0e19;\">γ=0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : X2(mm) </span></p></body></html>"))

from mplwidget import MPL_WIDGET_2D
