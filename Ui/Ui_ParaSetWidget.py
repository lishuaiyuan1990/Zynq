# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Zynq\Ui\ParaSetWidget.ui'
#
# Created: Sun Oct 01 21:10:07 2017
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
        ParaSetWidget.resize(261, 575)
        self.layoutWidget = QtGui.QWidget(ParaSetWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 241, 551))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_8 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.m_startSysBtn = QtGui.QPushButton(self.layoutWidget)
        self.m_startSysBtn.setObjectName(_fromUtf8("m_startSysBtn"))
        self.horizontalLayout_12.addWidget(self.m_startSysBtn)
        self.m_stopSysBtn = QtGui.QPushButton(self.layoutWidget)
        self.m_stopSysBtn.setObjectName(_fromUtf8("m_stopSysBtn"))
        self.horizontalLayout_12.addWidget(self.m_stopSysBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
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
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
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
        self.m_eVoltage.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.m_eVoltage)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_10.addWidget(self.label_10)
        self.m_sampleLen = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_sampleLen.setMinimum(100.0)
        self.m_sampleLen.setMaximum(512.0)
        self.m_sampleLen.setProperty("value", 250.0)
        self.m_sampleLen.setObjectName(_fromUtf8("m_sampleLen"))
        self.horizontalLayout_10.addWidget(self.m_sampleLen)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.m_gain = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gain.setMaximum(96.0)
        self.m_gain.setSingleStep(0.1)
        self.m_gain.setProperty("value", 35.0)
        self.m_gain.setObjectName(_fromUtf8("m_gain"))
        self.horizontalLayout_8.addWidget(self.m_gain)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_14.addWidget(self.label_11)
        self.m_recvChanNo = QtGui.QComboBox(self.layoutWidget)
        self.m_recvChanNo.setObjectName(_fromUtf8("m_recvChanNo"))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.m_recvChanNo.addItem(_fromUtf8(""))
        self.horizontalLayout_14.addWidget(self.m_recvChanNo)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 3, 0, 1, 1)
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
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.gridLayout.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.m_sendParaBtn = QtGui.QPushButton(self.layoutWidget)
        self.m_sendParaBtn.setObjectName(_fromUtf8("m_sendParaBtn"))
        self.horizontalLayout_15.addWidget(self.m_sendParaBtn)
        self.m_openSysBtn = QtGui.QPushButton(self.layoutWidget)
        self.m_openSysBtn.setObjectName(_fromUtf8("m_openSysBtn"))
        self.horizontalLayout_15.addWidget(self.m_openSysBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.m_gate1Checked = QtGui.QCheckBox(self.layoutWidget)
        self.m_gate1Checked.setChecked(True)
        self.m_gate1Checked.setObjectName(_fromUtf8("m_gate1Checked"))
        self.horizontalLayout_19.addWidget(self.m_gate1Checked)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_17.addWidget(self.label_14)
        self.m_gate1Threshold = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gate1Threshold.setMinimum(1.0)
        self.m_gate1Threshold.setMaximum(99.0)
        self.m_gate1Threshold.setProperty("value", 50.0)
        self.m_gate1Threshold.setObjectName(_fromUtf8("m_gate1Threshold"))
        self.horizontalLayout_17.addWidget(self.m_gate1Threshold)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_17)
        self.gridLayout_6.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_16.addWidget(self.label_12)
        self.m_gate1Start = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gate1Start.setMaximum(2999.0)
        self.m_gate1Start.setSingleStep(10.0)
        self.m_gate1Start.setProperty("value", 50.0)
        self.m_gate1Start.setObjectName(_fromUtf8("m_gate1Start"))
        self.horizontalLayout_16.addWidget(self.m_gate1Start)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_18.addWidget(self.label_13)
        self.m_gate1Len = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gate1Len.setMinimum(1.0)
        self.m_gate1Len.setMaximum(3000.0)
        self.m_gate1Len.setSingleStep(10.0)
        self.m_gate1Len.setProperty("value", 100.0)
        self.m_gate1Len.setObjectName(_fromUtf8("m_gate1Len"))
        self.horizontalLayout_18.addWidget(self.m_gate1Len)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_18)
        self.gridLayout_6.addLayout(self.horizontalLayout_20, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.m_gate2Checked = QtGui.QCheckBox(self.layoutWidget)
        self.m_gate2Checked.setChecked(True)
        self.m_gate2Checked.setObjectName(_fromUtf8("m_gate2Checked"))
        self.horizontalLayout_21.addWidget(self.m_gate2Checked)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_22.addWidget(self.label_15)
        self.m_gate2Threshold = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gate2Threshold.setMinimum(1.0)
        self.m_gate2Threshold.setMaximum(99.0)
        self.m_gate2Threshold.setProperty("value", 50.0)
        self.m_gate2Threshold.setObjectName(_fromUtf8("m_gate2Threshold"))
        self.horizontalLayout_22.addWidget(self.m_gate2Threshold)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)
        self.gridLayout_7.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_24.addWidget(self.label_16)
        self.m_gate2Start = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gate2Start.setMaximum(2999.0)
        self.m_gate2Start.setSingleStep(10.0)
        self.m_gate2Start.setProperty("value", 50.0)
        self.m_gate2Start.setObjectName(_fromUtf8("m_gate2Start"))
        self.horizontalLayout_24.addWidget(self.m_gate2Start)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_25.addWidget(self.label_17)
        self.m_gate2Len = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.m_gate2Len.setMinimum(1.0)
        self.m_gate2Len.setMaximum(3000.0)
        self.m_gate2Len.setSingleStep(10.0)
        self.m_gate2Len.setProperty("value", 100.0)
        self.m_gate2Len.setObjectName(_fromUtf8("m_gate2Len"))
        self.horizontalLayout_25.addWidget(self.m_gate2Len)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_25)
        self.gridLayout_7.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 2, 0, 1, 1)

        self.retranslateUi(ParaSetWidget)
        self.m_eVoltage.setCurrentIndex(2)
        self.m_prf.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(ParaSetWidget)

    def retranslateUi(self, ParaSetWidget):
        ParaSetWidget.setWindowTitle(_translate("ParaSetWidget", "ParaSet", None))
        self.m_startSysBtn.setText(_translate("ParaSetWidget", "配置DMA", None))
        self.m_stopSysBtn.setText(_translate("ParaSetWidget", "停止", None))
        self.label.setText(_translate("ParaSetWidget", "通道选择", None))
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
        self.m_eVoltage.setItemText(0, _translate("ParaSetWidget", "500", None))
        self.m_eVoltage.setItemText(1, _translate("ParaSetWidget", "400", None))
        self.m_eVoltage.setItemText(2, _translate("ParaSetWidget", "300", None))
        self.m_eVoltage.setItemText(3, _translate("ParaSetWidget", "200", None))
        self.m_eVoltage.setItemText(4, _translate("ParaSetWidget", "100", None))
        self.m_eVoltage.setItemText(5, _translate("ParaSetWidget", "50", None))
        self.label_10.setText(_translate("ParaSetWidget", "采样个数", None))
        self.label_6.setText(_translate("ParaSetWidget", "增益(dB)", None))
        self.label_11.setText(_translate("ParaSetWidget", "接收通道", None))
        self.m_recvChanNo.setItemText(0, _translate("ParaSetWidget", "通道1", None))
        self.m_recvChanNo.setItemText(1, _translate("ParaSetWidget", "通道2", None))
        self.m_recvChanNo.setItemText(2, _translate("ParaSetWidget", "通道3", None))
        self.m_recvChanNo.setItemText(3, _translate("ParaSetWidget", "通道4", None))
        self.m_recvChanNo.setItemText(4, _translate("ParaSetWidget", "通道5", None))
        self.m_recvChanNo.setItemText(5, _translate("ParaSetWidget", "通道6", None))
        self.m_recvChanNo.setItemText(6, _translate("ParaSetWidget", "通道7", None))
        self.m_recvChanNo.setItemText(7, _translate("ParaSetWidget", "通道8", None))
        self.label_8.setText(_translate("ParaSetWidget", "声速(m/s)", None))
        self.label_7.setText(_translate("ParaSetWidget", "声程(mm)", None))
        self.label_9.setText(_translate("ParaSetWidget", "起始偏移(mm)", None))
        self.label_2.setText(_translate("ParaSetWidget", "触发模式", None))
        self.m_triggerMode.setItemText(0, _translate("ParaSetWidget", "PE", None))
        self.m_triggerMode.setItemText(1, _translate("ParaSetWidget", "PC", None))
        self.label_5.setText(_translate("ParaSetWidget", "探头频率(MHz)", None))
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
        self.m_sendParaBtn.setText(_translate("ParaSetWidget", "发送参数", None))
        self.m_openSysBtn.setText(_translate("ParaSetWidget", "启动系统", None))
        self.m_gate1Checked.setText(_translate("ParaSetWidget", "闸门1", None))
        self.label_14.setText(_translate("ParaSetWidget", "阈值", None))
        self.label_12.setText(_translate("ParaSetWidget", "起始", None))
        self.label_13.setText(_translate("ParaSetWidget", "宽度", None))
        self.m_gate2Checked.setText(_translate("ParaSetWidget", "闸门2", None))
        self.label_15.setText(_translate("ParaSetWidget", "阈值", None))
        self.label_16.setText(_translate("ParaSetWidget", "起始", None))
        self.label_17.setText(_translate("ParaSetWidget", "宽度", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ParaSetWidget = QtGui.QWidget()
    ui = Ui_ParaSetWidget()
    ui.setupUi(ParaSetWidget)
    ParaSetWidget.show()
    sys.exit(app.exec_())

