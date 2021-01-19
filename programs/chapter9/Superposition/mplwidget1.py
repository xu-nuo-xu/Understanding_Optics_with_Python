# -*- coding: utf-8 -*-
'''
            **** MATPLOTLIB WIDGET  ****
'''

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
    from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout
    from PyQt5.QtCore import QSize
    
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
    from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
elif "PyQt4" in sys.modules:

    from PyQt4.QtGui import QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout
    from PyQt4.QtCore import QSize
    
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as Canvas
    from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
else:
    raise SystemError("PyQt4 or PyQt5 need to be installed first")

from matplotlib.figure import Figure

from matplotlib import rcParams
rcParams['font.size'] = 9
# PART 2): Wdget class
class QtMplCanvas(Canvas):
    def __init__(self, parent=None, width = 6.5, height = 5.5, dpi = 50, sharex = None, sharey = None, fig = None):
        if fig == None:
            self.fig = Figure(figsize = (width, height), dpi=dpi, facecolor = '#FFFFFF')
            self.ax = self.fig.add_subplot(111, projection='3d')
            self.fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)
            self.ax.hold(True)
        else:
            self.fig = fig

        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QSize(w, h)

    def minimumSizeHint(self):
        return QSize(10, 10)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QSize(w, h)

    def minimumSizeHint(self):
        return QSize(10, 10)


class MyNavigationToolbar(NavigationToolbar) :
    def __init__(self, parent, canvas, direction = 'h' ) :

        self.canvas = canvas
        QWidget.__init__( self, parent )

        if direction=='h' :
            self.layout = QHBoxLayout( self )
        else :
            self.layout = QVBoxLayout( self )

        self.layout.setMargin( 2 )
        self.layout.setSpacing( 0 )

        NavigationToolbar.__init__( self, canvas )


    def set_message( self, s ):
        pass


class MPL_WIDGET_3D(QWidget):
    def __init__(self, parent = None, enableAutoScale = False, enableCSV = False, enableEdit = False, fig = None):
        QWidget.__init__(self, parent)
        self.canvas = QtMplCanvas(fig)
        self.canvas.ax.mouse_init()
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        self.setLayout(self.vbox)

class MatplotlibWidget(Canvas):
    """
    MatplotlibWidget inherits PyQt4.QWidget
    and matplotlib.backend_bases.FigureCanvasBase
    
    """
    def __init__(self, parent=None, title='',suptitle='', xlabel='', ylabel='',
                 xlim=None, ylim=None, xscale='linear', yscale='linear',
                 width=6.5, height= 5.5, dpi=40):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title(title)
        self.figure.suptitle(suptitle)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
       

        if xscale is not None:
            self.ax.set_xscale(xscale)
        if yscale is not None:
            self.ax.set_yscale(yscale)
        if xlim is not None:
            self.ax.set_xlim(*xlim)
        if ylim is not None:
            self.ax.set_ylim(*ylim)
#        self.ax.hold(hold)

        Canvas.__init__(self, self.figure)
        self.setParent(parent)
        Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QSize(w, h)

    def minimumSizeHint(self):
        return QSize(10, 10)
        
class MPL_WIDGET_2D(QWidget):
    def __init__(self, parent = None, enableAutoScale = False, enableCSV = False, enableEdit = False, fig = None):
        QWidget.__init__(self, parent)
        self.canvas = MatplotlibWidget(fig)
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        self.setLayout(self.vbox)

