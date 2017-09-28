#! usr/bin/python #coding=utf-8
import sys
import random
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from matplotlib.ticker import MultipleLocator, FormatStrFormatter  
xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式  
ymajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式

class NavToolbar(NavigationToolbar):
    #toolitems = [('Save', 'Save the figure', 'filesave', 'save_figure')]
    #toolitems = []
    pass

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, title='Scan'):
        self.title = title
        # fig = Figure(figsize=(width, height), dpi=dpi)
        fig = Figure()
        self.axes = fig.add_subplot(111)
        fig.suptitle(title)
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.axes.xaxis.set_major_formatter(xmajorFormatter)  
        self.axes.yaxis.set_major_formatter(ymajorFormatter)  
    def configXAxis(self):
        pass
    
    def configYAxis(self):
        pass
    
    def drawData(self, scanData):
        pass

class AScanMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, parent = None, title='AScan'):
        MyMplCanvas.__init__(self, parent, title)
        self.axes.grid(True, linestyle = "-.")
        self.m_aScanPlotter = None
        self.m_gatePlotter = {'#FF0000': None, '#0000FF': None, '#00FF00': None}
    
    def configXAxis(self, start, end, stepNum,  label = 'x'):
        self.m_xStart = start
        self.m_xEnd = end
        self.m_xStepNum = stepNum
        self.m_xLabel = label
    
    def setXAxis(self):
        self.axes.set_xticks(np.linspace(self.m_xStart, self.m_xEnd, self.m_xStepNum))
        self.axes.set_xlim(self.m_xStart, self.m_xEnd * 1.02)
        self.axes.set_xlabel(self.m_xLabel)
    
    def configYAxis(self, start, end, stepNum,  label = 'y'):
        self.m_yStart = start
        self.m_yEnd = end
        self.m_yStepNum = stepNum
        self.m_yLabel = label
        
    def setYAxis(self):
        self.axes.set_yticks(np.linspace(self.m_yStart, self.m_yEnd, self.m_yStepNum))
        self.axes.set_ylim(self.m_yStart, self.m_yEnd * 1.02)
        self.axes.set_ylabel(self.m_yLabel)
    
    def drawData(self, scanData):
        if self.m_aScanPlotter == None:
            self.m_aScanPlotter, = self.axes.plot(scanData['x'], scanData['y'])
        else:
            self.m_aScanPlotter.set_data(scanData['x'], scanData['y'])
        self.axes.grid(True, linestyle = "-.")
        self.setXAxis()
        self.setYAxis()
        self.draw()
    def drawGate(self, gate):
        if not gate.m_enabled:
            datax = [gate.m_start]
            datay = [gate.m_threshold]
        else:
            datax = [gate.m_start, gate.m_start + gate.m_len]
            datay = [gate.m_threshold, gate.m_threshold]
        colorStr = gate.m_color
        if self.m_gatePlotter[colorStr] is None:
            self.m_gatePlotter[colorStr],  = self.axes.plot(np.array(datax),  colorStr)
        else:
            self.m_gatePlotter[colorStr].set_data(np.array(datax),  np.array(datay))
#        self.axes.grid(True, linestyle = "-.")
#        self.setXAxis()
#        self.setYAxis()
#        self.draw()

class AScanWidget(QWidget):
    def __init__(self,  parent = None):
        QWidget.__init__(self, parent)
        layout = QVBoxLayout()
        self.m_aScanCanvas = AScanMplCanvas(self)
        toolBar = NavToolbar(self.m_aScanCanvas, self) # only save button
        layout.addWidget(toolBar)
        layout.addWidget(self.m_aScanCanvas)
        self.setLayout(layout)
    
    def configXAxis(self, start, end, step,  label = 'x'):
        self.m_aScanCanvas.configXAxis(start, end, step, label)
    
    def configYAxis(self, start, end, step,  label = 'y'):
        self.m_aScanCanvas.configYAxis(start, end, step, label)
    
    def drawData(self, data):
        self.m_aScanCanvas.drawData(data)
    
    def drawGate(self, gate):
        self.m_aScanCanvas.drawGate(gate)
        

class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        self.main_widget = AScanWidget(self)
        self.setCentralWidget(self.main_widget)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt4 Matplot Example")
    aw.show()
    app.exec_()
