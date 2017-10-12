from PyQt4 import QtGui
from Src import MainWindow


if __name__ == "__main__":
    import sys
    import win32event, pywintypes, win32api 
    ERROR_ALREADY_EXISTS = 183 
    sz_mutex = "zynq_mutex_00" 
    hmutex = win32event.CreateMutex(None, pywintypes.FALSE, sz_mutex) 
    if (win32api.GetLastError() == ERROR_ALREADY_EXISTS): 
        print "checkExist ...."
        sys.exit(0)
    else:
        print "start zynq client app..."
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
