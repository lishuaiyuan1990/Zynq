import numpy as np
import struct
from ParseScanDataUtils import DetectionUtils, DynaGainUtils

FrameLen = 1250 
FrameHead = 0xCCDD

class AScanData(object):
    def __init__(self, data):
        self.m_dmaData = data
        self.m_parseFrameInterval = 1
        self.m_frameLen = 256
        self.parseAscanData()
        
    
    def iterateFrameData(self, startIndex = 0, endIndex = -1, frameStep = 1, typeSize = 4, cbBreak = None, cbIterate = None):
        if endIndex == -1:
            endIndex = len(self.m_dmaData)
        if self.m_frameLen <= 0:
            return
        while(True):
            if startIndex + self.m_frameLen * 4 >= endIndex:
                break
            dataTuple = struct.unpack("%dI" % (self.m_frameLen * 4 / typeSize),  self.m_dmaData[startIndex : startIndex + self.m_frameLen * 4])
            if cbIterate != None: 
                cbIterate(dataTuple)
            if cbBreak != None:
                for index, value in enumerate(dataTuple):
                    retIndex = startIndex + typeSize * index
                    if cbBreak(value, retIndex):
                        return retIndex
            startIndex += self.m_frameLen * 4 * frameStep
        return -1
    
    def findSampleNum(self):
        pass
    
    def isFrameHead(self, value, retIndex):
        if (value >> 16) == FrameHead:
            self.m_frameHeadNo += 1
            self.m_frameIndexList[self.m_frameHeadNo - 1] = retIndex
            if self.m_frameHeadNo >= 2:
                self.m_frameLen = value & 0x00000FFF
                frameLen = (self.m_frameIndexList[1] - self.m_frameIndexList[0]) / 4
                if frameLen != self.m_frameLen:
                    print "frameLen Error: 1 (frameLen in frameHead error)"
                if self.m_frameLen <= 0:
                    print "frameLn Error: 2 (frameLen in frameHead <= 0)"
                    self.m_frameLen = frameLen
                return True
            return False
        else:
            return False
        
    def getFirstFrameHead(self):
        self.m_frameHeadNo = 0
        self.m_frameIndexList = [0, 0]
        firstFrameHeadIndex = self.iterateFrameData(cbBreak = self.isFrameHead)
        return firstFrameHeadIndex
    
    def genAScanList(self, dataTuple):
        aScanList = []
        frameHead = dataTuple[0]
        chanNo = (frameHead & 0x0000F000) >> 12
        #print "frameHead: %0#8X chanNo: %0#8X " % (frameHead, chanNo)
        frameData = dataTuple[1:]
        for index, value in enumerate(frameData):
            caveData = self.parseFrameData(value)
            aScanList.append(caveData[0])
            #aScanList.append(caveData[1])
        if chanNo not in self.m_parsedFrameDataDict.keys():
            self.m_parsedFrameDataDict[chanNo] = []
        self.m_parsedFrameDataDict[chanNo].append(aScanList)
        return aScanList
    
    #rawData 32 bit
    def parseFrameData(self, rawData):
        dataL10 = 0xFFFF
        dataL = rawData & dataL10
        #dataH = rawData >> 10
        #return [dataL,  dataH]
        return [dataL]
        
        
    def parseAscanData(self):
        self.m_parsedFrameDataDict = {}
        for i in range(0, 16):
            self.m_parsedFrameDataDict[i] = []
        frameHeadIndex = self.getFirstFrameHead()
        if frameHeadIndex == -1:
            return self.m_parsedFrameDataDict
        self.iterateFrameData(startIndex = frameHeadIndex, frameStep = 1, cbIterate = self.genAScanList)
        return self.m_parsedFrameDataDict
    
    def compressAScanList(self, chanNo):
        recvInterval = 0.1
        fps = 10
        AScanListLen = int(round(recvInterval * fps))
        rawAScanListLen = len(self.m_parsedFrameDataDict[chanNo])
        step = max(int(rawAScanListLen / AScanListLen), 1)
        retList = []
        for i in range(0, rawAScanListLen, step):
            retList.append(self.m_parsedFrameDataDict[chanNo][i])
        return retList
        
    def limitDataRange(self, chanNo):
        maxData = 2 ** 10 - 1.0
        return np.array(self.compressAScanList(chanNo)) / maxData * 100
    
    def genAScanDectionData(self, aScanList, detectionMode):
        dectionFunc = None
        if detectionMode == 1:
            dectionFunc = DetectionUtils.positiveDetection
        elif detectionMode == 2:
            dectionFunc = DetectionUtils.negativeDetection
        elif detectionMode == 3:
            dectionFunc = DetectionUtils.allDetection
        return map(dectionFunc, aScanList)

    def genDynaGainData(self, aScanList, dynaGainObj):
        dynaGainFunc = None
        if dynaGainObj['gain'] != 0:
            dynaGainFunc = DynaGainUtils.dynaGain
        else:
            return aScanList
        return map(dynaGainFunc, aScanList, [dynaGainObj['dynaGainRange']] * len(aScanList), [dynaGainObj['gain']] * len(aScanList))

    def getAScanList(self, chanNo, detectionMode, dynaGainObj):
        limitRangeAScanList = self.limitDataRange(chanNo)
        detectionData = self.genAScanDectionData(limitRangeAScanList, detectionMode)
        retAScanList = self.genDynaGainData(detectionData, dynaGainObj)
        #print retAScanList
        return retAScanList

    def getRawAScanList(self, chanNo):
        return self.m_parsedFrameDataDict[chanNo]


class Gate(object):
    def __init__(self, start, len, threshold, enabled = True, color = "#FF0000", gain = 0):
        self.m_start = start
        self.m_len = len
        self.m_threshold = threshold
        self.m_color = color
        self.m_enabled = enabled
        self.m_gain = gain

    def setGain(self, gain):
        self.m_gain = gain
    
    def setStart(self, start):
        self.m_start = start
    
    def setLen(self, len):
        self.m_len = len
    
    def setThreshold(self, threshold):
        self.m_threshold = threshold
    
    def setEnabled(self, enabled):
        self.m_enabled = enabled
        
        
        
