import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import time
 
data1_arr = []
data2_arr = []
data3_arr = []
data4_arr = []
arduinoData = serial.Serial('com6', 9600) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
time_vec = []
t=0
data1 = 0.0
data2 = 0.0
data3 = 0.0

 
def makeFig(): #Create a function that makes our desired plot
    plt.ylim(0,1000)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temp F')                            #Set ylabels
    #plt.plot(tempF, 'r-', label='Degrees F')       #plot the temperature
    plt.plot(time_vec,data1_arr,'r-', label='Degrees F')                               #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(0,30)                           #Set limits of second y axis- adjust to readings you are getting
    #plt2.plot(pressure, 'b-', label='Pressure (Pa)') #plot pressure data
    plt2.plot(time_vec,data2_arr, 'b-', label='Pressure (Pa)')                           #plot pressure data
    plt2.set_ylabel('Pressrue (Pa)')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    
    
 
while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing

    arduinoString = arduinoData.readline() #read the line of text from the serial port
    arduinoData.flush()
    arduinoData.flushInput()
    arduinoData.flushOutput()
    ts = time.gmtime()
    print(time.strftime("%Y-%m-%d %H:%M:%S ", ts))
    print(arduinoString);

    filename =  time.strftime("%Y-%m-%d-%H",ts) + ".txt";
    f = open(filename, "a")
    f.write(time.strftime("%Y-%m-%d,%H:%M:%S , ", ts))
    f.write(arduinoString)
    f.close()

    dataArray = arduinoString.split(',')   #Split it into an array called dataArray
    
    if any(test < 0 for test in dataArray):
        data1 = data1
        data2 = data2
        data3 = data3
    elif (dataArray[0] == '3'):    
        data1 = float( dataArray[3])            #Convert first element to floating number and put in temp
    elif (dataArray[0] == '4'):
        data2 = float( dataArray[1])
        data3 = float( dataArray[2])
    else:
        data1 = data1
        data2 = data2
        data3 = data3
        
        #Convert second element to floating number and put in P
    #data3 = float( dataArray[6])
    #data4 = float( dataArray[7])

    t = t + 1
    data1_arr.append(data1)                     #Build our tempF array by appending temp readings
    data2_arr.append(data2)                     #Building our pressure array by appending P readings
    data3_arr.append(data3)
    #data4_arr.append(data4)
    time_vec.append(t)

    plt.clf()
    plt.ylim(0,600)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Light')                            #Set ylabels
    #plt.plot(tempF, 'r-', label='Degrees F')       #plot the temperature
    plt.plot(time_vec,data1_arr,'r-', label='Light')                               #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(0,40)                           #Set limits of second y axis- adjust to readings you are getting
    #plt2.plot(pressure, 'b-', label='Pressure (Pa)') #plot pressure data
    plt2.plot(time_vec,data2_arr, 'b-', label='Temperature')                           #plot pressure data
    plt2.plot(time_vec,data3_arr, 'k-', label='Temperature2')  
    plt2.set_ylabel('Temperature')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    plt.pause(1e-3)  # allows time to draw
    #drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.show()
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt = cnt+1

    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        time_vec.pop(0)                       #This allows us to just see the last 50 data points
        data1_arr.pop(0)
        data2_arr.pop(0)
        data3_arr.pop(0)
        #data4_arr.pop(0)
