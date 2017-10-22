from Ui_ParseToolWidget import Ui_ParseToolWidget
from PyQt4 import QtGui
class ParseToolWidgetUi(QtGui.QWidget):
    def __init__(self, parent = None):
        super(ParseToolWidgetUi, self).__init__(parent)
        self.ui = Ui_ParseToolWidget()
        self.ui.setupUi(self)
        pass
