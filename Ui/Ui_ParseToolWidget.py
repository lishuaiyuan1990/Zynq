# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Zynq\Ui/ParseToolWidget.ui'
#
# Created: Sat Oct 21 22:56:56 2017
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

class Ui_ParseToolWidget(object):
    def setupUi(self, ParseToolWidget):
        ParseToolWidget.setObjectName(_fromUtf8("ParseToolWidget"))
        ParseToolWidget.resize(221, 449)
        self.widget = QtGui.QWidget(ParseToolWidget)
        self.widget.setGeometry(QtCore.QRect(12, 12, 191, 411))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.widget)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        self.m_chanNo = QtGui.QComboBox(self.widget)
        self.m_chanNo.setObjectName(_fromUtf8("m_chanNo"))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.m_chanNo.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.m_chanNo)
        self.gridLayout_6.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.m_detectionMode = QtGui.QComboBox(self.widget)
        self.m_detectionMode.setObjectName(_fromUtf8("m_detectionMode"))
        self.m_detectionMode.addItem(_fromUtf8(""))
        self.m_detectionMode.addItem(_fromUtf8(""))
        self.m_detectionMode.addItem(_fromUtf8(""))
        self.m_detectionMode.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.m_detectionMode)
        self.gridLayout_6.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.m_gate1Checked = QtGui.QCheckBox(self.widget)
        self.m_gate1Checked.setChecked(True)
        self.m_gate1Checked.setObjectName(_fromUtf8("m_gate1Checked"))
        self.horizontalLayout.addWidget(self.m_gate1Checked)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_17.addWidget(self.label_14)
        self.m_gate1Threshold = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate1Threshold.setMinimum(1.0)
        self.m_gate1Threshold.setMaximum(99.0)
        self.m_gate1Threshold.setProperty("value", 50.0)
        self.m_gate1Threshold.setObjectName(_fromUtf8("m_gate1Threshold"))
        self.horizontalLayout_17.addWidget(self.m_gate1Threshold)
        self.horizontalLayout.addLayout(self.horizontalLayout_17)
        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_12 = QtGui.QLabel(self.widget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_16.addWidget(self.label_12)
        self.m_gate1Start = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate1Start.setMaximum(2999.0)
        self.m_gate1Start.setSingleStep(10.0)
        self.m_gate1Start.setProperty("value", 50.0)
        self.m_gate1Start.setObjectName(_fromUtf8("m_gate1Start"))
        self.horizontalLayout_16.addWidget(self.m_gate1Start)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_18.addWidget(self.label_13)
        self.m_gate1Len = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate1Len.setMinimum(1.0)
        self.m_gate1Len.setMaximum(3000.0)
        self.m_gate1Len.setSingleStep(10.0)
        self.m_gate1Len.setProperty("value", 100.0)
        self.m_gate1Len.setObjectName(_fromUtf8("m_gate1Len"))
        self.horizontalLayout_18.addWidget(self.m_gate1Len)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_18)
        self.gridLayout_5.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.m_gate2Checked = QtGui.QCheckBox(self.widget)
        self.m_gate2Checked.setChecked(True)
        self.m_gate2Checked.setObjectName(_fromUtf8("m_gate2Checked"))
        self.horizontalLayout_2.addWidget(self.m_gate2Checked)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_19.addWidget(self.label_15)
        self.m_gate2Threshold = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate2Threshold.setMinimum(1.0)
        self.m_gate2Threshold.setMaximum(99.0)
        self.m_gate2Threshold.setProperty("value", 50.0)
        self.m_gate2Threshold.setObjectName(_fromUtf8("m_gate2Threshold"))
        self.horizontalLayout_19.addWidget(self.m_gate2Threshold)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_19)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_16 = QtGui.QLabel(self.widget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_20.addWidget(self.label_16)
        self.m_gate2Start = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate2Start.setMaximum(2999.0)
        self.m_gate2Start.setSingleStep(10.0)
        self.m_gate2Start.setProperty("value", 50.0)
        self.m_gate2Start.setObjectName(_fromUtf8("m_gate2Start"))
        self.horizontalLayout_20.addWidget(self.m_gate2Start)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_17 = QtGui.QLabel(self.widget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_21.addWidget(self.label_17)
        self.m_gate2Len = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate2Len.setMinimum(1.0)
        self.m_gate2Len.setMaximum(3000.0)
        self.m_gate2Len.setSingleStep(10.0)
        self.m_gate2Len.setProperty("value", 100.0)
        self.m_gate2Len.setObjectName(_fromUtf8("m_gate2Len"))
        self.horizontalLayout_21.addWidget(self.m_gate2Len)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_21)
        self.gridLayout_4.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.m_gate3Checked = QtGui.QCheckBox(self.widget)
        self.m_gate3Checked.setChecked(True)
        self.m_gate3Checked.setObjectName(_fromUtf8("m_gate3Checked"))
        self.horizontalLayout_3.addWidget(self.m_gate3Checked)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_18 = QtGui.QLabel(self.widget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_22.addWidget(self.label_18)
        self.m_gate3Threshold = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate3Threshold.setMinimum(1.0)
        self.m_gate3Threshold.setMaximum(99.0)
        self.m_gate3Threshold.setProperty("value", 50.0)
        self.m_gate3Threshold.setObjectName(_fromUtf8("m_gate3Threshold"))
        self.horizontalLayout_22.addWidget(self.m_gate3Threshold)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_22)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_19 = QtGui.QLabel(self.widget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_23.addWidget(self.label_19)
        self.m_gate3Start = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate3Start.setMaximum(2999.0)
        self.m_gate3Start.setSingleStep(10.0)
        self.m_gate3Start.setProperty("value", 50.0)
        self.m_gate3Start.setObjectName(_fromUtf8("m_gate3Start"))
        self.horizontalLayout_23.addWidget(self.m_gate3Start)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.label_20 = QtGui.QLabel(self.widget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_24.addWidget(self.label_20)
        self.m_gate3Len = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate3Len.setMinimum(1.0)
        self.m_gate3Len.setMaximum(3000.0)
        self.m_gate3Len.setSingleStep(10.0)
        self.m_gate3Len.setProperty("value", 100.0)
        self.m_gate3Len.setObjectName(_fromUtf8("m_gate3Len"))
        self.horizontalLayout_24.addWidget(self.m_gate3Len)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_24)
        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.m_gate4Checked = QtGui.QCheckBox(self.widget)
        self.m_gate4Checked.setChecked(True)
        self.m_gate4Checked.setObjectName(_fromUtf8("m_gate4Checked"))
        self.horizontalLayout_9.addWidget(self.m_gate4Checked)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_21 = QtGui.QLabel(self.widget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_25.addWidget(self.label_21)
        self.m_gate4Threshold = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate4Threshold.setMinimum(1.0)
        self.m_gate4Threshold.setMaximum(99.0)
        self.m_gate4Threshold.setProperty("value", 50.0)
        self.m_gate4Threshold.setObjectName(_fromUtf8("m_gate4Threshold"))
        self.horizontalLayout_25.addWidget(self.m_gate4Threshold)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_25)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.label_22 = QtGui.QLabel(self.widget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_26.addWidget(self.label_22)
        self.m_gate4Start = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate4Start.setMaximum(2999.0)
        self.m_gate4Start.setSingleStep(10.0)
        self.m_gate4Start.setProperty("value", 50.0)
        self.m_gate4Start.setObjectName(_fromUtf8("m_gate4Start"))
        self.horizontalLayout_26.addWidget(self.m_gate4Start)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_26)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_23 = QtGui.QLabel(self.widget)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)
        self.m_gate4Len = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate4Len.setMinimum(1.0)
        self.m_gate4Len.setMaximum(3000.0)
        self.m_gate4Len.setSingleStep(10.0)
        self.m_gate4Len.setProperty("value", 100.0)
        self.m_gate4Len.setObjectName(_fromUtf8("m_gate4Len"))
        self.gridLayout_2.addWidget(self.m_gate4Len, 0, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_24 = QtGui.QLabel(self.widget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_8.addWidget(self.label_24)
        self.m_gate4Len_2 = QtGui.QDoubleSpinBox(self.widget)
        self.m_gate4Len_2.setMinimum(1.0)
        self.m_gate4Len_2.setMaximum(3000.0)
        self.m_gate4Len_2.setSingleStep(10.0)
        self.m_gate4Len_2.setProperty("value", 100.0)
        self.m_gate4Len_2.setObjectName(_fromUtf8("m_gate4Len_2"))
        self.horizontalLayout_8.addWidget(self.m_gate4Len_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 4, 0, 1, 1)

        self.retranslateUi(ParseToolWidget)
        QtCore.QMetaObject.connectSlotsByName(ParseToolWidget)

    def retranslateUi(self, ParseToolWidget):
        ParseToolWidget.setWindowTitle(_translate("ParseToolWidget", "Form", None))
        self.label.setText(_translate("ParseToolWidget", "通道选择", None))
        self.m_chanNo.setItemText(0, _translate("ParseToolWidget", "通道1", None))
        self.m_chanNo.setItemText(1, _translate("ParseToolWidget", "通道2", None))
        self.m_chanNo.setItemText(2, _translate("ParseToolWidget", "通道3", None))
        self.m_chanNo.setItemText(3, _translate("ParseToolWidget", "通道4", None))
        self.m_chanNo.setItemText(4, _translate("ParseToolWidget", "通道5", None))
        self.m_chanNo.setItemText(5, _translate("ParseToolWidget", "通道6", None))
        self.m_chanNo.setItemText(6, _translate("ParseToolWidget", "通道7", None))
        self.m_chanNo.setItemText(7, _translate("ParseToolWidget", "通道8", None))
        self.label_2.setText(_translate("ParseToolWidget", "波形显示", None))
        self.m_detectionMode.setItemText(0, _translate("ParseToolWidget", "射频波", None))
        self.m_detectionMode.setItemText(1, _translate("ParseToolWidget", "正半波", None))
        self.m_detectionMode.setItemText(2, _translate("ParseToolWidget", "负半波", None))
        self.m_detectionMode.setItemText(3, _translate("ParseToolWidget", "检波", None))
        self.m_gate1Checked.setText(_translate("ParseToolWidget", "闸门1", None))
        self.label_14.setText(_translate("ParseToolWidget", "阈值", None))
        self.label_12.setText(_translate("ParseToolWidget", "起始", None))
        self.label_13.setText(_translate("ParseToolWidget", "宽度", None))
        self.m_gate2Checked.setText(_translate("ParseToolWidget", "闸门2", None))
        self.label_15.setText(_translate("ParseToolWidget", "阈值", None))
        self.label_16.setText(_translate("ParseToolWidget", "起始", None))
        self.label_17.setText(_translate("ParseToolWidget", "宽度", None))
        self.m_gate3Checked.setText(_translate("ParseToolWidget", "闸门3", None))
        self.label_18.setText(_translate("ParseToolWidget", "阈值", None))
        self.label_19.setText(_translate("ParseToolWidget", "起始", None))
        self.label_20.setText(_translate("ParseToolWidget", "宽度", None))
        self.m_gate4Checked.setText(_translate("ParseToolWidget", "增益补偿闸门", None))
        self.label_21.setText(_translate("ParseToolWidget", "阈值", None))
        self.label_22.setText(_translate("ParseToolWidget", "起始", None))
        self.label_23.setText(_translate("ParseToolWidget", "宽度", None))
        self.label_24.setText(_translate("ParseToolWidget", "补偿增益(dB)", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ParseToolWidget = QtGui.QWidget()
    ui = Ui_ParseToolWidget()
    ui.setupUi(ParseToolWidget)
    ParseToolWidget.show()
    sys.exit(app.exec_())
