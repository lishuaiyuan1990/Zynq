from Ui_ParaSetWidget import Ui_ParaSetWidget
from PyQt4 import QtGui
class ParaSetWidgetUi(QtGui.QWidget):
    def __init__(self, parent = None):
        super(ParaSetWidgetUi, self).__init__(parent)
        self.ui = Ui_ParaSetWidget()
        self.ui.setupUi(self)
        pass
