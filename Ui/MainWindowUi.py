from Ui_MainWindow import Ui_MainWindow
from PyQt4 import QtGui
class MainWindowUi(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindowUi, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pass
