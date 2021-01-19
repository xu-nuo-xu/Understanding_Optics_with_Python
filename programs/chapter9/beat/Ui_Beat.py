# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Beat.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 557)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.label_xParam = QtWidgets.QLabel(self.centralWidget)
        self.label_xParam.setObjectName("label_xParam")
        self.gridLayout.addWidget(self.label_xParam, 3, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 7, 1, 1)
        self.label_dBeta = QtWidgets.QLabel(self.centralWidget)
        self.label_dBeta.setObjectName("label_dBeta")
        self.gridLayout.addWidget(self.label_dBeta, 2, 3, 1, 1)
        self.label_fc = QtWidgets.QLabel(self.centralWidget)
        self.label_fc.setObjectName("label_fc")
        self.gridLayout.addWidget(self.label_fc, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.lineEdit_GvCurs = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_GvCurs.setObjectName("lineEdit_GvCurs")
        self.gridLayout.addWidget(self.lineEdit_GvCurs, 2, 8, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 7, 1, 1)
        self.lineEdit_Gv = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Gv.setObjectName("lineEdit_Gv")
        self.gridLayout.addWidget(self.lineEdit_Gv, 0, 8, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 7, 1, 1)
        self.lineEdit_PvCurs = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_PvCurs.setText("")
        self.lineEdit_PvCurs.setObjectName("lineEdit_PvCurs")
        self.gridLayout.addWidget(self.lineEdit_PvCurs, 4, 8, 1, 1)
        self.lineEdit_Pv = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_Pv.setObjectName("lineEdit_Pv")
        self.gridLayout.addWidget(self.lineEdit_Pv, 3, 8, 1, 1)
        self.SpinBox_dFreq = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_dFreq.setMinimumSize(QtCore.QSize(70, 0))
        self.SpinBox_dFreq.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_dFreq.setDecimals(3)
        self.SpinBox_dFreq.setMaximum(0.1)
        self.SpinBox_dFreq.setSingleStep(0.001)
        self.SpinBox_dFreq.setProperty("value", 0.005)
        self.SpinBox_dFreq.setObjectName("SpinBox_dFreq")
        self.gridLayout.addWidget(self.SpinBox_dFreq, 0, 4, 1, 1)
        self.SpinBox_dBeta = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_dBeta.setMinimumSize(QtCore.QSize(70, 0))
        self.SpinBox_dBeta.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_dBeta.setDecimals(3)
        self.SpinBox_dBeta.setMinimum(0.01)
        self.SpinBox_dBeta.setMaximum(21.0)
        self.SpinBox_dBeta.setSingleStep(0.001)
        self.SpinBox_dBeta.setProperty("value", 1.745)
        self.SpinBox_dBeta.setObjectName("SpinBox_dBeta")
        self.gridLayout.addWidget(self.SpinBox_dBeta, 2, 4, 1, 1)
        self.SpinBox_xParam = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_xParam.setMinimumSize(QtCore.QSize(70, 0))
        self.SpinBox_xParam.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_xParam.setDecimals(1)
        self.SpinBox_xParam.setMaximum(10.0)
        self.SpinBox_xParam.setSingleStep(0.1)
        self.SpinBox_xParam.setProperty("value", 0.0)
        self.SpinBox_xParam.setObjectName("SpinBox_xParam")
        self.gridLayout.addWidget(self.SpinBox_xParam, 3, 4, 1, 1)
        self.SpinBox_tParam = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_tParam.setMinimumSize(QtCore.QSize(70, 0))
        self.SpinBox_tParam.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_tParam.setKeyboardTracking(False)
        self.SpinBox_tParam.setDecimals(1)
        self.SpinBox_tParam.setMaximum(30.0)
        self.SpinBox_tParam.setSingleStep(0.1)
        self.SpinBox_tParam.setProperty("value", 0.0)
        self.SpinBox_tParam.setObjectName("SpinBox_tParam")
        self.gridLayout.addWidget(self.SpinBox_tParam, 4, 4, 1, 1)
        self.label_k = QtWidgets.QLabel(self.centralWidget)
        self.label_k.setObjectName("label_k")
        self.gridLayout.addWidget(self.label_k, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 9, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.Slider_fc = QtWidgets.QSlider(self.centralWidget)
        self.Slider_fc.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Slider_fc.setMaximum(10)
        self.Slider_fc.setPageStep(1)
        self.Slider_fc.setProperty("value", 6)
        self.Slider_fc.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_fc.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_fc.setTickInterval(2)
        self.Slider_fc.setObjectName("Slider_fc")
        self.gridLayout.addWidget(self.Slider_fc, 2, 0, 1, 1)
        self.SpinBox_k = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_k.setMinimumSize(QtCore.QSize(70, 0))
        self.SpinBox_k.setMaximumSize(QtCore.QSize(53, 16777215))
        self.SpinBox_k.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_k.setDecimals(3)
        self.SpinBox_k.setMinimum(5.0)
        self.SpinBox_k.setMaximum(21.0)
        self.SpinBox_k.setSingleStep(0.001)
        self.SpinBox_k.setProperty("value", 12.217)
        self.SpinBox_k.setObjectName("SpinBox_k")
        self.gridLayout.addWidget(self.SpinBox_k, 4, 1, 1, 1)
        self.SpinBox_fc = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_fc.setMinimumSize(QtCore.QSize(70, 0))
        self.SpinBox_fc.setMaximumSize(QtCore.QSize(53, 16777215))
        self.SpinBox_fc.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_fc.setDecimals(1)
        self.SpinBox_fc.setMinimum(0.2)
        self.SpinBox_fc.setMaximum(1.0)
        self.SpinBox_fc.setSingleStep(0.1)
        self.SpinBox_fc.setProperty("value", 0.6)
        self.SpinBox_fc.setObjectName("SpinBox_fc")
        self.gridLayout.addWidget(self.SpinBox_fc, 2, 1, 1, 1)
        self.Slider_k = QtWidgets.QSlider(self.centralWidget)
        self.Slider_k.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Slider_k.setMinimum(5)
        self.Slider_k.setMaximum(21)
        self.Slider_k.setProperty("value", 12)
        self.Slider_k.setSliderPosition(12)
        self.Slider_k.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_k.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_k.setTickInterval(2)
        self.Slider_k.setObjectName("Slider_k")
        self.gridLayout.addWidget(self.Slider_k, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.mplwidget1 = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.mplwidget1.setObjectName("mplwidget1")
        self.verticalLayout.addWidget(self.mplwidget1)
        self.mplwidget2 = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.mplwidget2.setObjectName("mplwidget2")
        self.verticalLayout.addWidget(self.mplwidget2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beats"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0d12;\">Vf cursor (m/s)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Parameter t (fs)"))
        self.label_xParam.setText(_translate("MainWindow", "Parameter x (nm)"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff1216;\">Vg cursor (m/s)</span></p></body></html>"))
        self.label_dBeta.setText(_translate("MainWindow", "<html><head/><body><p>d&beta; (10<span style=\" vertical-align:super;\">4</span> cm<span style=\" vertical-align:super;\">-1</span>)</p></body></html>"))
        self.label_fc.setText(_translate("MainWindow", "<html><head/><body><p>Central &nu; (PHz)</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>d&nu; (PHz)</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Vg=dω/dβ (m/s) </p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>Vf=&omega;/&beta;   (m/s)</p></body></html>"))
        self.label_k.setText(_translate("MainWindow", "<html><head/><body><p>k (10<span style=\" vertical-align:super;\">4</span> cm<span style=\" vertical-align:super;\">-1</span>)</p></body></html>"))

from mplwidget import MPL_WIDGET_2D