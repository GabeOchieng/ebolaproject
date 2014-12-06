# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pstochpyf.ui'
#
# Created: Fri Dec 05 14:27:43 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(2080, 1401)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(630, 1200, 844, 40))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton_4 = QtGui.QRadioButton(self.widget)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.widget)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.widget)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.horizontalLayout.addWidget(self.radioButton_6)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(31, 20, 1841, 62))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.formLayout = QtGui.QFormLayout(self.widget1)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.InputFile = QtGui.QPushButton(self.widget1)
        self.InputFile.setObjectName(_fromUtf8("InputFile"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.InputFile)
        self.textBrowser = QtGui.QTextBrowser(self.widget1)
        self.textBrowser.setMinimumSize(QtCore.QSize(1637, 60))
        self.textBrowser.setMaximumSize(QtCore.QSize(1751, 60))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.textBrowser)
        self.widget2 = QtGui.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(30, 120, 1841, 1002))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.formLayout_2 = QtGui.QFormLayout(self.widget2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.pushButton_4 = QtGui.QPushButton(self.widget2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton_4)
        self.graphicsView = QtGui.QGraphicsView(self.widget2)
        self.graphicsView.setMinimumSize(QtCore.QSize(1637, 1000))
        self.graphicsView.setMaximumSize(QtCore.QSize(1640, 16777215))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.graphicsView)
        self.widget3 = QtGui.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(30, 1160, 191, 121))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.formLayout_3 = QtGui.QFormLayout(self.widget3)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.widget3)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.progressBar = QtGui.QProgressBar(self.widget3)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.radioButton_4.setText(_translate("Dialog", "Import Data CSV", None))
        self.radioButton_5.setText(_translate("Dialog", "Import Data ACII", None))
        self.radioButton_6.setText(_translate("Dialog", "Import Data Binary", None))
        self.InputFile.setText(_translate("Dialog", "Import File", None))
        self.pushButton_4.setText(_translate("Dialog", "Graph", None))
        self.label.setText(_translate("Dialog", "Processing", None))
		
		
