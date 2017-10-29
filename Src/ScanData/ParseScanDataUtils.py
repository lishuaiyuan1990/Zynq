import numpy as np

class DetectionUtils(object):
    rct = 100.0
    oldData = 0
    def __init__(self):
        pass
    
    @staticmethod
    def detection(aScanData, detectionFunc):
        dataRange = (0,  100)
        dataBase = (dataRange[0] + dataRange[1]) / 2;
        targetArray = np.array(aScanData) - dataBase
        detectionArray = map(detectionFunc, targetArray)
        #retArray = np.array(detectionArray) + dataBase
        return detectionArray
        
    @staticmethod
    def negativeToZero(data):
        if data < 0:
            data = 0
        data *= 2
        return data
        
    @staticmethod
    def positiveDetection(aScanData):
        return DetectionUtils.detection(aScanData, DetectionUtils.negativeToZero)

    @staticmethod
    def positiveToZero(data):
        if data > 0:
            data = 0
        data *= -2
        return data
        
    @staticmethod
    def negativeDetection(aScanData):
        return DetectionUtils.detection(aScanData, DetectionUtils.positiveToZero)

    @staticmethod
    def negativeToPositive(data):
        if data < 0:
            data *= -1
        data *= 2
        if (DetectionUtils.oldData <= data):
            DetectionUtils.oldData = data
        else:
            delta = DetectionUtils.rct / (1.0 + DetectionUtils.rct)
            DetectionUtils.oldData *= delta
        return DetectionUtils.oldData
    
    @staticmethod
    def allDetection(aScanData):
        DetectionUtils.oldData = 0
        return DetectionUtils.detection(aScanData, DetectionUtils.negativeToPositive)

class DynaGainUtils(object):
    @staticmethod
    def dynaGain(aScanData, dynaGainRange, gain):
        multi = 10 ** (gain / 20.0)
        retAScanList = list(aScanData[0:dynaGainRange['start']]) + \
        list(np.array(aScanData[dynaGainRange['start']:dynaGainRange['end']] * multi)) + \
        list(aScanData[dynaGainRange['end']:])
        return map(DynaGainUtils.limitDataByMax, retAScanList)
        
    @staticmethod
    def limitDataByMax(data):
        maxData = 100
        if data > maxData:
            data = 100
        return data
        
        
        
    
    
