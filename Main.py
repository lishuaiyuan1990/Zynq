from PyQt4 import QtGui
from Src import MainWindow
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
