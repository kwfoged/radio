import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PyQt4.QtCore import QTimer

class mainWindow(QtGui.QTabWidget):
    def __init__(self, parent = None):
        super(mainWindow, self).__init__(parent)



## ---------------------- TAB 1--------------------------------------

        
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

        self.RunPlots = False
        self.NoOfPlots = 8
        self.PlotNo = {}
        self.unitNo = {}
        self.comboColor2 = {}
        self.comboStyle2 = {}
        self.sensorData = {}
        self.checkboxShow = {}
        self.comboCOMport = 1
        self.comboBaudRate = 9600
        
        self.plotColor = ['k','k','b','r','y','g','b','r','y','g'] 
        self.plotStyle = ['-','-','-','-','-','-','-','-','-','-']
        self.usePlot = ['1','1','1','1','1','1','1','1','1','1'] 

        # Tab 1        
        self.tab1 = QtGui.QWidget()
        self.addTab(self.tab1,"Incomming Data")

        self.figure = plt.figure(figsize=(30,15))
        self.resize(1200,700)
        self.canvas = FigureCanvas(self.figure)

        
        # Label
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
	
        l1.setAlignment(Qt.AlignLeft)
        l2.setAlignment(Qt.AlignLeft)
        l3.setAlignment(Qt.AlignLeft)
        l4.setAlignment(Qt.AlignLeft)
        l5.setAlignment(Qt.AlignLeft)
        l6.setAlignment(Qt.AlignLeft)
        l7.setAlignment(Qt.AlignLeft)
        
        ## Create Grid for   
        grid = QGridLayout()

        grid.addWidget(l1,1,1)
        grid.addWidget(l2,1,2)
        grid.addWidget(l3,1,3)
        grid.addWidget(l4,1,4)
        grid.addWidget(l5,1,5)
        grid.addWidget(l6,1,6)
        grid.addWidget(l7,1,7)

        for i in range(2,self.NoOfPlots + 1):
            # Checkboxes
            self.checkboxShow[i] = QtGui.QCheckBox('', self)
            self.checkboxShow[i].setChecked(True)
           
            
            # Combo box 1 - Plot nr
            self.PlotNo[i] = QtGui.QComboBox(self)
            self.PlotNo[i].addItem("1")
            self.PlotNo[i].addItem("2")
            self.PlotNo[i].setFixedWidth(50)

            # Combo box 2 - Slave nr
            self.unitNo[i] = QtGui.QComboBox(self)
            self.unitNo[i].addItem("1")
            self.unitNo[i].addItem("2")
            self.unitNo[i].addItem("3")
            self.unitNo[i].addItem("4")
            self.unitNo[i].addItem("5")
            self.unitNo[i].addItem("6")
            self.unitNo[i].addItem("7")
            self.unitNo[i].setFixedWidth(50)

            # Combo box 3 - Sensor Data
            self.sensorData[i] = QtGui.QComboBox(self)
            self.sensorData[i].addItem("Temperature 1")
            self.sensorData[i].addItem("Temperature 2")
            self.sensorData[i].addItem("Temperature 3")
            self.sensorData[i].addItem("Humidity 1")
            self.sensorData[i].addItem("Light 1")
            self.sensorData[i].setFixedWidth(150)

            # Offset
            line = QtGui.QLineEdit(self)
            line.setFixedWidth(50)

            # Plot Color
            colorPath = "C:/Users/KWFO/Desktop/image_test/"
            self.comboColor2[i] = QtGui.QComboBox(self)
            self.comboColor2[i].addItem(QIcon(colorPath + "black.png"), "")
            self.comboColor2[i].addItem(QIcon(colorPath + "blue.png"), "")
            self.comboColor2[i].addItem(QIcon(colorPath + "red1.png"), "")
            #self.comboColor2[i].addItem(QIcon(colorPath + "yellow1.png"),"")
            self.comboColor2[i].addItem(QIcon(colorPath + "green.png"), "")
            self.comboColor2[i].addItem(QIcon(colorPath + "orange.png"), "")
            self.comboColor2[i].addItem(QIcon(colorPath + "magenta.png"), "")
            self.comboColor2[i].addItem(QIcon(colorPath + "cyan2.png"), "")
            self.comboColor2[i].setFixedWidth(50)
            self.comboColor2[i].setCurrentIndex(i-2) # Set different color for all at startup

            # Plot Style
            self.comboStyle2[i] = QtGui.QComboBox(self)
            self.comboStyle2[i].addItem("solid")
            self.comboStyle2[i].addItem("dashed")
            self.comboStyle2[i].addItem("dots")
            self.comboStyle2[i].addItem("solid + dots")
            self.comboStyle2[i].setFixedWidth(90)

            grid.addWidget(self.checkboxShow[i],i,1)
            grid.addWidget(self.unitNo[i],i,2)
            grid.addWidget(self.sensorData[i],i,3)
            grid.addWidget(self.PlotNo[i],i,4)
            grid.addWidget(line,i,5)
            grid.addWidget(self.comboColor2[i],i,6)
            grid.addWidget(self.comboStyle2[i],i,7)


        
        
    

        b1 = QPushButton("Plot incomming data")
        b1.clicked.connect(self.b1_clicked)
        b1.setFixedHeight(40)
        b1.setFixedWidth(125)
        
        b2 = QPushButton("Stop plotting")
        b2.clicked.connect(self.b2_clicked)
        b2.setFixedHeight(40)
        b2.setFixedWidth(125)

        serial_Setup = QGridLayout()
        com_port = QLabel()
        com_port.setText("COM Port")
        baudrate = QLabel()
        baudrate.setText("Baud Rate")
        self.comboCOMport = QtGui.QComboBox(self)
        self.comboCOMport.addItem("COM1")
        self.comboCOMport.addItem("COM2")
        self.comboCOMport.addItem("COM3")
        self.comboCOMport.addItem("COM4")
        self.comboCOMport.addItem("COM5")
        self.comboCOMport.addItem("COM6")
        self.comboCOMport.addItem("COM7")
        self.comboCOMport.addItem("COM8")
        self.comboCOMport.addItem("COM9")
        self.comboBaudRate = QtGui.QComboBox(self)
        self.comboBaudRate.addItem("9600")
        self.comboBaudRate.addItem("18200")
        self.comboBaudRate.addItem("36400")
        self.comboBaudRate.addItem("72800")
        self.comboBaudRate.addItem("115600")
        serial_Setup.addWidget(com_port,1,1)
        serial_Setup.addWidget(self.comboCOMport,2,1)
        serial_Setup.addWidget(baudrate,1,2)
        serial_Setup.addWidget(self.comboBaudRate,2,2)
        
        buttons = QtGui.QHBoxLayout()
        buttons.addWidget(b1)
        buttons.addWidget(b2)
        buttons.addSpacing(100)
        buttons.addLayout(serial_Setup)
        buttons.addStretch()

        self.show_plot_1 = QtGui.QCheckBox('Show Plot 1', self)
        self.show_plot_1.setChecked(True)
        self.show_plot_2 = QtGui.QCheckBox('Show Plot 2', self)
        self.show_plot_2.setChecked(True)
        
        # Input Data on Left Side Of Screen
        input_data = QtGui.QVBoxLayout()
        input_data.addLayout(buttons)
        input_data.addSpacing(20)
        input_data.addWidget(self.show_plot_1)
        input_data.addWidget(self.show_plot_2)
        input_data.addSpacing(40)
        input_data.addLayout(grid)
        input_data.addStretch()

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(input_data)
        hbox.addWidget(self.canvas)   

        
        self.tab1.setLayout(hbox)
## ---------------------------------------------------


        # Tab 2
        self.txt_data = {}
        self.txt_data2 = {}
        #self.lineEdit = ''
        
        self.tab2 = QtGui.QWidget()
        self.addTab(self.tab2,"Load Saved Data")       


        buttonLoadData = QPushButton("Load Data")
        buttonLoadData.clicked.connect(self.loadData_clicked)
        buttonLoadData.setFixedHeight(40)
        buttonLoadData.setFixedWidth(125)
        

        self.figure2 = plt.figure(figsize=(30,15))
        self.canvas2 = FigureCanvas(self.figure2)

        tab2_hbox = QtGui.QHBoxLayout()
        tab2_hbox.addWidget(buttonLoadData)
        tab2_hbox.addWidget(self.canvas2)  

        self.tab2.setLayout(tab2_hbox)

        # Plot First Time
        self.plot()
        
        #self.load_data()
        #self.tab2_plot()

        
# ------------- Plotting On Tab 1-------------------------
    def plot(self):
        data = []
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        data.append([random.random() for i in range(10)])
        
##        ax = self.figure.add_subplot(211)
##        ax.hold(False)
        self.figure.clf()
        
        if (self.show_plot_1.isChecked() and self.show_plot_2.isChecked()):
            ax = self.figure.add_subplot(211)
            ax.hold(False)
            
            ax2 = self.figure.add_subplot(212)
            ax2.hold(False)
        else: 
            ax = self.figure.add_subplot(111)
            ax.hold(False)


        for i in range(2,self.NoOfPlots + 1):
            if(self.checkboxShow[i].isChecked()):
                if(self.usePlot[i]==1 and self.show_plot_1.isChecked()):
                    ax.plot(data[i], self.plotStyle[i], color=self.plotColor[i])
                    ax.hold(True)
                elif(self.usePlot[i]==2 and self.show_plot_2.isChecked()):
                    if (self.show_plot_1.isChecked()):
                        ax2.plot(data[i], self.plotStyle[i], color=self.plotColor[i])
                        ax2.hold(True)
                    else:
                        ax.plot(data[i], self.plotStyle[i], color=self.plotColor[i])
                        ax.hold(True)
        
        
        self.canvas.draw()
        
## ---------------------------------------------------


## ------------- Plotting On Tab 2 -------------------------
    def tab2_plot(self):

        self.figure2.clf()
        tab2_data =  self.txt_data2.data1.values 
        tab2_ax = self.figure2.add_subplot(111)
        tab2_ax.plot(tab2_data, '--', color='blue')

        self.canvas2.draw()
## ---------------------------------------------------        


## ---------- Functions for Tab 1 --------------------        
    def b1_clicked(self):

        for i in range(2,self.NoOfPlots + 1):
            color_index = self.comboColor2[i].currentIndex()
            style_index = self.comboStyle2[i].currentIndex()
            plot_index =self.PlotNo[i].currentIndex()
        
            if color_index == 0:
                self.plotColor[i] = "black"
            elif color_index==1:
                self.plotColor[i] = "blue"
            elif color_index==2:
                self.plotColor[i] = "red"
            elif color_index==3:
                self.plotColor[i] = "green"
            elif color_index==4:
                self.plotColor[i] = "orange"
            elif color_index==5:
                self.plotColor[i] = "magenta"
            elif color_index==6:
                self.plotColor[i] = "cyan" 

            if style_index == 0:
                self.plotStyle[i] = "-"
            elif style_index==1:
                self.plotStyle[i] = "--"
            elif style_index==2:
                self.plotStyle[i] = "*"
            elif style_index==3:
                self.plotStyle[i] = "-*"
 
            self.usePlot[i] = plot_index + 1

            self.RunPlots = True
            #print (str(i) + "  " + self.plotColor[i])


    def b2_clicked(self):
        self.RunPlots = False


    def tick(self):
        if(self.RunPlots == True):
            self.plot()
## ---------------------------------------------------  

## ---------- Functions for Tab 2 --------------------

    # # def load_data(self):            
        # # self.txt_data = pd.read_csv('C:\Python27\Lib\site-packages\visual\examples\2018-06-24-12.txt', sep=",", header=None)
        # # self.txt_data.columns = ["date", "time", "data1", "data2","data3","data4"]
        # # print self.txt_data.data1.values


    def loadData_clicked(self):
        self.lineEdit = QFileDialog.getOpenFileNames()

        for i in range(1,len(self.lineEdit) + 1):
            str_path = str(self.lineEdit[i - 1])
            result = str_path.split("\\")
            result = result[len(result) - 1]
            #self.txt_data2 = pd.read_csv(str(result), sep=",", keep_default_na=False, na_values=[])
			#self.txt_data2 = pd.read_csv(str(result), sep=",", skiprows=(1), header=(0))
            self.txt_data2 = pd.read_csv(str_path, sep=",", skiprows=(1), header=(0))
            self.txt_data2.columns = ["date", "time", "data1", "data2","data3","data4"]
            #self.txt_data2.dropna(how='any')
            self.txt_data2.fillna(0, inplace=True)
            #filtered = self.txt_data2[(self.txt_data2['data1'] > 10)]
            print self.txt_data2
            
        self.tab2_plot()    



def main():
	#raw_input('2222dsada')
	app = QtGui.QApplication(sys.argv)
	main = mainWindow()
	main.show()
	#raw_input('dsada')
	sys.exit(app.exec_())

if __name__ == '__main__':
    main()
