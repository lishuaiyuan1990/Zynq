from PyQt4 import QtCore
from PyQt4 import QtGui
from ParaSetWidgetUi import ParaSetWidgetUi

class ParaSetWidget(ParaSetWidgetUi):
    def __init__(self, parent = None):
        super(ParaSetWidget, self).__init__(parent)
        self.configSignalAndSlot()
        #8 chan
        self.m_chanEnabled = 0xFF
        self.m_adDelay = 0
    
    def configSignalAndSlot(self):
        self.ui.m_sendParaBtn.clicked.connect(self.sendParaSlot)
        self.ui.m_startSysBtn.clicked.connect(self.startSys)
        self.ui.m_stopSysBtn.clicked.connect(self.stopSys)
        self.ui.m_openSysBtn.clicked.connect(self.openSys)
        self.ui.m_chanChecked.stateChanged.connect(self.setChanChecked)
        self.ui.m_chanNo.currentIndexChanged.connect(self.syncChanState)
        self.ui.m_gain.valueChanged.connect(self.setGain)
        self.ui.m_offset.valueChanged.connect(self.setOffset)
            
    def startSys(self):
        #start sys
        self.m_clientSocketTransObj.writePara(0x00030001)
        #create thread to read DMA
        self.m_clientSocketTransObj.writePara(97)
        #config DMA
        self.m_clientSocketTransObj.writePara(0x03000000)
    
    def stopSys(self):
        #stop sys
        self.m_clientSocketTransObj.writePara(0x00030000)
        self.closeSys()
    
    def setSocketTransObj(self,  socketTrans):
        self.m_clientSocketTransObj = socketTrans
    
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
        self.setSonicV()
        self.setOffset()
        self.setSampleLen()
        self.setRecvChanNo()
        self.setGainRangeNo()
    
    def writePara(self, handle, para = 0):
        chanNo = int(self.ui.m_chanNo.currentIndex())
        data = (handle << 24) + (chanNo << 16)  + int(para)
        print "writePara %0#8X" % data
        self.m_clientSocketTransObj.writePara(data)
    
    def closeSys(self):
        self.writePara(0x04, 0)

    def openSys(self):
        self.startSys()
        self.sendParaSlot()
        self.writePara(0x04, 1)
    
    def setTriggerMode(self):
        triggerMode = self.ui.m_triggerMode.currentIndex()
        self.writePara(0x05, triggerMode)
    
    def getPRFValue(self):
        prfList = [80, 160, 240, 400, 500, 1000, 2000, \
        4000, 5000, 8000, 10000, 16000]
        prfIndex = self.ui.m_prf.currentIndex()
        return prfList[prfIndex]

    def setPRF(self):
        prf = self.getPRFValue()
        prf /= 8
        data = int(10 ** 9 / prf / 200)
        print "data: ",  data
        self.writePara(0x06, data)
        
    def sendChanChecked(self):
        self.writePara(0x07, self.m_chanEnabled)
    
    def getEVoltageValue(self):
        eVoltageList = [500, 400, 300, 200, 100, 50]
        eVoltageIndex = self.ui.m_eVoltage.currentIndex()
        return eVoltageList[eVoltageIndex]
    
    def setEVoltage(self):
        eVoltage = self.getEVoltageValue()
        sendData = int(eVoltage * 51 / 80 / (2 ** 6))
        self.writePara(0x08, sendData)
    
    def setProbePrf(self):
        probePrf = self.ui.m_probePrf.value()
        sendData = int(1000 / probePrf / 5)
        self.writePara(0x09, sendData)
    
    def setGain(self):
        gain = self.ui.m_gain.value()
        sendData = ((100 - gain) / 200 + 1) * 2 ** 9
        self.writePara(0x0A, sendData)
    
    def setSonicPD(self):
        sonicPD = self.ui.m_sonicPD.value()
        self.writePara(0x0B,sonicPD)
    
    def setSonicV(self):
        sonicV = self.ui.m_sonicV.value()
        self.writePara(0x0C,sonicV)
    
    def setOffset(self):
        cycleTime = 100 #ns
        offset = int(self.ui.m_offset.value() * 1000 / cycleTime)
        self.writePara(0x0D,offset)
        self.m_adDelay = self.ui.m_offset.value()
    
    def getADDelay(self):
        return self.m_adDelay
    
    def setSampleLen(self):
        sampleLen = self.ui.m_sampleLen.value()
        self.writePara(0x0E,sampleLen)
    
    def setGainRangeNo(self):
        data = 0
        if self.ui.m_gain.value() > 39:
            data = 1
        self.writePara(0x0F, data)
        
    def setRecvChanNo(self):
        recvChanNo = self.ui.m_recvChanNo.currentIndex()
        self.writePara(0x10, recvChanNo)
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = ParaSetWidget()
    widget.show()
    sys.exit(app.exec_())
