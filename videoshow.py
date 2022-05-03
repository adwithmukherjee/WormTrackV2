#draw image and also dot, then flip
import psychopy
from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
import HelpFxns

frames = HelpFxns.folderToImgArray("/Users/rayna/Documents/GitHub/WormTrackV2/ClassifierOutput")

# make window and pixels
#full_scr = input('full screen? 1 (yes) or 0 (no)')
#if full_scr == '1':
	# 1440 x 900 is size of my mac
	#win = win = visual.Window([1440,900], color='black', fullscr=0)
#else:
win = visual.Window([600,600], color='black', fullscr=0)

#PLAN: want to draw the dots into the frames and then show the frames in the window
## 1. Get the first frame to show
## 2. Draw a dot into the first frame in the corner
## 3. Draw a dot into the first frame at the coordinate posList gives
## 4. Get all the frames to show
## 5. Draw a dot into all the frames at the coordinate posList gives for each


#show images at framerate for video -- ned to figure out how to show frames that I already have
#visual.ImageStim(win, pos=(0.0, 0.0))


#create a dot overlayed on the image at poslist coordinates - this currently won't show
c = visual.Circle(win, radius = 0.05, pos=(0,0), fillColor='white')
c.draw()
win.flip() #flips the window to show it

#plot the poslist
## This block gets the list of x,y positions for each frame
    #def getPosList(imgArray, stepSize='1'):
        #stepSize=5
        #poslist= np.zeros((listlen-1, 2)) #x,y
        #poslist= np.empty((0,2), int)

input('exit')


