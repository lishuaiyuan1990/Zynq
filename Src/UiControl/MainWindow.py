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

import time

IP = "192.168.1.10"
PORT = 6869

FrameLen = 1250 
FrameHead = 0xCCDD      

class MainWindow(MainWindowUi):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        #self.setWindowFlags(self.windowFlags()& ~QtCore.Qt.WindowMaximizeButtonHint)
        #self.setFixedSize(self.width(), self.height())
        
        self.m_clientSocketTransObj = SocketTrans(IP, PORT)
        self.ui.m_paraSetWidget.setSocketTransObj(self.m_clientSocketTransObj)
        self.m_startSys = False
        self.m_clockTimes = 0
        self.m_isDrawing = False
        self.setSonicPara()
        self.configSignalAndSlot()
        self.updateAxis()
        self.configAxis()
            
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
        self.m_gateList = self.ui.m_parseToolWidget.getGateListByChano()
        #self.m_gate2 = self.ui.m_parseToolWidget.getGate2()
    
    def updateAxis(self):
        self.m_offset = self.ui.m_paraSetWidget.getOffset()
        self.m_sonicPD = self.ui.m_paraSetWidget.getSonicPD()
        self.ui.m_aScanWidget.updateAxis()
        
    def getXAxisRange(self):
        self.setSonicPara()
        range = {}
        range['start'] = self.m_offset
        range['end'] = self.m_offset + self.m_sonicPD
        range['num'] = self.ui.m_paraSetWidget.getSampleLen() - 1
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
        self.m_recvInterval = 0.2
        self.m_timerThread = threading.Timer(self.m_recvInterval, self.recvScanData)
        self.m_timerThread.start()
        self.m_drawDone = True
        self.m_stopDraw = False
    
    def parseFrameDataAndDraw(self, data):
        aScanDataObj = AScanData(data)

        detectionModeByChan = self.ui.m_parseToolWidget.getDetectionModeByChan()
        index = 0
        dynaGainObjByChano = []
        for detectionMode in detectionModeByChan:
            chanNo = index
            dynaGainObj = self.parseDynaGain(chanNo)
            dynaGainObjByChano.append(dynaGainObj)
            index += 1

        
        #print "parseFrameDataAndDraw chanNo ",chanNo
        aScanDataList = aScanDataObj.getAScanListByChano(detectionModeByChan, dynaGainObjByChano)

        chanNum = len(aScanDataList)
        if chanNum <= 0:
            return

        aScanLen = len(aScanDataList[0])
        if aScanLen <= 0:
            return
        aScanDataListByChanNo = self.transScanDataListByChanNo(aScanDataList)



        drawClock = 0
        drawInterval = 1.0 * self.m_recvInterval / len(aScanDataListByChanNo)
        self.m_drawThread = threading.Timer(drawInterval, self.drawAScanData, [aScanDataListByChanNo, drawClock, drawInterval, True])
        self.m_drawThread.start()
        return

    def transScanDataListByChanNo(self, arr):
        retArr = []
        index = 0
        for r in range(0, len(arr[0])):
            retArr.append([])
            for i in range(0, len(arr)):
                retArr[r].append(arr[i][r])
        return retArr

    def parseDynaGain(self, chanNo):
        dynaGainObj = self.ui.m_parseToolWidget.getDynaGain(chanNo)
        gate = dynaGainObj['gate']
        gain = dynaGainObj['gain']
        scanRange = self.getXAxisRange()
        
        length = scanRange['end'] - scanRange['start']
        startOffset = min(max((gate.m_start - scanRange['start']) / length, 0), 1)
        endOffset   = min(max((gate.m_start + gate.m_len - scanRange['start']) / length, 0), 1)
        num = scanRange['num']
        dynaGainRange = {'start': int(round(startOffset * num)), 'end': int(round(endOffset * num))}
        return {'gain': gain, 'dynaGainRange' : dynaGainRange}

    def drawGate(self):
        gateListByColor = []
        for r in range(0, len(self.m_gateList[0])):
            gateListByColor.append([])
            for i in range(0, len(self.m_gateList)):
                gateListByColor[r].append(self.m_gateList[i][r])

        for gate in gateListByColor:
            self.ui.m_aScanWidget.drawGate(gate)
        return
    
    def drawAScanData(self, dataList, drawClock, drawInterval, firstTime = False):
        if not self.m_startSys:
            return        
        if drawClock >= len(dataList):
            return
        data = dataList[drawClock]

        scanDataList = []
        scanRange = self.getXAxisRange()
        for d in data:
            scanData = {}
            scanData['y'] = copy.deepcopy(d)
            scanData['x'] = np.linspace(scanRange['start'], scanRange['end'], len(data[0]))
            scanDataList.append(scanData)
        if not self.m_isDrawing:
            self.m_isDrawing = True
            self.configAxis()
            self.drawGate()
            self.ui.m_aScanWidget.drawData(scanDataList)
            self.m_isDrawing = False
        else:
            print "conflict...", self.m_clockTimes
        drawClock += 1
        self.m_drawThread = threading.Timer(drawInterval, self.drawAScanData, [dataList, drawClock, drawInterval])
        self.m_drawThread.start()
        
    def recvScanData(self):
        max_pkg_len = 50000
        try:
            data = self.m_clientSocketTransObj.recvData(max_pkg_len)
        except:
            return
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
