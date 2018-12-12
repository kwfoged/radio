# actions_class.py
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ActionClass(QtGui.QTabWidget):
    def __init__(self,tab_pointer, data_ref, parent = None):
		super(ActionClass, self).__init__(parent)
	
		l1 = QLabel()
		l2 = QLabel()
		l3 = QLabel()
		l4 = QLabel()
		l5 = QLabel()
		l6 = QLabel()
		l7 = QLabel()

		l1.setText("Show")
		l2.setText("Unit No")
		l3.setText("Data")
		l4.setText("Plot No")
		l5.setText("Offset")
		l6.setText("Plot Color")
		l7.setText("Plot Style")
		
		self.grid = QGridLayout()

		self.grid.addWidget(l1,1,1)
		self.grid.addWidget(l2,1,2)
		self.grid.addWidget(l3,1,3)
		self.grid.addWidget(l4,1,4)
		self.grid.addWidget(l5,1,5)
		self.grid.addWidget(l6,1,6)
		self.grid.addWidget(l7,1,7)
		
		for i in range(2,data_ref.NoOfPlots + 1):
			# Checkboxes
			data_ref.checkboxShow[i] = QtGui.QCheckBox('', self)
			data_ref.checkboxShow[i].setChecked(True)
			
			# Combo box 1 - Plot nr
			data_ref.PlotNo[i] = QtGui.QComboBox(self)
			data_ref.PlotNo[i].addItem("1")
			data_ref.PlotNo[i].addItem("2")
			data_ref.PlotNo[i].setFixedWidth(50)

			# Combo box 2 - Slave nr
			data_ref.unitNo[i] = QtGui.QComboBox(self)
			data_ref.unitNo[i].addItem("1")
			data_ref.unitNo[i].addItem("2")
			data_ref.unitNo[i].addItem("3")
			data_ref.unitNo[i].addItem("4")
			data_ref.unitNo[i].addItem("5")
			data_ref.unitNo[i].addItem("6")
			data_ref.unitNo[i].addItem("7")
			data_ref.unitNo[i].setFixedWidth(50)

			# Combo box 3 - Sensor Data
			data_ref.sensorData[i] = QtGui.QComboBox(self)
			data_ref.sensorData[i].addItem("Temperature 1")
			data_ref.sensorData[i].addItem("Temperature 2")
			data_ref.sensorData[i].addItem("Temperature 3")
			data_ref.sensorData[i].addItem("Humidity 1")
			data_ref.sensorData[i].addItem("Light 1")
			data_ref.sensorData[i].setFixedWidth(150)

			# Offset
			line = QtGui.QLineEdit(self)
			line.setFixedWidth(50)

			# Plot Color
			colorPath = "C:/Users/KWFO/Desktop/Python_GUI/plot_colors/" 
			data_ref.color[i] = QtGui.QComboBox(self)
			data_ref.color[i].addItem(QIcon(colorPath + "black.png"), "")
			data_ref.color[i].addItem(QIcon(colorPath + "blue.png"), "")
			data_ref.color[i].addItem(QIcon(colorPath + "red1.png"), "")
			data_ref.color[i].addItem(QIcon(colorPath + "green.png"), "")
			data_ref.color[i].addItem(QIcon(colorPath + "orange.png"), "")
			data_ref.color[i].addItem(QIcon(colorPath + "magenta.png"), "")
			data_ref.color[i].addItem(QIcon(colorPath + "cyan2.png"), "")
			data_ref.color[i].setFixedWidth(50)
			data_ref.color[i].setCurrentIndex(i-2) # Set different color for all at startup

			# Plot Style
			data_ref.style[i] = QtGui.QComboBox(self)
			data_ref.style[i].addItem("solid")
			data_ref.style[i].addItem("dashed")
			data_ref.style[i].addItem("dots")
			data_ref.style[i].addItem("solid + dots")
			data_ref.style[i].setFixedWidth(90)

			self.grid.addWidget(data_ref.checkboxShow[i],i,1)
			self.grid.addWidget(data_ref.unitNo[i],i,2)
			self.grid.addWidget(data_ref.sensorData[i],i,3)
			self.grid.addWidget(data_ref.PlotNo[i],i,4)
			self.grid.addWidget(line,i,5)
			self.grid.addWidget(data_ref.color[i],i,6)
			self.grid.addWidget(data_ref.style[i],i,7)
		
