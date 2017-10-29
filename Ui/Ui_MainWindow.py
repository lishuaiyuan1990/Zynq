# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Zynq\Ui\MainWindow.ui'
#
# Created: Sun Oct 29 11:31:23 2017
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
        MainWindow.resize(1498, 895)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.m_aScanWidget = AScanWidgetMultiPlot(self.centralWidget)
        self.m_aScanWidget.setGeometry(QtCore.QRect(260, 20, 1211, 851))
        self.m_aScanWidget.setObjectName(_fromUtf8("m_aScanWidget"))
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 461))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.m_parseToolWidget = ParseToolWidget(self.groupBox)
        self.m_parseToolWidget.setGeometry(QtCore.QRect(10, 20, 221, 421))
        self.m_parseToolWidget.setObjectName(_fromUtf8("m_parseToolWidget"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 473, 241, 401))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.m_paraSetWidget = ParaSetWidget(self.groupBox_2)
        self.m_paraSetWidget.setGeometry(QtCore.QRect(10, 20, 221, 371))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_paraSetWidget.sizePolicy().hasHeightForWidth())
        self.m_paraSetWidget.setSizePolicy(sizePolicy)
        self.m_paraSetWidget.setObjectName(_fromUtf8("m_paraSetWidget"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "波形分析", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "超声参数设置", None))

from ScanWidget import AScanWidgetMultiPlot
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

