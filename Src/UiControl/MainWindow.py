from PyQt4 import QtCore
from PyQt4 import QtGui
import numpy as np
import threading
import struct
from Ui import MainWindowUi
from Src.TransLib import SocketTrans

IP = "192.168.1.10"
PORT = 6869

FrameLen = 1250 
FrameHead = 0xCCDD

class AScanData(object):
    def __init__(self, data):
        self.m_dmaData = data
        self.m_parseFrameInterval = 10
        self.parseAscanData()
    
    def iterateFrameData(self, startIndex = 0, endIndex = -1, frameStep = 1, typeSize = 4, cbBreak = None, cbIterate = None):
        if endIndex == -1:
            endIndex = len(self.m_dmaData)
        while(True):
            if startIndex + FrameLen * 4 >= endIndex:
                break
            dataTuple = struct.unpack("%dI" % (FrameLen * 4 / typeSize),  self.m_dmaData[startIndex : startIndex + FrameLen * 4])
            if cbIterate != None: 
                cbIterate(dataTuple)
            if cbBreak != None:
                for index, value in enumerate(dataTuple):
                    if cbBreak(value):
                        return startIndex + typeSize * index
            startIndex += FrameLen * 4 * frameStep
        return -1
    
    def isFrameHead(self, value):
        if (value >> 16) == FrameHead:
            if self.m_frameHeadNo > 3:
                return True
            self.m_frameHeadNo += 1
            return False
        else:
            return False
        
    def getFirstFrameHead(self):
        self.m_frameHeadNo = 1
        firstFrameHeadIndex = self.iterateFrameData(cbBreak = self.isFrameHead)
        return firstFrameHeadIndex
    
    def genAScanList(self, dataTuple):
        aScanList = []
        frameHead = dataTuple[0]
        frameData = dataTuple[1:]
        for index, value in enumerate(frameData):
            aScanList.append(value)
        self.m_parsedFrameDataList.append(aScanList)
        return aScanList
        
    def parseAscanData(self):
        self.m_parsedFrameDataList = []
        frameHeadIndex = self.getFirstFrameHead()
        if frameHeadIndex == -1:
            return self.m_parsedFrameDataList
        self.iterateFrameData(startIndex = frameHeadIndex, frameStep = 10, cbIterate = self.genAScanList)
        return self.m_parsedFrameDataList
    
    def getAScanList(self):
        return self.m_parsedFrameDataList
        
class MainWindow(MainWindowUi):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.m_clientSocketTransObj = SocketTrans(IP, PORT)
        self.ui.m_paraSetWidget.setSocketTransObj(self.m_clientSocketTransObj)
        self.m_startSys = False
        self.m_clockTimes = 1
        self.configSignalAndSlot()
        self.configAxis()
    
    def configSignalAndSlot(self):
        self.connect(self.ui.m_paraSetWidget.ui.m_startSysBtn,  QtCore.SIGNAL("clicked()"),\
        self.createThreadToRecvData)
        self.connect(self.ui.m_paraSetWidget.ui.m_stopSysBtn,  QtCore.SIGNAL("clicked()"),\
        self.stopRecvDataThread)
    
    def stopRecvDataThread(self):
        if self.m_startSys:
            self.m_timerThread.cancel()
            self.m_startSys = False 
        return
    
    def createThreadToRecvData(self):
        self.m_startSys = True
        self.m_recvInterval = 1
        self.m_timerThread = threading.Timer(self.m_recvInterval, self.recvScanData)
        self.m_timerThread.start()
        self.m_drawDone = True
        self.m_stopDraw = False
    
    def parseFrameDataAndDraw(self, data):
        aScanDataObj = AScanData(data)
        aScanDataList = aScanDataObj.getAScanList()
        drawClock = 0
        drawInterval = self.m_recvInterval / len(aScanDataList)
        drawInterval = 0.5        
        self.m_drawThread = threading.Timer(drawInterval, self.drawAScanData, [aScanDataList, drawClock, drawInterval, True])
        self.m_drawThread.start()
        return
    
    def drawAScanData(self, dataList, drawClock, drawInterval, firstTime = False):
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
        scanData['y'] = data
        scanData['x'] = np.linspace(0, FrameLen - 1, len(data))
        self.configAxis()
        self.ui.m_aScanWidget.drawData(scanData)
        drawClock += 1
        if drawClock >= len(dataList) or self.m_stopDraw:
            self.m_stopDraw = False
            self.m_drawDone = True
            return
        self.m_drawThread = threading.Timer(drawInterval, self.drawAScanData, [dataList, drawClock, drawInterval])
        self.m_drawThread.start()
        
    def recvScanData(self):
        max_pkg_len = 450000 * 4
        data = self.m_clientSocketTransObj.recvData(max_pkg_len)
        self.m_parseThread = threading.Timer(0.1, self.parseFrameDataAndDraw, [data])
        self.m_parseThread.start()
        
        file = open("text_%d" % self.m_clockTimes, 'wb')
        file.write(data)
        file.close()
        #one page read done
        self.m_clientSocketTransObj.writePara(0xDDDD)
        self.m_clockTimes += 1
        if self.m_startSys:
            self.createThreadToRecvData()
    
    def configAxis(self):
        self.ui.m_aScanWidget.configXAxis(0, FrameLen, 10, "us")
        self.ui.m_aScanWidget.configYAxis(0, 1250, 10, "%")
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())