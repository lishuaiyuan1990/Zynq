from PyQt4 import QtCore
from PyQt4 import QtGui
import numpy as np
import threading
import copy
import os
import datetime
from Ui import MainWindowUi
from Src.TransLib import SocketTrans
from Src.ScanData import AScanData, Gate

IP = "192.168.1.10"
PORT = 6869

FrameLen = 1250 
FrameHead = 0xCCDD      

class MainWindow(MainWindowUi):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(self.windowFlags()& ~QtCore.Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        
        self.m_clientSocketTransObj = SocketTrans(IP, PORT)
        self.ui.m_paraSetWidget.setSocketTransObj(self.m_clientSocketTransObj)
        self.m_startSys = False
        self.m_clockTimes = 0
        self.setSonicPara()
        self.configSignalAndSlot()
        self.updateAxis()
        self.configAxis()
        self.mainUpdate()
    
    def mainUpdate(self):
        #sendNum = self.m_clientSocketTransObj.writePara(0xFFFF)
        #print "sendNum: ",  sendNum 
        timerThread = threading.Timer(1.0, self.mainUpdate)
        timerThread.start()
        
    def configSignalAndSlot(self):
        self.connect(self.ui.m_paraSetWidget.ui.m_openSysBtn,  QtCore.SIGNAL("clicked()"),\
        self.createThreadToRecvData)
        self.connect(self.ui.m_paraSetWidget.ui.m_openSysBtn,  QtCore.SIGNAL("clicked()"),\
        self.setSonicPara)
        self.connect(self.ui.m_paraSetWidget.ui.m_stopSysBtn,  QtCore.SIGNAL("clicked()"),\
        self.stopRecvDataThread)
        self.connect(self.ui.m_paraSetWidget.ui.m_sonicPD,  QtCore.SIGNAL('editingFinished()'), \
        self.updateAxis)
        self.connect(self.ui.m_paraSetWidget.ui.m_offset,  QtCore.SIGNAL('editingFinished()'), \
        self.updateAxis)
        #self.connect(self.ui.m_paraSetWidget.m_gateProcesser, QtCore.SIGNAL("gateUpdated()"), \
        #self.drawGate)
    #stop sys
    def closeEvent(self, event):
        self.ui.m_paraSetWidget.stopSys()
        
    def setSonicPara(self):
        self.m_AScanLen = (FrameLen - 1) * 2
        self.m_sampleFreq = 100
        #mm/us
        #self.m_sonicV = self.ui.m_paraSetWidget.getSonicV() / 1000
        self.m_gate1 = self.ui.m_paraSetWidget.getGate1()
        self.m_gate2 = self.ui.m_paraSetWidget.getGate2()
    
    def updateAxis(self):
        self.m_offset = self.ui.m_paraSetWidget.getOffset()
        self.m_sonicPD = self.ui.m_paraSetWidget.getSonicPD()
        self.ui.m_aScanWidget.updateAxis()
        
    def getXAxisRange(self):
        self.setSonicPara()
        range = {}
        range['start'] = self.m_offset
        range['end'] = self.m_offset + self.m_sonicPD
        #sampleTime = 1.0 / self.m_sampleFreq
        #range['end'] = self.m_offset + sampleTime * self.m_AScanLen * self.m_sonicV
        return range
    
    def stopRecvDataThread(self):
        if self.m_startSys:
            self.m_timerThread.cancel()
            self.m_startSys = False 
        return
    
    #main thread
    def createThreadToRecvData(self):
        self.m_startSys = True
        self.m_recvInterval = 0.1
        self.m_timerThread = threading.Timer(self.m_recvInterval, self.recvScanData)
        self.m_timerThread.start()
        self.m_drawDone = True
        self.m_stopDraw = False
    
    def parseFrameDataAndDraw(self, data):
        aScanDataObj = AScanData(data)
        chanNo = 0
        aScanDataList = aScanDataObj.getAScanList(chanNo)
        if len(aScanDataList) <= 0:
            return
        drawClock = 0
        drawInterval = 1.0 * self.m_recvInterval / len(aScanDataList)
        self.m_drawThread = threading.Timer(drawInterval, self.drawAScanData, [aScanDataList, drawClock, drawInterval, True])
        self.m_drawThread.start()
        return
    
    def drawGate(self):
        self.ui.m_aScanWidget.drawGate(self.m_gate1)
        self.ui.m_aScanWidget.drawGate(self.m_gate2)
    
    def drawAScanData(self, dataList, drawClock, drawInterval, firstTime = False):
        if not self.m_startSys:
            return
        if firstTime and not self.m_drawDone:
            self.m_stopDraw = True
            self.m_drawThread = threading.Timer(drawInterval, self.drawAScanData, [dataList, drawClock, drawInterval, True])
            self.m_drawThread.start()
            return
        self.m_drawDone = False
        if drawClock >= len(dataList) or self.m_stopDraw:
            self.m_stopDraw = False
            self.m_drawDone = True
            return
        data = dataList[drawClock]
        scanData = {}
        scanData['y'] = copy.deepcopy(data)
        scanRange = self.getXAxisRange()
        scanData['x'] = np.linspace(scanRange['start'], scanRange['end'], len(data))
        self.configAxis()
        self.drawGate()
        self.ui.m_aScanWidget.drawData(scanData)
        drawClock += 1
        if drawClock >= len(dataList) or self.m_stopDraw:
            self.m_stopDraw = False
            self.m_drawDone = True
            return
        self.m_drawThread = threading.Timer(drawInterval, self.drawAScanData, [dataList, drawClock, drawInterval])
        self.m_drawThread.start()
        
    def recvScanData(self):
        max_pkg_len = 50000
        data = self.m_clientSocketTransObj.recvData(max_pkg_len)
        self.parseFrameDataAndDraw(data)

        #one page read done
        self.m_clientSocketTransObj.writePara(0xDDDD)
        self.m_clockTimes += 1
        if self.m_startSys:
            self.saveScanDataToFile(data)
            self.createThreadToRecvData()
        return
    #append data to file
    def saveScanDataToFile(self, data):
        fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        dataPath = "./dmaData"
        if not os.path.exists(dataPath):
            os.makedirs(dataPath)
        file = open("%s/%s" % (dataPath, fileName), 'wb+')
        file.write(data)
        file.close()
        
    
    def configAxis(self):        
        scanRange = self.getXAxisRange()
        self.ui.m_aScanWidget.configXAxis(scanRange['start'], scanRange['end'], 10, "mm")
        self.ui.m_aScanWidget.configYAxis(0, 100, 11, "Amp")
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
