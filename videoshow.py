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

framesforposlist = HelpFxns.folderToImgArray("/Users/rayna/Documents/GitHub/WormTrackV2/ClassifierInput")
#INSTEAD: LOAD IN CSV JOHN IS MAKING

ImgPath = "/Users/rayna/Documents/GitHub/WormTrackV2/ClassifierInput"
frames = glob.glob(os.path.join(ImgPath, '*.jpg'))
frames.sort()

positionlist = HelpFxns.getPosList(framesforposlist)
print(positionlist[0])

# make window and pixels
win = visual.Window([1024,800], color='blue', fullscr=0)
print('hello')




#create a dot overlayed on the image
    # c = visual.Circle(win, radius = 0.05, pos=(0,0), fillColor='red', lineColor=None)
    # pic = visual.ImageStim(win, image=frames[f], colorSpace='rgb', size=0.9) #need to fix the size!
    # pic.draw()
    # c.draw()
    # win.flip() #flips the window to show it

#show the images in order
for f in range(0,len(frames),5):
    c = visual.Circle(win, radius = 0.01, pos=(0,0), fillColor='red', lineColor=None) #eventually need to load in positions
    pic = visual.ImageStim(win, image=frames[f], colorSpace='rgb', size=2) #need to fix the size!
    pic.draw()
    c.draw()
    win.flip() #flips the window to show it
    time.sleep(0.07)

    
#HALEY'S IDEA FOR FINDING COORDINATES OF SCREEN VS POSITION LIST:
#print where it is drawing the dot each time in an approximate location for the first frame

# x = -.5
# y = .5

# for s in range(1000):
#     for ss in range(1000):
#         xstep = s*.001
#         ystep = ss*.001
#         dot = visual.Circle(win,radius=.05,pos=(x+xstep,y+ystep),color='red')
#         dot.draw()
#         win.flip()
#         print(x+xstep, y+ystep)
#         time.sleep(.3)

#print(1/0)


input('exit')


