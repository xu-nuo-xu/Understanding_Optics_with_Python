# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DoubleSlit1D.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 777)
        MainWindow.setMinimumSize(QtCore.QSize(780, 0))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplwidget1D = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget1D.setMinimumSize(QtCore.QSize(650, 0))
        self.mplwidget1D.setObjectName("mplwidget1D")
        self.horizontalLayout.addWidget(self.mplwidget1D)
        MainWindow.setCentralWidget(self.centralWidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setMinimumSize(QtCore.QSize(205, 735))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_lamda = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_lamda.setObjectName("label_lamda")
        self.verticalLayout.addWidget(self.label_lamda)
        self.SpinBox_lambda = QtWidgets.QSpinBox(self.dockWidgetContents_3)
        self.SpinBox_lambda.setMinimumSize(QtCore.QSize(0, 20))
        self.SpinBox_lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_lambda.setMinimum(400)
        self.SpinBox_lambda.setMaximum(900)
        self.SpinBox_lambda.setSingleStep(10)
        self.SpinBox_lambda.setProperty("value", 632)
        self.SpinBox_lambda.setObjectName("SpinBox_lambda")
        self.verticalLayout.addWidget(self.SpinBox_lambda)
        self.slider_lambda = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_lambda.setMinimumSize(QtCore.QSize(0, 25))
        self.slider_lambda.setStyleSheet("font: 12pt \"Helvetica\";")
        self.slider_lambda.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_lambda.setMinimum(400)
        self.slider_lambda.setMaximum(900)
        self.slider_lambda.setSingleStep(10)
        self.slider_lambda.setProperty("value", 632)
        self.slider_lambda.setOrientation(QtCore.Qt.Horizontal)
        self.slider_lambda.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_lambda.setTickInterval(50)
        self.slider_lambda.setObjectName("slider_lambda")
        self.verticalLayout.addWidget(self.slider_lambda)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SpinBox_sx = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_sx.setMinimumSize(QtCore.QSize(0, 20))
        self.SpinBox_sx.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_sx.setDecimals(1)
        self.SpinBox_sx.setMinimum(0.1)
        self.SpinBox_sx.setSingleStep(1.0)
        self.SpinBox_sx.setProperty("value", 5.0)
        self.SpinBox_sx.setObjectName("SpinBox_sx")
        self.gridLayout_2.addWidget(self.SpinBox_sx, 4, 1, 1, 1)
        self.slider_sx = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_sx.setMinimumSize(QtCore.QSize(0, 25))
        self.slider_sx.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_sx.setMinimum(1)
        self.slider_sx.setMaximum(100)
        self.slider_sx.setProperty("value", 5)
        self.slider_sx.setOrientation(QtCore.Qt.Horizontal)
        self.slider_sx.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_sx.setTickInterval(10)
        self.slider_sx.setObjectName("slider_sx")
        self.gridLayout_2.addWidget(self.slider_sx, 5, 1, 1, 1)
        self.slider_b = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_b.setMinimumSize(QtCore.QSize(0, 25))
        self.slider_b.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_b.setMinimum(1)
        self.slider_b.setMaximum(1000)
        self.slider_b.setSingleStep(1)
        self.slider_b.setPageStep(100)
        self.slider_b.setProperty("value", 435)
        self.slider_b.setOrientation(QtCore.Qt.Horizontal)
        self.slider_b.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_b.setTickInterval(100)
        self.slider_b.setObjectName("slider_b")
        self.gridLayout_2.addWidget(self.slider_b, 2, 0, 1, 1)
        self.SpinBox_b = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_b.setMinimumSize(QtCore.QSize(0, 20))
        self.SpinBox_b.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_b.setDecimals(2)
        self.SpinBox_b.setMinimum(0.1)
        self.SpinBox_b.setMaximum(1000.0)
        self.SpinBox_b.setSingleStep(0.1)
        self.SpinBox_b.setProperty("value", 435.0)
        self.SpinBox_b.setObjectName("SpinBox_b")
        self.gridLayout_2.addWidget(self.SpinBox_b, 1, 0, 1, 1)
        self.SpinBox_db = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_db.setMinimumSize(QtCore.QSize(0, 20))
        self.SpinBox_db.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_db.setDecimals(1)
        self.SpinBox_db.setMinimum(0.0)
        self.SpinBox_db.setMaximum(500.0)
        self.SpinBox_db.setSingleStep(10.0)
        self.SpinBox_db.setProperty("value", 0.0)
        self.SpinBox_db.setObjectName("SpinBox_db")
        self.gridLayout_2.addWidget(self.SpinBox_db, 1, 1, 1, 1)
        self.SpinBox_a = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_a.setMinimumSize(QtCore.QSize(0, 20))
        self.SpinBox_a.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_a.setDecimals(3)
        self.SpinBox_a.setMinimum(0.0)
        self.SpinBox_a.setMaximum(10.0)
        self.SpinBox_a.setSingleStep(0.01)
        self.SpinBox_a.setProperty("value", 0.1)
        self.SpinBox_a.setObjectName("SpinBox_a")
        self.gridLayout_2.addWidget(self.SpinBox_a, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.slider_db = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_db.setMinimumSize(QtCore.QSize(0, 25))
        self.slider_db.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_db.setMaximum(500)
        self.slider_db.setSingleStep(10)
        self.slider_db.setProperty("value", 0)
        self.slider_db.setOrientation(QtCore.Qt.Horizontal)
        self.slider_db.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_db.setTickInterval(50)
        self.slider_db.setObjectName("slider_db")
        self.gridLayout_2.addWidget(self.slider_db, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.slider_a = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_a.setMinimumSize(QtCore.QSize(0, 25))
        self.slider_a.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_a.setMaximum(10)
        self.slider_a.setSingleStep(1)
        self.slider_a.setPageStep(1)
        self.slider_a.setProperty("value", 0)
        self.slider_a.setOrientation(QtCore.Qt.Horizontal)
        self.slider_a.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_a.setTickInterval(1)
        self.slider_a.setObjectName("slider_a")
        self.gridLayout_2.addWidget(self.slider_a, 5, 0, 1, 1)
        self.label_a = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_a.setObjectName("label_a")
        self.gridLayout_2.addWidget(self.label_a, 3, 1, 1, 1)
        self.label_b = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_b.setObjectName("label_b")
        self.gridLayout_2.addWidget(self.label_b, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_f2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_f2.setObjectName("label_f2")
        self.verticalLayout.addWidget(self.label_f2)
        self.SpinBox_D = QtWidgets.QDoubleSpinBox(self.dockWidgetContents_3)
        self.SpinBox_D.setMinimumSize(QtCore.QSize(0, 20))
        self.SpinBox_D.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_D.setDecimals(1)
        self.SpinBox_D.setMinimum(0.1)
        self.SpinBox_D.setMaximum(50.0)
        self.SpinBox_D.setProperty("value", 1.0)
        self.SpinBox_D.setObjectName("SpinBox_D")
        self.verticalLayout.addWidget(self.SpinBox_D)
        self.slider_D = QtWidgets.QSlider(self.dockWidgetContents_3)
        self.slider_D.setMinimumSize(QtCore.QSize(0, 25))
        self.slider_D.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.slider_D.setMinimum(1)
        self.slider_D.setMaximum(50)
        self.slider_D.setProperty("value", 1)
        self.slider_D.setSliderPosition(1)
        self.slider_D.setOrientation(QtCore.Qt.Horizontal)
        self.slider_D.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_D.setTickInterval(10)
        self.slider_D.setObjectName("slider_D")
        self.verticalLayout.addWidget(self.slider_D)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Internal_Spot = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.Internal_Spot.setObjectName("Internal_Spot")
        self.gridLayout.addWidget(self.Internal_Spot, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_4.setMinimumSize(QtCore.QSize(0, 13))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.Central_Spot = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.Central_Spot.setMinimumSize(QtCore.QSize(0, 20))
        self.Central_Spot.setObjectName("Central_Spot")
        self.gridLayout.addWidget(self.Central_Spot, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.dockWidget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 915, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diffraction - Fraunhofer"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Setting"))
        self.label_lamda.setText(_translate("MainWindow", "Wavelength(nm)"))
        self.SpinBox_lambda.setStatusTip(_translate("MainWindow", "Change the wave length of monochromatic light"))
        self.slider_lambda.setStatusTip(_translate("MainWindow", "Change the wave length of monochromatic light"))
        self.SpinBox_sx.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.slider_sx.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.slider_b.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.SpinBox_b.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>&Delta;b( &mu;m)</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "a(cm)"))
        self.label_a.setText(_translate("MainWindow", "sx(mm)"))
        self.label_b.setText(_translate("MainWindow", "<html><head/><body><p>b1( &mu;m)</p></body></html>"))
        self.label_f2.setText(_translate("MainWindow", "D(m)"))
        self.SpinBox_D.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))
        self.slider_D.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Internal Spot</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Central spot</span></p></body></html>"))

from mplwidget import MPL_WIDGET_2D
