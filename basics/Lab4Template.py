# Lab4Template.py
# Team Number:
# Hardware TM:
# Software TM:
# Date:
# Code purpose: 

# Import Internal Programs
import L2_kinematics as kin
import L2_log as log

# Import External programs
import numpy as np
import time

# DEFINE THE FUNCTIONS FOR THE PROGRAM
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


# UNCOMMENT THE LOOP BELOW TO RUN THE PROGRAM CONTINUOUSLY
while 1:
    task2()
    time.sleep(0.2) # delay a short period
