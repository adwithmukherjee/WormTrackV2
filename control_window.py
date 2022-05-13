
## TO DO
# 1. create a window
# 2. input field for filepath, direct to run john's functions
# 3. check boxes for neural net or difference tracker
# 4. check for showing tracker
from psychopy import gui
import os
import glob
from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

from HelpFxns import ImgArray, folderToImgArray, folderToResizeImgArray, vidToImage, showLabeledVid
from tracker import getPosListNew

#title dialog box
myDlg = gui.Dlg(title="WORMS WORMS WORMS")

myDlg.addText('Control Settings')

#input a video file to track
myDlg.addField('Filepath:')

#input sensitivity value
myDlg.addField('Sensitivity:', 21)

#check box for show tracker or nah
myDlg.addField('Show tracker:', initial=False)

#choose to use neural net or difference tracker
myDlg.addField('Tracker type:', choices=["Neural Net", "Difference Tracker"])
ok_data = myDlg.show()  # show dialog and wait for OK or Cancel

if myDlg.OK:  # or if ok_data is not None

    #label data appropriately
    filepath = ok_data[0]
    sensitivity = ok_data[1]
    show_tracker = ok_data[2]
    nn_or_dt = ok_data[3]

    #direct to turn filepath into frames
    directory = vidToImage(filepath)
    imgs = folderToImgArray('frames/')
    print(imgs.size)

    #direct to DT if selected
    if nn_or_dt == 'Difference Tracker':
        positions = getPosListNew(imgs, stepSize = 5)
        print(positions)

        if show_tracker ==True:
            #input rayna code for overlaying video and poslist HERE
            ImgPath = "frames"
            frames = glob.glob(os.path.join(ImgPath, '*.jpg'))
            frames.sort()

            print(f'Analyzing {len(frames)} frames')

            # make window and pixels
            win = visual.Window([1024,800], color='blue', fullscr=0)
            win.clearBuffer()


            #show the images in order
            for f in range(0,len(frames),5):#positionlist)):
                x = 2*((positions[f][0])/512) - 1 #would want this to read the width of the image and divide by it
                y = 2*((positions[f][1])/400) - 1 #would want this to read the height of the image and divide by it
                print(x,y)
                c = visual.Circle(win, radius = 0.01, pos=(x, -y), fillColor='red', lineColor=None) #eventually need to load in positions
                pic = visual.ImageStim(win, image=frames[f], colorSpace='rgb', size=2) #size=2 fills the window
                pic.draw()
                c.draw()
                win.flip() #flips the window to show it
                time.sleep(0.5) #show frames every 0.5 seconds

            input('exit')


        else:
            #input rayna code for videos without tracker
            ImgPath = "frames/"
            frames = glob.glob(os.path.join(ImgPath, '*.jpg'))
            frames.sort()

            print(f'Analyzing {len(frames)} frames')
            # make window and pixels
            win = visual.Window([1024,800], color='blue', fullscr=0)
            win.clearBuffer()

            #show the images in order
            for f in range(0,len(positions)):
                pic = visual.ImageStim(win, image=imgs[f], colorSpace='rgb', size=2) #size=2 fills the window
                pic.draw()
                win.flip() #flips the window to show it
                time.sleep(0.5) #show frames every 0.5 seconds

            input('exit')

    else: 
        #input what happens for neural net here, add later
        positions = getPosListNew(imgs, stepSize = 15, useNeuralNet=True)

        if show_tracker==True:
            ImgPath = "frames"
            frames = glob.glob(os.path.join(ImgPath, '*.jpg'))
            frames.sort()

            print(f'Analyzing {len(frames)} frames')

            # make window and pixels
            win = visual.Window([1024,800], color='blue', fullscr=0)
            win.clearBuffer()


            #show the images in order
            for f in range(0,len(frames)):#positionlist)):
                x = 2*((positions[f][0])/512) - 1 #would want this to read the width of the image and divide by it
                y = 2*((positions[f][1])/400) - 1 #would want this to read the height of the image and divide by it
                c = visual.Circle(win, radius = 0.01, pos=(x, -y), fillColor='red', lineColor=None) #eventually need to load in positions
                pic = visual.ImageStim(win, image=frames[f], colorSpace='rgb', size=2) #size=2 fills the window
                pic.draw()
                win.flip() #flips the window to show it
                time.sleep(0.5) #show frames every 0.5 seconds
                
            input('exit')
        
        else:
            ImgPath = "frames/"
            frames = glob.glob(os.path.join(ImgPath, '*.jpg'))
            frames.sort()

            print(f'Analyzing {len(frames)} frames')
            # make window and pixels
            win = visual.Window([1024,800], color='blue', fullscr=0)
            win.clearBuffer()

            #show the images in order
            for f in range(0,len(positions)):
                pic = visual.ImageStim(win, image=imgs[f], colorSpace='rgb', size=2) #size=2 fills the window
                pic.draw()
                win.flip() #flips the window to show it
                time.sleep(0.5) #show frames every 0.5 seconds

            input('exit') 

        
    
else:
    print('user cancelled') 

