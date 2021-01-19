# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QSpinBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # GUI proprieties
        self.setGeometry(400, 100, 300, 200)
        self.setWindowTitle('My first app')

        # Labels
        # Label 1: Plain text
        label1 = QLabel('My first application says:', self)
        label1.setFixedWidth(120)  # fixing the width of the label
        label1.move(10, 10)
        # Label 2: Rich text
        self.label2 = QLabel("", self)
        self.label2.move(130, 10)
        message = "<h3><b><font color='green'>Hello Python!</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)
        # Label 3: Image
        self.label3 = QLabel("", self)
        self.label3.setFixedSize(50, 50)
        self.label3.setPixmap(QPixmap("greating.svg"))
        self.label3.show()
        self.label3.move(250, 10)

        # Buttons
        # Push Button 1: Hello Button
        button1 = QPushButton('Hello', self)
        button1.setToolTip('This is the Hello Button')
        button1.move(50, 50)
        button1.clicked.connect(self.on_click_button1)
        # Push Button 2: Goodbye Button
        button2 = QPushButton('Goodbye', self)
        button2.setToolTip('This is the Goodbye Button')
        button2.move(170, 50)
        button2.clicked.connect(self.on_click_button2)

        # Spin Box: Spin Box change integer value from 0 to 100
        self.spb = QSpinBox(self)
        self.spb.setMinimum(0)
        self.spb.setMaximum(100)
        self.spb.setValue(50)
        self.spb.setSingleStep(1)
        self.spb.setGeometry(80, 110, 50, 20)  # set geometry (x,y,width,hight)
        self.spb.valueChanged.connect(self.spb_valuechange)
        self.spb.move(180, 160)
        # set a label saying what Spin Box refer to
        txt = QLabel('The value is: ', self)
        txt.setGeometry(10, 110, 75, 20)  # set geometry (x,y,width,hight)
        # set a label to a receive a value from the spin box
        self.val = QLabel("", self)
        # set geometry (x,y,width,height)
        self.val.setGeometry(150, 110, 75, 20)

    @pyqtSlot()  # Push Button 1 signal
    def on_click_button1(self):
        message = "<h3><b><font color='green'>Hello Python!</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)
        self.label3.setPixmap(QPixmap("greating.svg"))
        self.label3.show()

    @pyqtSlot()  # Push Button 2 signal
    def on_click_button2(self):
        message = "<h3><b><font color='red'>Goodbye Python!</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)
        self.label3.setPixmap(QPixmap("greating.svg"))
        self.label3.show()

    @pyqtSlot(int)  # Spin Box signal
    def spb_valuechange(self, value):
        '''
        the value of the spin box is an integer, 
        convert it to a string using the str() function.
        '''
        self.val.setText(str(self.spb.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())
