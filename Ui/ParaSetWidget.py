from PyQt4 import QtCore
from PyQt4 import QtGui
from ParaSetWidgetUi import ParaSetWidgetUi
from Src.ScanData import Gate
class ParaSetWidget(ParaSetWidgetUi):
    def __init__(self, parent = None):
        super(ParaSetWidget, self).__init__(parent)
        self.configSignalAndSlot()
        self.m_gateProcesser = GateProcess(self.ui)
        #8 chan
        self.m_chanEnabled = 0xFF
        self.m_offset = 20
        self.m_haveSendPara = False
    
    def configSignalAndSlot(self):
        self.ui.m_stopSysBtn.clicked.connect(self.stopSys)
        self.ui.m_openSysBtn.clicked.connect(self.openSys)
        self.ui.m_chanChecked.stateChanged.connect(self.setChanChecked)
        self.ui.m_chanNo.currentIndexChanged.connect(self.syncChanState)
        self.ui.m_eVoltage.currentIndexChanged.connect(self.setEVoltage)
        self.ui.m_prf.currentIndexChanged.connect(self.setPRF)
        self.ui.m_gain.editingFinished.connect(self.setGain)
        self.ui.m_offset.editingFinished.connect(self.setOffset)
        self.ui.m_recvChanNo.currentIndexChanged.connect(self.setRecvChanNo)
        self.ui.m_probePrf.editingFinished.connect(self.setProbePrf)
        self.ui.m_sampleLen.editingFinished.connect(self.setSampleLen)
        self.ui.m_sampleLen.editingFinished.connect(self.setCompressRatio)
        self.ui.m_sonicPD.editingFinished.connect(self.setCompressRatio)
        self.ui.m_sonicV.editingFinished.connect(self.setSonicV)
        
            
    def startSys(self):
        #start sys
        self.m_clientSocketTransObj.writePara(0x00030001)
        #create thread to read DMA
        self.m_clientSocketTransObj.writePara(97)
        #config DMA
        #self.m_clientSocketTransObj.writePara(0x03000000)
    
    def stopSys(self):
        #stop sys
        #self.writePara(0x03, 0)
        self.ui.m_openSysBtn.setEnabled(True)
        self.ui.m_stopSysBtn.setEnabled(False)
        self.closeSys()
    
    def closeSys(self):
        self.writePara(0x04, 0)

    def openSys(self):
        self.ui.m_openSysBtn.setEnabled(False)
        self.ui.m_stopSysBtn.setEnabled(True)
        if not self.m_haveSendPara:
            self.startSys()
            self.sendParaSlot()
            self.writePara(0x04, 1)
        else:
            self.reStartSys()
    
    def reStartSys(self):
        #self.writePara(0x03, 1)
        self.writePara(0x04, 1)
    
    def setSocketTransObj(self,  socketTrans):
        self.m_clientSocketTransObj = socketTrans
    
    def getSonicPD(self):
        return self.ui.m_sonicPD.value()
    
    def syncChanState(self):
        chan = self.ui.m_chanNo.currentIndex()
        data = (1 << chan)
        enabled = data & self.m_chanEnabled
        self.ui.m_chanChecked.setChecked(enabled)
        
    def setChanChecked(self):
        checked = self.ui.m_chanChecked.checkState()
        chan = self.ui.m_chanNo.currentIndex()
        data = 0
        if checked == QtCore.Qt.Checked:
            data = 1 << chan
            self.m_chanEnabled = self.m_chanEnabled | data
        else:
            data = ~(1 << chan)
            self.m_chanEnabled = self.m_chanEnabled & data
        return
        
    def sendParaSlot(self):
        #self.setTriggerMode()
        self.setPRF()
        self.sendChanChecked()
        self.setEVoltage()
        self.setProbePrf()
        self.setGain()
        self.setSonicPD()
        self.setOffset()
        self.setSampleLen()
        self.setRecvChanNo()
        self.setCompressRatio()
        #self.setGainRangeNo()
        self.m_haveSendPara = True
    
    def writePara(self, handle, para = 0):
        chanNo = int(self.ui.m_chanNo.currentIndex())
        data = (handle << 24) + (chanNo << 16)  + int(para)
        print "writePara %0#8X" % data
        self.m_clientSocketTransObj.writePara(data)
    
    def setTriggerMode(self):
        triggerMode = self.ui.m_triggerMode.currentIndex()
        self.writePara(0x05, triggerMode)
    
    def getPRFValue(self):
        prfList = [80, 160, 240, 400, 500, 1000, 2000, \
        4000, 5000, 8000, 10000, 16000]
        prfIndex = self.ui.m_prf.currentIndex()
        return prfList[prfIndex]
    
    def getChanNum(self):
        chanSum = 16
        chanNum = 0
        for i in range(0, chanSum):
            if self.m_chanEnabled & (1 << i):
                chanNum += 1
        chanNum = min(chanNum, 1)
        return chanNum

    def setPRF(self):
        prf = self.getPRFValue()
        prf /= self.getChanNum()
        data = int(10 ** 9 / prf / 200)
        self.writePara(0x06, data)
        
    def sendChanChecked(self):
        self.writePara(0x07, self.m_chanEnabled)
    
    def getEVoltageValue(self):
        eVoltageList = [400, 300, 200, 100, 50]
        eVoltageIndex = self.ui.m_eVoltage.currentIndex()
        return eVoltageList[eVoltageIndex]
    
    def setEVoltage(self):
        eVoltage = self.getEVoltageValue()
        sendData = int((eVoltage * 256.0 / 400.0 - 1) * (2 ** 6))
        self.writePara(0x08, sendData)
    
    def setProbePrf(self):
        probePrf = self.ui.m_probePrf.value()
        sendData = int(1000 / probePrf / 5)
        self.writePara(0x09, sendData)
    
    def setGain(self):
        gain = self.ui.m_gain.value()
        #sendData = ((100 - gain) / 200 + 1) * 2 ** 9
        #sendData = (gain + 6.5) * 1024 / (50 * 1.3046)
        if gain <= 39.7:
            sendData = (((gain + 20 + 12.4) / 2.0) + 6.5) * 1024.0 / (50 * 1.304) 
        else:
            sendData = (((gain + 20 - 23.9 + 3.5) / 2.0) + 6.5) * 1024.0 / (50 * 1.304) 
        self.writePara(0x0A, sendData)
        self.setGainRangeNo()
    
    def setSonicPD(self):
        sonicPD = self.ui.m_sonicPD.value()
        self.writePara(0x0B,sonicPD)
    
    def setCompressRatio(self):
        sampleFreq = 100
        ad_length = self.ui.m_sonicPD.value() / self.ui.m_sonicV.value() * 1000 * sampleFreq
        sampleLen = self.ui.m_sampleLen.value()
        compressRatio = max(ad_length / sampleLen, 1)
        self.writePara(0x11,compressRatio)
        
    def setSonicV(self):
        #sonicV = self.ui.m_sonicV.value()
        #self.writePara(0x0C,sonicV)
        self.setCompressRatio()
        self.setOffset()
    
    def getSonicV(self):
        #m/s
        sonicV = self.ui.m_sonicV.value()
        return sonicV
    
    def setOffset(self):
        cycleTime = 10 #ns
        #1000 * m/s -> mm/us
        adDelay = int(self.ui.m_offset.value() * 1000 / self.ui.m_sonicV.value())
        sendData = int(adDelay * 1000 / cycleTime)
        self.writePara(0x0D, sendData)
        self.m_offset = self.ui.m_offset.value()
    
    def getOffset(self):
        return self.m_offset
    
    def setSampleLen(self):
        sampleLen = self.ui.m_sampleLen.value()
        sendData = sampleLen# / 2
        self.writePara(0x0E, sendData)
    
    def setGainRangeNo(self):
        data = 1
        if self.ui.m_gain.value() > 39.7:
            data = 0
        self.writePara(0x0F, data)
    
    def getRecvSendData(self):
        sendRecvChanList = [0, 1, 2, 3, 4, 6, 7, 5]
        recvChanNo = self.ui.m_recvChanNo.currentIndex()
        return sendRecvChanList[recvChanNo]
        
    def setRecvChanNo(self):
        recvChanNo = self.getRecvSendData()
        self.writePara(0x10, recvChanNo)
    
    def getGate1(self):
        return self.m_gateProcesser.getGate1()
    
    def getGate2(self):
        return self.m_gateProcesser.getGate2() 

class GateProcess(QtCore.QObject):
    gateUpdated = QtCore.pyqtSignal()
    def __init__(self, ui):
        super(GateProcess, self).__init__()
        self.ui = ui
        self.configSignalAndSlot()
        self.initGate1()
        self.initGate2()
    
    def getGate1(self):
        return self.m_gate1
    
    def getGate2(self):
        return self.m_gate2
    
    def configSignalAndSlot(self):
        self.ui.m_gate1Checked.stateChanged.connect(self.updateGate1)
        self.ui.m_gate1Start.valueChanged.connect(self.updateGate1)
        self.ui.m_gate1Len.valueChanged.connect(self.updateGate1)
        self.ui.m_gate1Threshold.valueChanged.connect(self.updateGate1)
        
        self.ui.m_gate2Checked.stateChanged.connect(self.updateGate2)
        self.ui.m_gate2Start.valueChanged.connect(self.updateGate2)
        self.ui.m_gate2Len.valueChanged.connect(self.updateGate2)
        self.ui.m_gate2Threshold.valueChanged.connect(self.updateGate2)

    def initGate1(self):
        color = "#FF0000"
        checked = self.ui.m_gate1Checked.checkState()
        enabled = False
        if checked == QtCore.Qt.Checked:
            enabled = True
        start = self.ui.m_gate1Start.value()
        len   = self.ui.m_gate1Len.value()
        threshold = self.ui.m_gate1Threshold.value()
        self.m_gate1 = Gate(start, len, threshold, enabled, color)
        self.gateUpdated.emit()
    
    def updateGate1(self):
        checked = self.ui.m_gate1Checked.checkState()
        enabled = False
        if checked == QtCore.Qt.Checked:
            enabled = True
        start = self.ui.m_gate1Start.value()
        len   = self.ui.m_gate1Len.value()
        threshold = self.ui.m_gate1Threshold.value()
        self.m_gate1.setStart(start)
        self.m_gate1.setLen(len)
        self.m_gate1.setThreshold(threshold)
        self.m_gate1.setEnabled(enabled)
        self.gateUpdated.emit()
    
    def initGate2(self):
        color = "#00FF00"
        checked = self.ui.m_gate2Checked.checkState()
        enabled = False
        if checked == QtCore.Qt.Checked:
            enabled = True
        start = self.ui.m_gate2Start.value()
        len   = self.ui.m_gate2Len.value()
        threshold = self.ui.m_gate2Threshold.value()
        self.m_gate2 = Gate(start, len, threshold, enabled, color)
        self.gateUpdated.emit()
    
    def updateGate2(self):
        checked = self.ui.m_gate2Checked.checkState()
        enabled = False
        if checked == QtCore.Qt.Checked:
            enabled = True
        start = self.ui.m_gate2Start.value()
        len   = self.ui.m_gate2Len.value()
        threshold = self.ui.m_gate2Threshold.value()
        self.m_gate2.setStart(start)
        self.m_gate2.setLen(len)
        self.m_gate2.setThreshold(threshold)
        self.m_gate2.setEnabled(enabled)
        self.gateUpdated.emit()
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = ParaSetWidget()
    widget.show()
    sys.exit(app.exec_())
