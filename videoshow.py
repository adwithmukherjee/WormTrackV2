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
import random


import os, glob

#PLAN: want to draw the dots into the frames and then show the frames in the window
## 1. Get the first frame to show
## 2. Draw a dot into the first frame in the corner
## 3. Draw a dot into the first frame at the coordinate posList gives
## 4. Get all the frames to show
## 5. Draw a dot into all the frames at the coordinate posList gives for each
print('Loading Images')

nthframe = 40

framesforposlist = HelpFxns.folderToImgArray("ClassifierInput")
framesforposlist = framesforposlist[0::nthframe] #TEMPORARY UNTIL GETPOSLIST IS FASTER
#INSTEAD: LOAD IN CSV JOHN IS MAKING?

ImgPath = "ClassifierInput"
frames = glob.glob(os.path.join(ImgPath, 'vid4*.jpg'))
frames.sort()
frames = frames[0::nthframe] #TEMPORARY UNTIL GETPOSLIST IS FASTER

print(f'Analyzing {len(frames)} frames')

#positionlist = HelpFxns.getPosList(framesforposlist)

# make window and pixels
win = visual.Window([1024,800], color='blue', fullscr=0)
win.clearBuffer()


#show the images in order
for f in range(0,len(frames)):#positionlist)):
    #x = 2*((positionlist[f][0])/512) - 1 #would want this to read the width of the image and divide by it
    #y = 2*((positionlist[f][1])/400) - 1 #would want this to read the height of the image and divide by it
    #c = visual.Circle(win, radius = 0.01, pos=(x, -y), fillColor='red', lineColor=None) #eventually need to load in positions
    pic = visual.ImageStim(win, image=frames[f], colorSpace='rgb', size=2) #size=2 fills the window
    pic.draw()
    #c.draw()
    win.flip() #flips the window to show it
    time.sleep(0.5) #show frames every 0.5 seconds

    


input('exit')


