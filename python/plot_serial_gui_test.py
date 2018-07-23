import sys
import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import time
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random

from PyQt4.QtCore import QTimer

data1_arr = []
data2_arr = []
data3_arr = []
data4_arr = []
data1 = 0
data2 = 0
data3 = 0
data4 = 0
arduinoData = serial.Serial('com6', 9600) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
time_vec = []
t=0



class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.dataArray = []
        self.data1_arr = []
        self.data2_arr = []
        self.time_vec = []
        self.data1 = 0.0
        self.data2 = 0.0
        self.t = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(100)

    def tick(self):
        
        while (arduinoData.inWaiting()==0): #Wait here until there is data
            pass #do nothing

        arduinoString = arduinoData.readline() #read the line of text from the serial port
        if (arduinoString.find('#end')!=-1):
            arduinoData.flush()
            arduinoData.flushInput()
            arduinoData.flushOutput()

        print arduinoString

        dataArray = arduinoString.split(',')

        if any(test < 0 for test in dataArray):
            self.data1 = self.data1
            self.data2 = self.data2
        elif (dataArray[0] == '3'):    
            self.data1 = float( dataArray[3])            #Convert first element to floating number and put in temp
        elif (dataArray[0] == '4'):
            self.data2 = float( dataArray[1])
        else:
            self.data1 = self.data1
            self.data2 = self.data2
        

        self.t = self.t + 1
        self.data1_arr.append(self.data1)                     #Build our tempF array by appending temp readings
        self.data2_arr.append(self.data2)                     #Building our pressure array by appending P readings
        self.time_vec.append(self.t)

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.plot(self.time_vec, self.data2_arr,  '*-')

        # refresh canvas
        self.canvas.draw()

        if(self.t>50):                            #If you have 50 or more points, delete the first one from the array
            self.time_vec.pop(0)                       #This allows us to just see the last 50 data points
            self.data1_arr.pop(0)
            self.data2_arr.pop(0)

    
    
    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.plot(self.data1_arr,  '*-')

        # refresh canvas
        self.canvas.draw()

        if(self.t>50):                            #If you have 50 or more points, delete the first one from the array
            time_vec.pop(0)                       #This allows us to just see the last 50 data points
            data1_arr.pop(0)
            data2_arr.pop(0)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())






 
def run_serial_test(void):
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing

    arduinoString = arduinoData.readline() #read the line of text from the serial port
    if (arduinoString.find('#end')!=-1):
        arduinoData.flush()
        arduinoData.flushInput()
        arduinoData.flushOutput()

    ts = time.gmtime()
    #print(time.strftime("%Y-%m-%d %H:%M:%S ", ts))
    #print(arduinoString);

    filename =  time.strftime("%Y-%m-%d-%H",ts) + ".txt";
    f = open(filename, "a")
    f.write(time.strftime("%Y-%m-%d,%H:%M:%S , ", ts))
    f.write(arduinoString)
    f.close()


    
    # When a '#end' is recived put in array and plot  
    if (arduinoString.find('#end')!=-1):


        if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
            time_vec.pop(0)                       #This allows us to just see the last 50 data points
            data1_arr.pop(0)
            data2_arr.pop(0)
            data3_arr.pop(0)
            data4_arr.pop(0)


        print("data1 a: " + str(data1))
        print("data2 a: " + str(data2))
        print("data3 a: " + str(data3))
        
        t = t + 1
        data1_arr.append(data1)                     #Build our tempF array by appending temp readings
        data2_arr.append(data2)                     #Building our pressure array by appending P readings
        data3_arr.append(data3)
        data4_arr.append(data4)
        time_vec.append(t)


        plt.clf()
        plt.ylim(20,40)                                 #Set y min and max values
        plt.title('My Live Streaming Sensor Data')      #Plot the title
        plt.grid(True)                                  #Turn the grid on
        plt.ylabel('Unit 1: Temp 2 C')                            #Set ylabels
        #plt.plot(tempF, 'r-', label='Degrees F')       #plot the temperature
        plt.plot(time_vec,data1_arr,'r-', label='Unit 1: Temp 2 C')                               #plot the temperature
        plt.legend(loc='upper left')                    #plot the legend
        plt2=plt.twinx()                                #Create a second y axis
        plt.ylim(0,1000)                           #Set limits of second y axis- adjust to readings you are getting
        #plt2.plot(pressure, 'b-', label='Pressure (Pa)') #plot pressure data
        plt2.plot(time_vec,data2_arr, 'b-', label='Unit 2: Potmeter')                           #plot pressure data
        plt2.set_ylabel('Unit 2: Potmeter')                    #label second y axis
        plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
        plt2.legend(loc='upper right')                  #plot the legend
        plt.pause(1e-3)  # allows time to draw
        #drawnow(makeFig)                       #Call drawnow to update our live graph
        plt.show()
        plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
        cnt = cnt+1
        
    else:    # When a '#end' is not recived put local variable
        dataArray = arduinoString.split(',')   #Split it into an array called dataArray
        #print(dataArray)
        #print(dataArray[2])
        if (dataArray[0]=='1'):
            data1 = float( dataArray[2])            #Convert first element to floating number and put in temp
        elif (dataArray[0]=='2'):
            data2 = float( dataArray[1])
        elif (dataArray[0]=='3'):
            data3 = float( dataArray[1]) 


        print("data1: " + str(data1))
        print("data2: " + str(data2))
        print("data3: " + str(data3))
        data4 = float(52.0)
        
        



    

