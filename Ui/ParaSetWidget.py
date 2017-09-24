from PyQt4 import QtCore
from PyQt4 import QtGui
from ParaSetWidgetUi import ParaSetWidgetUi

class ParaSetWidget(ParaSetWidgetUi):
    def __init__(self, parent = None):
        super(ParaSetWidget, self).__init__(parent)
        self.configSignalAndSlot()
    
    def configSignalAndSlot(self):
        self.ui.m_sendParaBtn.clicked.connect(self.sendParaSlot)
        self.ui.m_startSysBtn.clicked.connect(self.startSys)
        self.ui.m_stopSysBtn.clicked.connect(self.stopSys)
    
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
    
    def setSocketTransObj(self,  socketTrans):
        self.m_clientSocketTransObj = socketTrans

            
    def sendParaSlot(self):
        self.setTriggerMode()
        self.setPRF()
        self.setChanChecked()
        self.setEVoltage()
        self.setBandWidth()
        self.setGain()
        self.setSonicPD()
        self.setSonicV()
        self.setOffset()
        self.setSampleLen()
        self.setRecvChanNo()
        self.setGainRangeNo()
    
    def writePara(self, handle, para = 0):
        chanNo = int(self.ui.m_chanNo.currentIndex())
        data = handle << 24 + chanNo << 16  + int(para)
        self.m_clientSocketTransObj.writePara(int(data))
    def openSys(self):
        self.writePara(0x04, 1)
    
    def setTriggerMode(self):
        triggerMode = self.ui.m_triggerMode.currentIndex()
        self.writePara(0x05, triggerMode)
    
    def setPRF(self):
        prf = self.ui.m_prf.value()
        self.writePara(0x06, prf)
        
    def setChanChecked(self):
        checked = self.ui.m_chanChecked.checkState()
        data = 0
        if checked == QtCore.Qt.Checked:
            data = 1
        else:
            data = 0
        self.writePara(0x07, data)
    
    def setEVoltage(self):
        eVoltage = self.ui.m_eVoltage.value()
        self.writePara(0x08,eVoltage)
    
    def setBandWidth(self):
        bandWidth = self.ui.m_bandWidth.value()
        self.writePara(0x09,bandWidth)
    
    def setGain(self):
        gain = self.ui.m_gain.value()
        self.writePara(0x0A,gain)
    
    def setSonicPD(self):
        sonicPD = self.ui.m_sonicPD.value()
        self.writePara(0x0B,sonicPD)
    
    def setSonicV(self):
        sonicV = self.ui.m_sonicV.value()
        self.writePara(0x0C,sonicV)
    
    def setOffset(self):
        offset = self.ui.m_offset.value()
        self.writePara(0x0D,offset)
    
    def setSampleLen(self):
        sampleLen = self.ui.m_sampleLen.value()
        self.writePara(0x0E,sampleLen)
    
    def setGainRangeNo(self):
        data = 0
        if self.ui.m_gainRange1Btn.isChecked():
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
