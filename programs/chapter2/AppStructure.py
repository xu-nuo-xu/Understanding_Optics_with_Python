# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # GUI proprieties
        self.setGeometry(400, 100, 300, 200)
        self.setWindowTitle('My first app')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())
