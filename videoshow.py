#draw image and also dot, then flip
import psychopy
from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
import HelpFxns
import matplotlib.pyplot as plt
import time


import os, glob

#PLAN: want to draw the dots into the frames and then show the frames in the window
## 1. Get the first frame to show
## 2. Draw a dot into the first frame in the corner
## 3. Draw a dot into the first frame at the coordinate posList gives
## 4. Get all the frames to show
## 5. Draw a dot into all the frames at the coordinate posList gives for each

# frames = HelpFxns.folderToImgArray("/Users/rayna/Documents/GitHub/WormTrackV2/ClassifierOutput")

ImgPath = "/Users/rayna/Documents/GitHub/WormTrackV2/ClassifierOutput"
frames = glob.glob(os.path.join(ImgPath, '*.jpg'))
frames.sort()


# make window and pixels
win = visual.Window([800,800], color='blue', fullscr=0)




#create a dot overlayed on the image
    # c = visual.Circle(win, radius = 0.05, pos=(0,0), fillColor='red', lineColor=None)
    # pic = visual.ImageStim(win, image=frames[f], colorSpace='rgb', size=0.9) #need to fix the size!
    # pic.draw()
    # c.draw()
    # win.flip() #flips the window to show it

#show the images in order
for f in range(0,len(frames),1):
    c = visual.Circle(win, radius = 0.05, pos=(0,0), fillColor='red', lineColor=None) #eventually need to load in posititions
    pic = visual.ImageStim(win, image=frames[f], colorSpace='rgb', size=0.9) #need to fix the size!
    pic.draw()
    c.draw()
    win.flip() #flips the window to show it
    time.sleep(0.08)

    

#plot the poslist
## This block gets the list of x,y positions for each frame
    #def getPosList(imgArray, stepSize='1'):
        #stepSize=5
        #poslist= np.zeros((listlen-1, 2)) #x,y
        #poslist= np.empty((0,2), int)

input('exit')


