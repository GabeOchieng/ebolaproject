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
        MainWindow.resize(1406, 800)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 5000))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.InputFile = QtGui.QPushButton(self.centralwidget)
        self.InputFile.setMaximumSize(QtCore.QSize(241, 16777215))
        self.InputFile.setObjectName(_fromUtf8("InputFile"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.InputFile)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(241, 91))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pushButton_2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        #self.label_2.setMaximumSize(QtCore.QSize(1381, 891))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_2)
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.radioButton_3)
        MainWindow.setCentralWidget(self.centralwidget)

	def setLabelText():
		pathname = os.path.dirname(sys.argv[0]) 
		mytext = 'File Imported from Directory: '  + str(os.path.realpath(pathname))
		self.label.setText(str(mytext))
	
	def showGraph():
		my_matrix = np.loadtxt('epidemic_no_iv.csv', delimiter = ',',skiprows=1)
		my_matrix2 = np.loadtxt('epidemic_opt_iv.csv', delimiter = ',',skiprows=1)
		#my_matrix = my_matrix.reshape((128, 128))
		#print my_matrix.shape
		#plt.plot(my_matrix[:,0], my_matrix[:,4],my_matrix[:,0], my_matrix[:,6],my_matrix[:,0], my_matrix[:,8],my_matrix[:,0], my_matrix[:,10])
		#plt.contour(my_matrix)
		#plt.ylabel('Number of Infections [thousands]')
		#plt.xlabel('Time [days]')
		#plt.title('Ebola Infections Reported Over Time')
		

		f, axarr = plt.subplots(2, 2)
		#axarr2 = axarr[0,1].twinx()
		#axarr3 = axarr[1,1].twinx()
		ploty = [my_matrix[:,3], my_matrix[:,5],my_matrix[:,7],my_matrix[:,9],my_matrix[:,3]+my_matrix[:,5]+my_matrix[:,7]+my_matrix[:,9]]
		plotx = [my_matrix2[:,3], my_matrix2[:,5],my_matrix2[:,7],my_matrix2[:,9],my_matrix2[:,3]+my_matrix2[:,5]+my_matrix2[:,7]+my_matrix2[:,9]]
		labels = ['E', 'I', 'H', 'F', 'Total']
		
		for ploty_arr, label in zip(ploty, labels):
			axarr[0, 0].plot(my_matrix[:,0], ploty_arr, label=label)
			
		for plotx_arr, label in zip(plotx, labels):	
			axarr[1, 0].plot(my_matrix2[:,0], plotx_arr, label=label)
	
	
		#axarr[0, 0].plot(my_matrix[:,0], my_matrix[:,4],my_matrix[:,0], my_matrix[:,6],my_matrix[:,0], my_matrix[:,8],my_matrix[:,0], my_matrix[:,10])
		axarr[0, 0].set_title('Ebola Infections Reported Over Time - No Optimization')
		axarr[0, 0].set_xlabel('Time [days]')
		axarr[0, 0].set_ylabel('Number Infected')
		axarr[0,0].legend(loc=0)
		axarr[0, 1].plot(my_matrix[:,0], my_matrix[:,1],label='Suscept')
		#axarr2.plot(my_matrix[:,0], my_matrix[:,11],label='Recov')
		axarr[0, 1].set_title('Ebola Susceptibilty Data - No Optimization')
		axarr[0, 1].set_xlabel('Time [days]')
		#axarr2.set_ylabel('Number Removed/Recovered')
		axarr[0,1].set_ylabel('Number Susceptibility')
		axarr[0,1].legend(loc=0)
		#axarr[1, 0].plot(my_matrix[:,0], my_matrix[:,4],my_matrix[:,0], my_matrix[:,6],my_matrix[:,0], my_matrix[:,8],my_matrix[:,0], my_matrix[:,10])
			
		axarr[1, 0].set_title('Ebola Infections Reported Over Time - Optimization Applied')
		axarr[1, 0].set_xlabel('Time [days]')
		axarr[1, 0].set_ylabel('Number Infected')
		axarr[1,0].legend(loc=0)
		axarr[1, 1].plot(my_matrix2[:,0], my_matrix2[:,1],label='Suscept')
		#axarr3.plot(my_matrix2[:,0], my_matrix2[:,11], label='Recov')
		axarr[1, 1].set_title('Ebola Susceptibilty Data - Optimization Applied')
		axarr[1, 1].set_xlabel('Time [days]')
		#axarr3.set_ylabel('Number Removed/Recovered')
		axarr[1,1].set_ylabel('Number Susceptibility')
		#axarr3.legend(loc=0)
		
		#plt.switch_backend('QT4Agg') #default on my system
		#print '#3 Backend:',plt.get_backend()
		figManager = plt.get_current_fig_manager()
		figManager.window.showMaximized()
		#figManager.frame.Maximize(True)  
		plt.legend()
		plt.show()
		fig = plt.gcf()
		fig.canvas.set_window_title('Ebola Data Projections For Country Chosen')
		fig.canvas.manager.window.activateWindow()
		fig.canvas.manager.window.raise_()
		plt.savefig('Graph1.png')
		self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Graph1.png")))
		#self.label_2.setScaledContents(True)
		

	def Ebola_Simulator():
		from ebolaopt import optimize
		
		alloc, cost = optimize(constraints_file="constraints.csv", \
                       data_file="cases.csv", t_final=300, \
                       country="Liberia", out_iv_file="liberia_iv.csv", \
                       out_noiv_file="liberia_noiv.csv", \
                       figure_file="liberia.png", \
                       valid_interventions=["beta_H", "theta_1"])
		
	
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.InputFile, QtCore.SIGNAL(_fromUtf8("clicked()")), setLabelText)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Ebola_Simulator)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.InputFile.setText(_translate("MainWindow", "Import File", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_2.setText(_translate("MainWindow", "Graph", None))
        self.label_2.setText(_translate("MainWindow", "TextLabel", None))
        self.radioButton.setText(_translate("MainWindow", "Import Data CSV", None))
        self.radioButton_2.setText(_translate("MainWindow", "Import Data ASCII", None))
        self.radioButton_3.setText(_translate("MainWindow", "Import Data Binary", None))


	def Import_CSV(self):
		f = open('output_File.out', 'r')
		f1 = open('EbolaDataProjection.csv', 'w')
		f1.write(f.read())
		f1.close()
		f.close()
	self.radioButton.clicked.connect(Import_CSV)

	def Import_ASCII(self):
		f = open('output_File.out', 'r')
		f1 = open('EbolaDataProjection.txt', 'w')
		f1.write(f.read())
		f1.close()
		f.close()
	self.radioButton_2.clicked.connect(Import_ASCII)

	
	def Import_Binary(self):
		f = open('output_File.out', 'r')
		f1 = open('EbolaDataProjection.bin', 'wb')
		f1.write(f.read())
		f1.close()
		f.close()
	self.radioButton_3.clicked.connect(Import_Binary)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

