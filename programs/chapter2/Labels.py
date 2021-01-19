# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


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
        label2 = QLabel("", self)
        message = "<h3><b><font color='green'>Hello Python!</font></b>"
        label2.setText(message)
        label2.setFixedWidth(120)
        label2.move(130, 50)
        # Label 3: Image
        label3 = QLabel("", self)
        label3.setPixmap(QPixmap("greating.svg"))
        label3.setFixedSize(50, 50)
        label3.show()
        label3.move(250, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())
