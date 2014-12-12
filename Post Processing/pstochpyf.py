#!/usr/bin/python 

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
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(630, 1200, 844, 40))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton_4 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.horizontalLayout.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.horizontalLayout.addWidget(self.radioButton_6)
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 120, 1841, 1041))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton_4)
        self.EbolaPlot = QtGui.QLabel(self.layoutWidget1)
        self.EbolaPlot.setMinimumSize(QtCore.QSize(1637, 1000))
        self.EbolaPlot.setMaximumSize(QtCore.QSize(1640, 16777215))
        self.EbolaPlot.setObjectName(_fromUtf8("EbolaPlot"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.EbolaPlot)
        self.layoutWidget2 = QtGui.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(34, 23, 1841, 59))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.InputFile = QtGui.QPushButton(self.layoutWidget2)
        self.InputFile.setMaximumSize(QtCore.QSize(187, 500))
        self.InputFile.setObjectName(_fromUtf8("InputFile"))
        self.horizontalLayout_2.addWidget(self.InputFile)
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setMaximumSize(QtCore.QSize(1751, 60))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)

	def setLabelText():
		pathname = os.path.dirname(sys.argv[0]) 
		mytext = 'File Imported from Directory: '  + str(os.path.realpath(pathname))
		self.label.setText(str(mytext))
	
	def showGraph():
		my_matrix = np.loadtxt('heat_omp.out')
		my_matrix = my_matrix.reshape((128, 128))
		#print my_matrix.shape
		plt.contour(my_matrix)
		plt.ylabel('Number of Infections [thousands]')
		plt.xlabel('Time [days]')
		plt.title('Ebola Infections Reported Over Time')
		#plt.plot(my_matrix[:,0], my_matrix[:,1])
		#plt.show()
		plt.savefig('Graph1.png')
		self.EbolaPlot.setPixmap(QtGui.QPixmap(_fromUtf8("Graph1.png")))
		self.EbolaPlot.setScaledContents(True)
		
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), showGraph)
        QtCore.QObject.connect(self.InputFile, QtCore.SIGNAL(_fromUtf8("clicked()")), setLabelText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Ebola Data Projections", None))
        self.radioButton_4.setText(_translate("Dialog", "Import Data CSV", None))
        self.radioButton_5.setText(_translate("Dialog", "Import Data ACII", None))
        self.radioButton_6.setText(_translate("Dialog", "Import Data Binary", None))
        self.pushButton_4.setWhatsThis(_translate("Dialog", "Data Plots", None))
        self.pushButton_4.setText(_translate("Dialog", "Graph", None))
        self.InputFile.setWhatsThis(_translate("Dialog", "Imports File for Analysis", None))
        self.InputFile.setText(_translate("Dialog", "Import File", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))

			
	def Import_CSV(self):
		f = open('heat_omp.out', 'r')
		f1 = open('EbolaDataProjection.csv', 'w')
		f1.write(f.read())
		f1.close()
		f.close()
	self.radioButton_4.clicked.connect(Import_CSV)

	def Import_ASCII(self):
		f = open('heat_omp.out', 'r')
		f1 = open('EbolaDataProjection.txt', 'w')
		f1.write(f.read())
		f1.close()
		f.close()
	self.radioButton_5.clicked.connect(Import_ASCII)

	
	def Import_Binary(self):
		f = open('heat_omp.out', 'r')
		f1 = open('EbolaDataProjection.bin', 'wb')
		f1.write(f.read())
		f1.close()
		f.close()
	self.radioButton_6.clicked.connect(Import_Binary)
	

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

