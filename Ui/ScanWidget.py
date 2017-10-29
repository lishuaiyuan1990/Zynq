#! usr/bin/python #coding=utf-8
import sys
import random
import numpy as np
import matplotlib
import copy
matplotlib.use("Qt5Agg")
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QComboBox, QHBoxLayout
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from matplotlib.ticker import MultipleLocator, FormatStrFormatter  
xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式  
ymajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

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
        #fig.suptitle(title)
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
    def __init__(self, parent = None, title=None):
        MyMplCanvas.__init__(self, parent, title)
        self.axes.grid(True, linestyle = "-.")
        self.m_aScanPlotter = None
        self.m_updateAxis = True
        self.m_gatePlotter = {'#FF0000': None, '#0000FF': None, '#00FF00': None, '#FFFF00': None}
    
    def configXAxis(self, start, end, stepNum,  label = 'x'):
        self.m_xStart = start
        self.m_xEnd = end
        self.m_xStepNum = stepNum
        self.m_xLabel = label
    
    def setXAxis(self):
        self.axes.set_xticks(np.linspace(self.m_xStart, self.m_xEnd, self.m_xStepNum))
        self.axes.set_xlim(self.m_xStart, self.m_xEnd * 1.001)
        self.axes.set_xlabel(self.m_xLabel)
    
    def configYAxis(self, start, end, stepNum,  label = 'y'):
        self.m_yStart = start
        self.m_yEnd = end
        self.m_yStepNum = stepNum
        self.m_yLabel = label
        
    def setYAxis(self):
        self.axes.set_yticks(np.linspace(self.m_yStart, self.m_yEnd, self.m_yStepNum))
        self.axes.set_ylim(self.m_yStart, self.m_yEnd * 1.005)
        self.axes.set_ylabel(self.m_yLabel)
    
    def updateAxis(self):
        self.m_updateAxis = True
    
    def drawData(self, scanData):
        if self.m_aScanPlotter == None:
            self.m_aScanPlotter, = self.axes.plot(scanData['x'], scanData['y'])
        else:
            self.m_aScanPlotter.set_data(scanData['x'], scanData['y'])
        if self.m_updateAxis:
            self.axes.grid(True, linestyle = "-.")
            self.setXAxis()
            self.setYAxis()
            self.m_updateAxis = False
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
        self.m_aScanCanvas = AScanMplCanvas(self, None)
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
    
    def updateAxis(self):
        self.m_aScanCanvas.updateAxis()

class AScanWidgetMultiChano(QWidget):
    def __init__(self,  parent = None):
        QWidget.__init__(self, parent)
        layout = QVBoxLayout()
        self.m_aScanCanvas = AScanMplCanvas(self)
        toolBar = NavToolbar(self.m_aScanCanvas, self) # only save button
        self.m_chanNo = self.genChanComboBox()
        layout.setContentsMargins(0, 0, 0, 0)
        #
        subLayout = QHBoxLayout()
        subLayout.setContentsMargins(0, 0, 0, 0)
        subLayout.addWidget(toolBar)
        subLayout.addWidget(self.m_chanNo)
        layout.addLayout(subLayout)
        layout.addWidget(self.m_aScanCanvas)
        self.setLayout(layout)

    def genChanComboBox(self):
        self.m_chanNo = QComboBox(self)
        self.m_chanNo.setObjectName(_fromUtf8("m_chanNo"))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.setItemText(0, _translate("ParseToolWidget", "通道1", None))
        self.m_chanNo.setItemText(1, _translate("ParseToolWidget", "通道2", None))
        self.m_chanNo.setItemText(2, _translate("ParseToolWidget", "通道3", None))
        self.m_chanNo.setItemText(3, _translate("ParseToolWidget", "通道4", None))
        self.m_chanNo.setItemText(4, _translate("ParseToolWidget", "通道5", None))
        self.m_chanNo.setItemText(5, _translate("ParseToolWidget", "通道6", None))
        self.m_chanNo.setItemText(6, _translate("ParseToolWidget", "通道7", None))
        self.m_chanNo.setItemText(7, _translate("ParseToolWidget", "通道8", None))
        return self.m_chanNo
    
    def configXAxis(self, start, end, step,  label = 'x'):
        self.m_aScanCanvas.configXAxis(start, end, step, label)
    
    def configYAxis(self, start, end, step,  label = 'y'):
        self.m_aScanCanvas.configYAxis(start, end, step, label)
    
    def drawData(self, data):
        self.m_aScanCanvas.drawData(data)
    
    def drawGate(self, gate):
        self.m_aScanCanvas.drawGate(gate)
    
    def updateAxis(self):
        self.m_aScanCanvas.updateAxis()
        

class MyMplCanvasMultiChano(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, title='Channel'):
        self.m_fig = Figure(figsize=(50,8), dpi = 100, tight_layout=True)
        #plt.tight_layout()
        FigureCanvas.__init__(self, self.m_fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.title = title
        # fig = Figure(figsize=(width, height), dpi=dpi)
        
        #fig.suptitle(title)
        # We want the axes cleared every time plot() is called
        
        #
        self.genMultiAxes(self.m_fig)
        
        

    def genMultiAxes(self, fig):
        print "1"
        plotRange = 420
        self.axesSet = []
        for i in range(0, 8):
            plotRange += 1
            axes = fig.add_subplot(plotRange)
            axes.set_title("%s %d" % (self.title, i + 1))
            axes.xaxis.set_major_formatter(xmajorFormatter)  
            axes.yaxis.set_major_formatter(ymajorFormatter)
            #axes.hold(False)  
            axes.grid(True, linestyle = "-.")
            self.axesSet.append(axes)
        return

    def configXAxis(self):
        pass
    
    def configYAxis(self):
        pass
    
    def drawData(self, scanData):
        pass

class AScanMplCanvasMultiChano(MyMplCanvasMultiChano):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, parent = None, title='Channel'):
        MyMplCanvasMultiChano.__init__(self, parent, title)
        self.m_aScanPlotterSet = None
        self.m_updateAxis = True
        self.m_gatePlotterSet = {'#FF0000': None, '#0000FF': None, '#00FF00': None, '#00FFFF': None}
        self.m_testScanData = None
    
    def configXAxis(self, start, end, stepNum,  label = 'x'):
        self.m_xStart = start
        self.m_xEnd = end
        self.m_xStepNum = stepNum
        self.m_xLabel = label
    
    def setXAxis(self):
        for axes in self.axesSet:
            axes.set_xticks(np.linspace(self.m_xStart, self.m_xEnd, self.m_xStepNum))
            axes.set_xlim(self.m_xStart, self.m_xEnd * 1.001)
            axes.set_xlabel(self.m_xLabel)
        return

    
    def configYAxis(self, start, end, stepNum,  label = 'y'):
        self.m_yStart = start
        self.m_yEnd = end
        self.m_yStepNum = stepNum
        self.m_yLabel = label
        
    def setYAxis(self):
        for axes in self.axesSet:
            axes.set_yticks(np.linspace(self.m_yStart, self.m_yEnd, self.m_yStepNum))
            axes.set_ylim(self.m_yStart, self.m_yEnd * 1.005)
            axes.set_ylabel(self.m_yLabel)
        return
    
    def updateAxis(self):
        self.m_updateAxis = True
    
    def drawData(self, scanDataPara):
        if self.m_testScanData is None:
            self.m_testScanData = copy.deepcopy(scanDataPara)

        scanData = self.m_testScanData

        scanData = scanDataPara

        if self.m_aScanPlotterSet == None:
            self.m_aScanPlotterSet = []
            index = 0
            for axes in self.axesSet:
                scanPlotter, = axes.plot(scanData[index]['x'], scanData[index]['y'])
                self.m_aScanPlotterSet.append(scanPlotter)
                index += 1
        else:
            index = 0
            for scanPlotter in self.m_aScanPlotterSet:
                axes = self.axesSet[index]
                #axes.plot(scanData[index]['x'], scanData[index]['y'])
                scanPlotter.set_data(scanData[index]['x'], scanData[index]['y'])
                index += 1
        self.m_updateAxis = True
        if self.m_updateAxis:
            for axes in self.axesSet:
                axes.grid(True, linestyle = "-.")
            self.setXAxis()
            self.setYAxis()
            self.m_updateAxis = False
        self.draw()

    def drawGate(self, gateSet):
        colorStr = gateSet[0].m_color
        if self.m_gatePlotterSet[colorStr] is None:
            self.m_gatePlotterSet[colorStr] = []
            index = 0
            for gate in gateSet:
                if not gate.m_enabled:
                    datax = [gate.m_start]
                    datay = [gate.m_threshold]
                    continue
                else:
                    datax = [gate.m_start, gate.m_start + gate.m_len]
                    datay = [gate.m_threshold, gate.m_threshold]
                axes = self.axesSet[index]
                gatePlotter, = axes.plot(np.array(datax),  np.array(datay), colorStr)
                self.m_gatePlotterSet[colorStr].append(gatePlotter)
                index += 1
        else:
            index = 0
            for gatePlotter in self.m_gatePlotterSet[colorStr]:
                gate = gateSet[index]
                if not gate.m_enabled:
                    datax = [gate.m_start]
                    datay = [gate.m_threshold]
                    continue
                else:
                    datax = [gate.m_start, gate.m_start + gate.m_len]
                    datay = [gate.m_threshold, gate.m_threshold]
                axes = self.axesSet[index]
                #axes.plot(np.array(datax),  np.array(datay), colorStr)
                gatePlotter.set_data(np.array(datax),  np.array(datay))
                index += 1
        # self.m_updateAxis = True
        # if self.m_updateAxis:
        #     for axes in self.axesSet:
        #         axes.grid(True, linestyle = "-.")
        #     self.setXAxis()
        #     self.setYAxis()
        #     self.m_updateAxis = False
        return
#        self.axes.grid(True, linestyle = "-.")
#        self.setXAxis()
#        self.setYAxis()
#        self.draw()


class AScanWidgetMultiPlot(QWidget):
    def __init__(self,  parent = None):
        QWidget.__init__(self, parent)
        layout = QVBoxLayout()
        self.m_aScanCanvas = AScanMplCanvasMultiChano(self, 'Channe')
        #toolBar = NavToolbar(self.m_aScanCanvas, self) # only save button
        #layout.addWidget(toolBar)
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
    
    def updateAxis(self):
        self.m_aScanCanvas.updateAxis()

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
