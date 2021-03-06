from PyQt4 import QtCore
from PyQt4 import QtGui
from ParaSetWidgetUi import ParaSetWidgetUi
from Src.ScanData import Gate

import json

class ParaSetWidget(ParaSetWidgetUi):
    def __init__(self, parent = None):
        super(ParaSetWidget, self).__init__(parent)
        self.configSignalAndSlot()
        #8 chan
        self.m_chanEnabled = 0xFF
        self.m_offset = 20
        self.m_haveSendPara = False
        self.m_sampleLenValue = self.ui.m_sampleLen.value()
    
    def configSignalAndSlot(self):
        self.ui.m_stopSysBtn.clicked.connect(self.stopSys)
        self.ui.m_openSysBtn.clicked.connect(self.openSys)
        self.ui.m_saveSettingBtn.clicked.connect(self.saveSettings)
        self.ui.m_openSettingBtn.clicked.connect(self.openSettings)
        self.ui.m_chanChecked.stateChanged.connect(self.setChanChecked)
        self.ui.m_chanNo.currentIndexChanged.connect(self.syncChanState)
        self.ui.m_eVoltage.currentIndexChanged.connect(self.setEVoltage)
        self.ui.m_prf.currentIndexChanged.connect(self.setPRF)
        self.ui.m_gain.editingFinished.connect(self.setGain)
        self.ui.m_offset.editingFinished.connect(self.setOffset)
        self.ui.m_probePrf.editingFinished.connect(self.setProbePrf)
        self.ui.m_sampleLen.editingFinished.connect(self.setSampleLen)
        self.ui.m_sampleLen.editingFinished.connect(self.setCompressRatio)
        self.ui.m_sonicPD.editingFinished.connect(self.setCompressRatio)
        self.ui.m_sonicV.editingFinished.connect(self.setSonicV)

    def saveSettings(self):
        fileName2 = QtGui.QFileDialog.getSaveFileName(self,  "Save", "./",  "Settings Files (*.json)")
        if len(fileName2) <= 0:
            return
        fileObj = open(fileName2, 'w')
        jsonStr = json.dumps(self.settings())
        fileObj.write(jsonStr)
        fileObj.close()


    def openSettings(self):
        fileName2 = QtGui.QFileDialog.getOpenFileName(self,  "Open", "./",  "Settings Files (*.json)")
        if len(fileName2) <= 0:
            return
        fileObj = open(fileName2, 'r')
        jsonStr = fileObj.read()
        fileObj.close()
        settingsObj = json.loads(jsonStr)
        self.configSettings(settingsObj)


    def settings(self):
        settingsObj = {}
        settingsObj['chanEnabled'] = self.m_chanEnabled
        settingsObj['eVoltageIndex'] = self.ui.m_eVoltage.currentIndex()
        settingsObj['sonicPD'] = self.ui.m_sonicPD.value()
        settingsObj['sonicV'] = self.ui.m_sonicV.value()
        settingsObj['sampleLen'] = self.ui.m_sampleLen.value()
        settingsObj['gain'] = self.ui.m_gain.value()
        settingsObj['prfIndex'] = self.ui.m_prf.currentIndex()
        settingsObj['probePrf'] = self.ui.m_probePrf.value()
        settingsObj['offset'] = self.ui.m_offset.value()
        return settingsObj

    def configSettings(self, settingsObj):
        self.m_chanEnabled = settingsObj['chanEnabled']
        self.syncChanState()
        self.ui.m_eVoltage.setCurrentIndex(settingsObj['eVoltageIndex'])
        self.ui.m_prf.setCurrentIndex(settingsObj['prfIndex'])
        self.ui.m_sonicPD.setValue(settingsObj['sonicPD'])
        self.ui.m_sonicV.setValue(settingsObj['sonicV'])
        self.ui.m_sampleLen.setValue(settingsObj['sampleLen'])
        self.ui.m_gain.setValue(settingsObj['gain'])
        self.ui.m_probePrf.setValue(settingsObj['probePrf'])
        self.ui.m_offset.setValue(settingsObj['offset'])
            
    def startSys(self):
        #start sys
        #self.m_clientSocketTransObj.writePara(0x00030001)
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
        self.m_clientSocketTransObj.writePara(97)
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
        self.sendChanChecked()
        self.setPRF()
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
        self.setCompressRatio()
        #self.setGainRangeNo()
        self.m_haveSendPara = True
    
    def writePara(self, handle, para = 0):
        data = (handle << 24)   + int(para)
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
        #chanNum = min(chanNum, 1)
        return chanNum

    def setPRF(self):
        chanNum = self.getChanNum()
        print "chanNum", chanNum
        if chanNum <= 0:
            return
        prf = self.getPRFValue()
        prf /= chanNum
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
        self.m_sampleLenValue = sampleLen
        sendData = sampleLen# / 2
        self.writePara(0x0E, sendData)

    def getSampleLen(self):
        return self.m_sampleLenValue
    
    def setGainRangeNo(self):
        data = 1
        if self.ui.m_gain.value() > 39.7:
            data = 0
        self.writePara(0x0F, data)
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = ParaSetWidget()
    widget.show()
    sys.exit(app.exec_())
