from PyQt4 import QtCore
from PyQt4 import QtGui
from ParseToolWidgetUi import ParseToolWidgetUi
from Src.ScanData import Gate
class ParseToolWidget(ParseToolWidgetUi):
    def __init__(self, parent = None):
        super(ParseToolWidget, self).__init__(parent)
        self.m_chanNoNum = 8
        self.m_lockList = [False]
        self.m_gateProcesser = GateProcess(self.ui, self.m_chanNoNum, self.m_lockList)
        self.initUiData()
        self.configSignalAndSlot()
    
    def initUiData(self):
        self.m_detectionModeByChano = []
        for chanNo in range(0, self.m_chanNoNum):
            self.m_detectionModeByChano.append(self.getCurrentDetectionMode())
        return

    def configSignalAndSlot(self):
        self.ui.m_chanNo.currentIndexChanged.connect(self.updateUi)
        self.ui.m_detectionMode.currentIndexChanged.connect(self.updateUiData)


    def updateUiData(self):
        chanNo = self.ui.m_chanNo.currentIndex()
        self.m_detectionModeByChano[chanNo] = self.ui.m_detectionMode.currentIndex()

    def updateUi(self):
        self.m_lockList[0] = True
        chanNo = self.ui.m_chanNo.currentIndex()
        detectionMode = self.m_detectionModeByChano[chanNo]
        self.ui.m_detectionMode.setCurrentIndex(detectionMode)

        self.m_currentGateList = self.getGateList(chanNo)
        self.m_gateProcesser.iterateGateUiList(self.updateGateUi)
        self.m_lockList[0] = False


    def updateGateUi(self, gateUi, index):
        gateList = self.m_currentGateList
        gateUi['start'].setValue(gateList[index].m_start)
        gateUi['length'].setValue(gateList[index].m_len)
        gateUi['threshold'].setValue(gateList[index].m_threshold)
        if gateUi['gain'] != None:
            gateUi['gain'].setValue(gateList[index].m_gain)
        gateUi['checked'].setChecked(gateList[index].m_enabled)


    def getGateList(self, chanNo = 0):
        return self.m_gateProcesser.getGateList(chanNo)

    def getGateListByChano(self):
        return self.m_gateProcesser.getGateListByChano()
        
    def getChanNo(self):
        chan = self.ui.m_chanNo.currentIndex()
        return chan

    def getDetectionModeByChan(self):
        return self.m_detectionModeByChano
        
    def getCurrentDetectionMode(self):
        detectionMode = self.ui.m_detectionMode.currentIndex()
        return detectionMode
    
    def getDynaGain(self, chanNo):
        dynaGate = self.m_gateProcesser.getDynaGate(chanNo)
        dynaGain = 0
        if dynaGate.m_enabled:
            dynaGain = dynaGate.m_gain
        return {'gate': dynaGate, 'gain': dynaGain}



        
class GateProcess(QtCore.QObject):
    gateUpdated = QtCore.pyqtSignal()
    def __init__(self, ui, chanNoNum, lockList):
        super(GateProcess, self).__init__()
        self.ui = ui
        self.m_chanNoNum = chanNoNum
        self.m_lockList = lockList
        self.genGateUiList()
        self.configSignalAndSlot()
        self.initGate()
    
    def genGateUiList(self):
        gate1Ui = {'checked': self.ui.m_gate1Checked, 'start': self.ui.m_gate1Start,  \
        'length': self.ui.m_gate1Len, 'threshold': self.ui.m_gate1Threshold, 'color': "#FF0000", 'gain': None}
        gate2Ui = {'checked': self.ui.m_gate2Checked, 'start': self.ui.m_gate2Start,  \
        'length': self.ui.m_gate2Len, 'threshold': self.ui.m_gate2Threshold, 'color': "#00FF00", 'gain': None}
        gate3Ui = {'checked': self.ui.m_gate3Checked, 'start': self.ui.m_gate3Start,  \
        'length': self.ui.m_gate3Len, 'threshold': self.ui.m_gate3Threshold, 'color': "#0000FF", 'gain': None}
        gate4Ui = {'checked': self.ui.m_gate4Checked, 'start': self.ui.m_gate4Start,  \
        'length': self.ui.m_gate4Len, 'threshold': self.ui.m_gate4Threshold, 'color': "#00FFFF", 'gain': self.ui.m_gateGain}
        self.m_gateUiList = [gate1Ui, gate2Ui, gate3Ui, gate4Ui]
    
    def getDynaGate(self, chanNo):
        length = len(self.m_gateListByChaNo[chanNo])
        return self.m_gateListByChaNo[chanNo][length - 1] 

    def getGateList(self, chanNo):
        return self.m_gateListByChaNo[chanNo]

    def getGateListByChano(self):
        return self.m_gateListByChaNo

    def iterateGateUiList(self, callback):
        for index, gateUi in enumerate(self.m_gateUiList):
            callback(gateUi, index)
        return
    
    def configSignalAndSlot(self):
        for gateUi in self.m_gateUiList:
            gateUi['checked'].stateChanged.connect(self.updateGate)
            gateUi['start'].editingFinished.connect(self.updateGate)
            gateUi['length'].editingFinished.connect(self.updateGate)
            gateUi['threshold'].editingFinished.connect(self.updateGate)
            if gateUi['gain'] != None:
                gateUi['gain'].editingFinished.connect(self.updateGate)
        return
    
    def initGate(self):
        self.m_gateListByChaNo = []
        for chanNo in range(0, self.m_chanNoNum):
            gateList = []
            for gateUi in self.m_gateUiList:
                checked = gateUi['checked'].checkState()
                enabled = False
                if checked == QtCore.Qt.Checked:
                    enabled = True
                start = gateUi['start'].value()
                length   = gateUi['length'].value()
                threshold = gateUi['threshold'].value()
                gain = 0
                if gateUi['gain'] != None:
                    gain = gateUi['gain'].value()
                color = gateUi['color']
                gate = Gate(start, length, threshold, enabled, color, gain)
                gateList.append(gate)
            self.m_gateListByChaNo.append(gateList)
        self.gateUpdated.emit()


    def updateGate(self):
        if self.m_lockList[0]:
            return
        chanNo = self.ui.m_chanNo.currentIndex()
        gateList = self.m_gateListByChaNo[chanNo]
        for index, gateUi in enumerate(self.m_gateUiList):
            checked = gateUi['checked'].checkState()
            enabled = False
            if checked == QtCore.Qt.Checked:
                enabled = True
            start = gateUi['start'].value()
            length   = gateUi['length'].value()
            threshold = gateUi['threshold'].value()
            if gateUi['gain'] != None:
                gain = gateUi['gain'].value()
                gateList[index].setGain(gain)
            gateList[index].setStart(start)
            gateList[index].setLen(length)
            gateList[index].setThreshold(threshold)
            gateList[index].setEnabled(enabled)
        self.gateUpdated.emit()        
    
