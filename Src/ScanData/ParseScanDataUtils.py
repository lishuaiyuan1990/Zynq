import numpy as np

class DetectionUtils(object):
    def __init__(self):
        pass
    
    @staticmethod
    def detection(aScanData, detectionFunc):
        dataRange = (0,  100)
        dataBase = (dataRange[0] + dataRange[1]) / 2;
        targetArray = np.array(aScanData) - dataBase
        detectionArray = map(detectionFunc, targetArray)
        retArray = np.array(detectionArray) + dataBase
        return retArray
        
    @staticmethod
    def negativeToZero(data):
        if data < 0:
            data = 0
        return data
        
    @staticmethod
    def positiveDetection(aScanData):
        return DetectionUtils.detection(aScanData, DetectionUtils.negativeToZero)

    @staticmethod
    def positiveToZero(data):
        if data > 0:
            data = 0
        return data
        
    @staticmethod
    def negativeDetection(aScanData):
        return DetectionUtils.detection(aScanData, DetectionUtils.positiveToZero)
    
    @staticmethod
    def allDetection(aScanData):
        return DetectionUtils.detection(aScanData, abs)
    
    
