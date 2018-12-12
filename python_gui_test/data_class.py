# data_class.py
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DataClass():
	def __init__(self, num_plots):
	
		self.NoOfPlots = num_plots
		self.PlotNo = {}
		self.unitNo = {}
		self.color = {}
		self.style = {}
		self.sensorData = {}
		self.checkboxShow = {}
