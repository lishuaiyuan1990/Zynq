import numpy as np
import struct

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
        #frameHead = dataTuple[0]
        frameData = dataTuple[1:]
        for index, value in enumerate(frameData):
            caveData = self.parseFrameData(value)
            aScanList.append(caveData[0])
            aScanList.append(caveData[1])
        self.m_parsedFrameDataList.append(aScanList)
        return aScanList
    
    #rawData 32 bit
    def parseFrameData(self, rawData):
        dataL10 = 0x3FF
        dataL = rawData & dataL10
        dataH = rawData >> 10
        return [dataL,  dataH]
        
        
    def parseAscanData(self):
        self.m_parsedFrameDataList = []
        frameHeadIndex = self.getFirstFrameHead()
        if frameHeadIndex == -1:
            return self.m_parsedFrameDataList
        self.iterateFrameData(startIndex = frameHeadIndex, frameStep = 10, cbIterate = self.genAScanList)
        return self.m_parsedFrameDataList
    
    def limitDataRange(self):
        maxData = 2 ** 10 - 1.0
        return np.array(self.m_parsedFrameDataList) / maxData * 100
    
    def getAScanList(self):
        return self.limitDataRange()
        
    def getRawAScanList(self):
        return self.m_parsedFrameDataList



class Gate(object):
    def __init__(self, start, len, threshold, enabled = True, color = "#FF0000"):
        self.m_start = start
        self.m_len = len
        self.m_threshold = threshold
        self.m_color = color
        self.m_enabled = enabled
    
    def setStart(self, start):
        self.m_start = start
    
    def setLen(self, len):
        self.m_len = len
    
    def setThreshold(self, threshold):
        self.m_threshold = threshold
    
    def setEnabled(self, enabled):
        self.m_enabled = enabled
        
        
        
