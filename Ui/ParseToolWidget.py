from PyQt4 import QtCore
from PyQt4 import QtGui
from ParseToolWidgetUi import ParseToolWidgetUi
from Src.ScanData import Gate
class ParseToolWidget(ParseToolWidgetUi):
    def __init__(self, parent = None):
        super(ParseToolWidget, self).__init__(parent)
        self.m_gateProcesser = GateProcess(self.ui)

    def getGateList(self):
        return self.m_gateProcesser.getGateList()

    def getChanNo(self):
        chan = self.ui.m_chanNo.currentIndex()
        return chan

    def getDetectionMode(self):
        detectionMode = self.ui.m_detectionMode.currentIndex()
        return detectionMode
    
    def getDynaGain(self):
        dynaGate = self.m_gateProcesser.getDynaGate()
        dynaGain = 0
        if dynaGate.m_enabled:
            dynaGain = dynaGate.m_gain
        return {'gate': dynaGate, 'gain': dynaGain}
        
class GateProcess(QtCore.QObject):
    gateUpdated = QtCore.pyqtSignal()
    def __init__(self, ui):
        super(GateProcess, self).__init__()
        self.ui = ui
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
        'length': self.ui.m_gate4Len, 'threshold': self.ui.m_gate4Threshold, 'color': "#FFFF00", 'gain': self.ui.m_gateGain}
        self.m_gateUiList = [gate1Ui, gate2Ui, gate3Ui, gate4Ui]
    
    def getDynaGate(self):
        length = len(self.m_gateList)
        return self.m_gateList[length - 1] 

    def getGateList(self):
        return self.m_gateList

    def iterateGateUiList(self, callback):
        for gateUi in self.m_gateUiList:
            callback(gateUi)
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
        self.m_gateList = []
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
            self.m_gateList.append(gate)
        self.gateUpdated.emit()


    def updateGate(self):
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
                self.m_gateList[index].setGain(gain)
            self.m_gateList[index].setStart(start)
            self.m_gateList[index].setLen(length)
            self.m_gateList[index].setThreshold(threshold)
            self.m_gateList[index].setEnabled(enabled)
        self.gateUpdated.emit()        
    
