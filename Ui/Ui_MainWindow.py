# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Zynq\Ui\MainWindow.ui'
#
# Created: Sun Oct 22 20:01:05 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(857, 634)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.m_paraSetWidget = ParaSetWidget(self.centralWidget)
        self.m_paraSetWidget.setGeometry(QtCore.QRect(10, 480, 841, 141))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_paraSetWidget.sizePolicy().hasHeightForWidth())
        self.m_paraSetWidget.setSizePolicy(sizePolicy)
        self.m_paraSetWidget.setObjectName(_fromUtf8("m_paraSetWidget"))
        self.m_aScanWidget = AScanWidget(self.centralWidget)
        self.m_aScanWidget.setGeometry(QtCore.QRect(10, 10, 611, 461))
        self.m_aScanWidget.setObjectName(_fromUtf8("m_aScanWidget"))
        self.m_parseToolWidget = ParseToolWidget(self.centralWidget)
        self.m_parseToolWidget.setGeometry(QtCore.QRect(630, 10, 221, 461))
        self.m_parseToolWidget.setObjectName(_fromUtf8("m_parseToolWidget"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

from ScanWidget import AScanWidget
from ParaSetWidget import ParaSetWidget
from ParseToolWidget import ParseToolWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

