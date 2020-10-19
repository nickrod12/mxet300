# Lab4Template.py
# Team Number:
# Hardware TM:
# Software TM:
# Date:
# Code purpose: 

# Import Internal Programs
import L1_mpu as mpu                                # retrieve magnetometer info
import L2_kinematics as kin
import L2_log as log

# Import External programs
import numpy as np
import time

# DEFINE THE FUNCTIONS FOR THE PROGRAM

# PDL, PDR, X_DOT, THETA_DOT
def task2():
  
  pd = kin.getPdCurrent()  # returns [pdl, pdr] in radians/second
  print ("pd = ", pd)
  pdl = pd[0]
  pdr = pd[1]
  
  frame = kin.getMotion() # returns a matrix containing [xDot, thetaDot]
  print ("frame = ", frame)
  framex = frame[0]
  frametheta = frame[1]
  
  log.tmpFile(pdl,"pdl.txt")
  log.tmpFile(pdr,"pdr.txt")
  log.tmpFile(framex,"framex.txt")
  log.tmpFile(frametheta,"frametheta.txt")
  
# def tmpFile(value, fileName):                               # this function takes a 2-element array called val
#     txt = open("/tmp/" + fileName, 'w+')                    # file with specified name
#     myValue = round(value, 2)
#     txt.write(str(myValue))
#     txt.close()


# HEADING
xRange = np.array([-68.182, 68.800])                         # range must be updated for your device
yRange = np.array([-67.836, 68.891])                        # range must be updated for your device


def getXY():                                        # this function returns an average of several magnetometer readings for x and y
    data = np.take(mpu.getMag(), [0, 1])            # take only the first two elements of the returned array
    for i in range(10):                             # iterate 10 times (i will start at zero)
        newData = np.take(mpu.getMag(), [0, 1])     # call getMag and take the first two elements
        data = np.vstack((data, newData))           # vertically stack the new data array at bottom of existing data
        time.sleep(0.002)                           # delay 5 ms
    data_av = np.average(data, axis=0)              # take an average of the x's and y's to form new array
    data_av = np.round(data_av, 3)                  # round the data
    return(data_av)
    
def scale(axes):                                    # convert raw values to range of [-1 1]

    # re-scale the returned values to a ratio of the value to it's maximum value (0 to 1)
    xScaled = (axes[0] - xRange[0]) / (xRange[1]-xRange[0])
    yScaled = (axes[1] - yRange[0]) / (yRange[1]-yRange[0])

    # re-center the values about zero, and expand the range to +/- 1
    xCentered = (xScaled - 0.5) * 2
    yCentered = (yScaled - 0.5) * 2
    axes = np.array([xCentered, yCentered])
    axes = np.round(axes, 2)
    return(axes)     

def getHeading(myAxes):                             # convert scaled values to a heading
    h = np.arctan2(myAxes[0], myAxes[1])            # atan2 uses all four quadrants to return [-180, 180] range
    return(h)

def convertHeading():
    axes = getXY()                              # call xy function
#    print("raw values:", axes)
    axesScaled = scale(axes)                    # perform scale function
#    print("scaled values:", axesScaled)         # print it out
    h = getHeading(axesScaled)                  # compute the heading
    headingDegrees = round(h*180/np.pi, 2)
    print("heading:", headingDegrees)
    time.sleep(0.25)                            # delay 0.25 sec
    
    log.tmpFile(headingDegrees,"headingDegrees.txt")
    
    return headingDegrees
    
    

# UNCOMMENT THE LOOP BELOW TO RUN THE PROGRAM CONTINUOUSLY
while 1:
    task2()
    convertHeading()
    time.sleep(0.2) # delay a short period
