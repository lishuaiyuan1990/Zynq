# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Zynq\Ui\ParaSetWidget.ui'
#
# Created: Sun Oct 22 16:32:22 2017
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

class Ui_ParaSetWidget(object):
    def setupUi(self, ParaSetWidget):
        ParaSetWidget.setObjectName(_fromUtf8("ParaSetWidget"))
        ParaSetWidget.resize(745, 136)
        self.layoutWidget = QtGui.QWidget(ParaSetWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 7, 721, 116))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.m_chanNo = QtGui.QComboBox(self.layoutWidget)
        self.m_chanNo.setObjectName(_fromUtf8("m_chanNo"))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.m_chanNo)
        self.horizontalLayout_11.addLayout(self.horizontalLayout)
        self.m_chanChecked = QtGui.QCheckBox(self.layoutWidget)
        self.m_chanChecked.setChecked(True)
        self.m_chanChecked.setObjectName(_fromUtf8("m_chanChecked"))
        self.horizontalLayout_11.addWidget(self.m_chanChecked)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)
        self.gridLayout_5.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.m_eVoltage = QtGui.QComboBox(self.layoutWidget)
        self.m_eVoltage.setObjectName(_fromUtf8("m_eVoltage"))
        self.m_eVoltage.addItem(_fromUtf8(""))
        self.m_eVoltage.addItem(_fromUtf8(""))
        self.m_eVoltage.addItem(_fromUtf8(""))
        self.m_eVoltage.addItem(_fromUtf8(""))
        self.m_eVoltage.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.m_eVoltage)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.m_sampleLen = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_sampleLen.setMinimum(100.0)
        self.m_sampleLen.setMaximum(2000.0)
        self.m_sampleLen.setProperty("value", 250.0)
        self.m_sampleLen.setObjectName(_fromUtf8("m_sampleLen"))
        self.horizontalLayout_10.addWidget(self.m_sampleLen)
        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.m_gain = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gain.setMaximum(110.0)
        self.m_gain.setSingleStep(0.1)
        self.m_gain.setProperty("value", 35.0)
        self.m_gain.setObjectName(_fromUtf8("m_gain"))
        self.horizontalLayout_8.addWidget(self.m_gain)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_9.addWidget(self.label_8)
        self.m_sonicV = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_sonicV.setMinimum(300.0)
        self.m_sonicV.setMaximum(10000.0)
        self.m_sonicV.setSingleStep(10.0)
        self.m_sonicV.setProperty("value", 5950.0)
        self.m_sonicV.setObjectName(_fromUtf8("m_sonicV"))
        self.horizontalLayout_9.addWidget(self.m_sonicV)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.m_sonicPD = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_sonicPD.setMinimum(10.0)
        self.m_sonicPD.setMaximum(3000.0)
        self.m_sonicPD.setSingleStep(10.0)
        self.m_sonicPD.setProperty("value", 300.0)
        self.m_sonicPD.setObjectName(_fromUtf8("m_sonicPD"))
        self.horizontalLayout_5.addWidget(self.m_sonicPD)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.m_offset = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_offset.setMaximum(1000.0)
        self.m_offset.setSingleStep(10.0)
        self.m_offset.setProperty("value", 20.0)
        self.m_offset.setObjectName(_fromUtf8("m_offset"))
        self.horizontalLayout_6.addWidget(self.m_offset)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 4, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.m_openSysBtn = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_openSysBtn.sizePolicy().hasHeightForWidth())
        self.m_openSysBtn.setSizePolicy(sizePolicy)
        self.m_openSysBtn.setObjectName(_fromUtf8("m_openSysBtn"))
        self.verticalLayout.addWidget(self.m_openSysBtn)
        self.m_stopSysBtn = QtGui.QPushButton(self.layoutWidget)
        self.m_stopSysBtn.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_stopSysBtn.sizePolicy().hasHeightForWidth())
        self.m_stopSysBtn.setSizePolicy(sizePolicy)
        self.m_stopSysBtn.setObjectName(_fromUtf8("m_stopSysBtn"))
        self.verticalLayout.addWidget(self.m_stopSysBtn)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 6, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.m_triggerMode = QtGui.QComboBox(self.layoutWidget)
        self.m_triggerMode.setObjectName(_fromUtf8("m_triggerMode"))
        self.m_triggerMode.addItem(_fromUtf8(""))
        self.m_triggerMode.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.m_triggerMode)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.m_prf = QtGui.QComboBox(self.layoutWidget)
        self.m_prf.setObjectName(_fromUtf8("m_prf"))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.m_prf.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.m_prf)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.m_probePrf = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_probePrf.setMinimum(0.5)
        self.m_probePrf.setMaximum(15.0)
        self.m_probePrf.setSingleStep(0.25)
        self.m_probePrf.setProperty("value", 2.5)
        self.m_probePrf.setObjectName(_fromUtf8("m_probePrf"))
        self.horizontalLayout_4.addWidget(self.m_probePrf)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.retranslateUi(ParaSetWidget)
        self.m_eVoltage.setCurrentIndex(1)
        self.m_prf.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(ParaSetWidget)

    def retranslateUi(self, ParaSetWidget):
        ParaSetWidget.setWindowTitle(_translate("ParaSetWidget", "ParaSet", None))
        self.label.setText(_translate("ParaSetWidget", "通道使能选择", None))
        self.m_chanNo.setItemText(0, _translate("ParaSetWidget", "通道1", None))
        self.m_chanNo.setItemText(1, _translate("ParaSetWidget", "通道2", None))
        self.m_chanNo.setItemText(2, _translate("ParaSetWidget", "通道3", None))
        self.m_chanNo.setItemText(3, _translate("ParaSetWidget", "通道4", None))
        self.m_chanNo.setItemText(4, _translate("ParaSetWidget", "通道5", None))
        self.m_chanNo.setItemText(5, _translate("ParaSetWidget", "通道6", None))
        self.m_chanNo.setItemText(6, _translate("ParaSetWidget", "通道7", None))
        self.m_chanNo.setItemText(7, _translate("ParaSetWidget", "通道8", None))
        self.m_chanChecked.setText(_translate("ParaSetWidget", "通道使能", None))
        self.label_4.setText(_translate("ParaSetWidget", "激励电压(V)", None))
        self.m_eVoltage.setItemText(0, _translate("ParaSetWidget", "400", None))
        self.m_eVoltage.setItemText(1, _translate("ParaSetWidget", "300", None))
        self.m_eVoltage.setItemText(2, _translate("ParaSetWidget", "200", None))
        self.m_eVoltage.setItemText(3, _translate("ParaSetWidget", "100", None))
        self.m_eVoltage.setItemText(4, _translate("ParaSetWidget", "50", None))
        self.label_10.setText(_translate("ParaSetWidget", "采样个数", None))
        self.label_6.setText(_translate("ParaSetWidget", "增益(dB)", None))
        self.label_8.setText(_translate("ParaSetWidget", "声速(m/s)", None))
        self.label_7.setText(_translate("ParaSetWidget", "声程(mm)", None))
        self.label_9.setText(_translate("ParaSetWidget", "起始偏移(mm)", None))
        self.m_openSysBtn.setText(_translate("ParaSetWidget", "启动系统", None))
        self.m_stopSysBtn.setText(_translate("ParaSetWidget", "停止", None))
        self.label_2.setText(_translate("ParaSetWidget", "触发模式", None))
        self.m_triggerMode.setItemText(0, _translate("ParaSetWidget", "PE", None))
        self.m_triggerMode.setItemText(1, _translate("ParaSetWidget", "PC", None))
        self.label_3.setText(_translate("ParaSetWidget", "重复频率(Hz)", None))
        self.m_prf.setItemText(0, _translate("ParaSetWidget", "80", None))
        self.m_prf.setItemText(1, _translate("ParaSetWidget", "160", None))
        self.m_prf.setItemText(2, _translate("ParaSetWidget", "240", None))
        self.m_prf.setItemText(3, _translate("ParaSetWidget", "400", None))
        self.m_prf.setItemText(4, _translate("ParaSetWidget", "500", None))
        self.m_prf.setItemText(5, _translate("ParaSetWidget", "1000", None))
        self.m_prf.setItemText(6, _translate("ParaSetWidget", "2000", None))
        self.m_prf.setItemText(7, _translate("ParaSetWidget", "4000", None))
        self.m_prf.setItemText(8, _translate("ParaSetWidget", "5000", None))
        self.m_prf.setItemText(9, _translate("ParaSetWidget", "8000", None))
        self.m_prf.setItemText(10, _translate("ParaSetWidget", "10000", None))
        self.m_prf.setItemText(11, _translate("ParaSetWidget", "16000", None))
        self.label_5.setText(_translate("ParaSetWidget", "探头频率(MHz)", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ParaSetWidget = QtGui.QWidget()
    ui = Ui_ParaSetWidget()
    ui.setupUi(ParaSetWidget)
    ParaSetWidget.show()
    sys.exit(app.exec_())

