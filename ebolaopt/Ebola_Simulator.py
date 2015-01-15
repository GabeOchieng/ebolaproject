#!/usr/bin/python 

#	Created by Sandra Sowah
#	APC 524 - Final Project
#	Due: January 15, 2014


import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib 
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar 
from matplotlib.figure import Figure 
from matplotlib.legend_handler import HandlerLine2D

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
        MainWindow.resize(1296, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1296, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1296, 800))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(250, 71))
        self.label.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtGui.QFrame.WinPanel)
        self.label.setFrameShadow(QtGui.QFrame.Raised)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(321, 71))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(321, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(20, 431))
        self.line.setMaximumSize(QtCore.QSize(20, 431))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 5, 1)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(250, 71))
        self.label_2.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtGui.QFrame.Raised)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(321, 71))
        self.lineEdit.setMaximumSize(QtCore.QSize(321, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.formLayout_5.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.checkBox_3 = QtGui.QCheckBox(self.splitter)
        self.checkBox_3.setMinimumSize(QtCore.QSize(191, 61))
        self.checkBox_3.setMaximumSize(QtCore.QSize(191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox = QtGui.QCheckBox(self.splitter)
        self.checkBox.setMinimumSize(QtCore.QSize(191, 61))
        self.checkBox.setMaximumSize(QtCore.QSize(191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.splitter)
        self.checkBox_2.setMinimumSize(QtCore.QSize(191, 61))
        self.checkBox_2.setMaximumSize(QtCore.QSize(191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.splitter)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(250, 71))
        self.label_7.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_7.setFrameShadow(QtGui.QFrame.Raised)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(331, 71))
        self.comboBox.setMaximumSize(QtCore.QSize(331, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setMaxCount(10)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.LabelRole, self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(250, 71))
        self.label_8.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_8.setFrameShadow(QtGui.QFrame.Raised)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(331, 71))
        self.comboBox_2.setMaximumSize(QtCore.QSize(331, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.formLayout_3.setLayout(1, QtGui.QFormLayout.LabelRole, self.formLayout_2)
        self.formLayout_5.setLayout(2, QtGui.QFormLayout.LabelRole, self.formLayout_3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(600, 91))
        self.pushButton.setMaximumSize(QtCore.QSize(600, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.gridLayout.addLayout(self.formLayout_5, 0, 2, 5, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(250, 71))
        self.label_3.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtGui.QFrame.Raised)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(321, 71))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(321, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(250, 71))
        self.label_4.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_4.setFrameShadow(QtGui.QFrame.Raised)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(321, 71))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(321, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(250, 71))
        self.label_5.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_5.setFrameShadow(QtGui.QFrame.Raised)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(321, 71))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(321, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(250, 71))
        self.label_6.setMaximumSize(QtCore.QSize(250, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_6.setFrameShadow(QtGui.QFrame.Raised)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(321, 71))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(321, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.formLayout_8 = QtGui.QFormLayout()
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(300, 71))
        self.label_9.setMaximumSize(QtCore.QSize(300, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_9.setFrameShadow(QtGui.QFrame.Raised)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(920, 71))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(920, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.formLayout_8.setLayout(0, QtGui.QFormLayout.LabelRole, self.formLayout_4)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(300, 71))
        self.label_10.setMaximumSize(QtCore.QSize(300, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_10.setFrameShadow(QtGui.QFrame.Raised)
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(920, 71))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(920, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.formLayout_8.setLayout(1, QtGui.QFormLayout.LabelRole, self.formLayout_6)
        self.formLayout_7 = QtGui.QFormLayout()
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(300, 71))
        self.label_11.setMaximumSize(QtCore.QSize(300, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_11.setFrameShadow(QtGui.QFrame.Raised)
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_9 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(920, 71))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(920, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_9)
        self.formLayout_8.setLayout(2, QtGui.QFormLayout.LabelRole, self.formLayout_7)
        self.gridLayout.addLayout(self.formLayout_8, 5, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1296, 47))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionImport_Data_File = QtGui.QAction(MainWindow)
        self.actionImport_Data_File.setObjectName(_fromUtf8("actionImport_Data_File"))
        self.actionImport_Constraints_File = QtGui.QAction(MainWindow)
        self.actionImport_Constraints_File.setObjectName(_fromUtf8("actionImport_Constraints_File"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionImport_Data_File)
        self.menuFile.addAction(self.actionImport_Constraints_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

	
	def openFileDialog_Data():
		global data_file
		path = str(QtGui.QFileDialog.getOpenFileName())
		result = os.path.basename(path);
		data_file = path
		

	def openFileDialog_Constraints():
		global constraints_file
		path = str(QtGui.QFileDialog.getOpenFileName())
		result = os.path.basename(path);
		constraints_file = path

		
	def Ebola_Simulator():  
		if self.checkBox.isChecked():
			plot_fit = True
		else:
			plot_fit = False

		if self.checkBox_2.isChecked():
			plot = True
		else:
			plot = False
		
		if self.checkBox_3.isChecked():
			disp = True
		else:
			disp = False
				
		N=int(self.lineEdit.text())
		N_samples=int(self.lineEdit_2.text())
		t_final=int(self.lineEdit_3.text())
		I_init=int(self.lineEdit_4.text())
		trajectories=int(self.lineEdit_5.text())
		n_threads=int(self.lineEdit_6.text())

		country=str(self.comboBox.currentText())
		out_iv_file=str(self.lineEdit_7.text())
		out_noiv_file=str(self.lineEdit_8.text())
		figure_file=str(self.lineEdit_9.text())

		valid_interventions=[str(self.comboBox_2.currentText())]
		
		if 'all' == self.comboBox_2.currentText():
			valid_interventions= str(self.comboBox_2.currentText())
		else:
			valid_interventions= str(self.comboBox_2.currentText()).split()	
		
		print [N_samples, t_final, I_init, trajectories, n_threads, N, valid_interventions, country, constraints_file, data_file, disp, plot_fit, plot, out_iv_file, out_noiv_file, figure_file]
		
		from ebolaopt import optimize
		
		alloc, cost = optimize(N=N,N_samples=N_samples, t_final=t_final, I_init=I_init, trajectories=trajectories,\
        valid_interventions=valid_interventions, country=country, constraints_file=constraints_file, data_file=data_file,\
         disp=disp, plot_fit=plot_fit, plot=plot, n_threads=n_threads)
		
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Ebola_Simulator)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox_2.isChecked)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox_3.isChecked)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.checkBox.isChecked)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.comboBox_2.currentText)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.comboBox.currentText)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionImport_Constraints_File, QtCore.SIGNAL(_fromUtf8("triggered()")), openFileDialog_Constraints)
        QtCore.QObject.connect(self.actionImport_Data_File, QtCore.SIGNAL(_fromUtf8("triggered()")), openFileDialog_Data)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_2.setText)
        QtCore.QObject.connect(self.lineEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_7.setText)
        QtCore.QObject.connect(self.lineEdit_8, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_8.setText)
        QtCore.QObject.connect(self.lineEdit_9, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_9.setText)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit.setText)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_3.setText)
        QtCore.QObject.connect(self.lineEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_4.setText)
        QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_5.setText)
        QtCore.QObject.connect(self.lineEdit_6, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.lineEdit_6.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ebola_Simulator", None))
        self.label.setText(_translate("MainWindow", "N_samples", None))
        self.lineEdit_2.setText(_translate("MainWindow", "200", None))
        self.label_2.setText(_translate("MainWindow", "N", None))
        self.lineEdit.setText(_translate("MainWindow", "200000", None))
        self.checkBox_3.setText(_translate("MainWindow", "disp", None))
        self.checkBox.setText(_translate("MainWindow", "plot_fit", None))
        self.checkBox_2.setText(_translate("MainWindow", "plot", None))
        self.label_7.setText(_translate("MainWindow", "country", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sierra Leone", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Guinea", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Liberia", None))
        self.label_8.setText(_translate("MainWindow", "valid_iv", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "all", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "beta_H delta_2", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "beta_H theta_1", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "delta_2 theta_1", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "delta_2", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "beta_H", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "theta_1", None))
        self.pushButton.setText(_translate("MainWindow", "Run Simulation", None))
        self.label_3.setText(_translate("MainWindow", "t_final", None))
        self.lineEdit_3.setText(_translate("MainWindow", "250", None))
        self.label_4.setText(_translate("MainWindow", "I_init", None))
        self.lineEdit_4.setText(_translate("MainWindow", "3", None))
        self.label_5.setText(_translate("MainWindow", "Trajectories", None))
        self.lineEdit_5.setText(_translate("MainWindow", "20", None))
        self.label_6.setText(_translate("MainWindow", "n_threads", None))
        self.lineEdit_6.setText(_translate("MainWindow", "1", None))
        self.label_9.setText(_translate("MainWindow", "out_noiv_file", None))
        self.lineEdit_7.setText(_translate("MainWindow", "out_noiv.csv", None))
        self.label_10.setText(_translate("MainWindow", "out_iv_file", None))
        self.lineEdit_8.setText(_translate("MainWindow", "out_iv.csv", None))
        self.label_11.setText(_translate("MainWindow", "figure_file", None))
        self.lineEdit_9.setText(_translate("MainWindow", "out.png", None))
        self.menuFile.setTitle(_translate("MainWindow", "Menu", None))
        self.actionImport_Data_File.setText(_translate("MainWindow", "Import Data File", None))
        self.actionImport_Constraints_File.setText(_translate("MainWindow", "Import Constraints File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


def run():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()

