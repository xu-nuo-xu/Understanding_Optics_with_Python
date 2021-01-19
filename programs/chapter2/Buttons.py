# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
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
        label3 = QLabel("", self)
        label3.setFixedSize(50, 50)
        label3.setPixmap(QPixmap("greating.svg"))
        label3.show()
        label3.move(250, 10)

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

    @pyqtSlot()  # Push Button 1 signal
    def on_click_button1(self):
        message = "<h3><b><font color='green'>Hello Python!</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)

    @pyqtSlot()  # Push Button 2 signal
    def on_click_button2(self):
        message = "<h3><b><font color='red'>Goodbye Python!</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())