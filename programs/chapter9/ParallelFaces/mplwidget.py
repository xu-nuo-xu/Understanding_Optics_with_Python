# -*- coding: utf-8 -*-
# PART 1): Importing libraries and functions
import sys
if __name__ == '__main__':
    try:
        # Use PyQt5 if present
        from PyQt5.QtCore import QT_VERSION_STR
        import matplotlib
        matplotlib.use("Qt5Agg")
        print("Qt version:", QT_VERSION_STR)
    except:
        # Else, use PyQt4
        from PyQt4.QtCore import QT_VERSION_STR
        print("Qt version:", QT_VERSION_STR)

# Import PyQt Widgets and Matplotlib canvas for actually used PyQt version
if "PyQt5" in sys.modules:
    from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout

    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
elif "PyQt4" in sys.modules:

    from PyQt4.QtGui import QSizePolicy, QWidget, QVBoxLayout

    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
else:
    raise SystemError("PyQt4 or PyQt5 need to be installed first")

from matplotlib.figure import Figure

from matplotlib import rcParams
rcParams['font.size'] = 9
# PART 2): Wdget class


class MplCanvas(FigureCanvas):

    def __init__(self, dpi=100):
        self.fig = Figure(dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MPL_WIDGET_2D(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas()  # create canvas that will hold our plot
        # createa navigation toolbar for our plot canvas
        self.navi_toolbar = NavigationToolbar(self.canvas, self)

        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.navi_toolbar)
        self.setLayout(self.vbl)
