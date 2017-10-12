import win32event, pywintypes, win32api 
import time
import sys

def checkExist():
    ERROR_ALREADY_EXISTS = 183 
    sz_mutex = "zynq_mutex_00" 
    hmutex = win32event.CreateMutex(None, pywintypes.FALSE, sz_mutex) 
    if (win32api.GetLastError() == ERROR_ALREADY_EXISTS): 
        print "checkExist ...."
        sys.exit(0)
    else:
        print "checkExist no...."

if __name__ == "__main__":
    checkExist()
