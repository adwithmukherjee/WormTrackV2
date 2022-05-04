from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd

# window and pixels. if you make one that isn't the right size, it will tell you in warnings in the terminal
full_scr = input('full screen? 1 (yes) or 0 (no)')
if full_scr:
	# 1440 x 900 is size of my mac
	win = win = visual.Window([1440,900], color='black', fullscr=0)
else:
	win = visual.Window([600,400], color='black', fullscr=0)

# basic text
ready_text = visual.TextStim(win, text='hello world!')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
core.wait(2) # this literally pauses the script, so its best typically avoided for something more specific
win.flip()
# I like using print(1/0) as a catch all exception that kills my python scripts while I'm testing them
# strictly speaking this is bad coding practice and you should throw an exception
# print(1/0)

# move to the middle and change color
ready_text = visual.TextStim(win, text='hello world!', pos=(450, 0), color='red', units='pix')
ready_text.draw()
win.flip()
core.wait(2)
win.flip()

# same for an image or two
dog1 = visual.ImageStim(win=win, image='dog_cat/im0.jpeg', units="pix", pos=(-300,0))
dog2 = visual.ImageStim(win=win, image='dog_cat/im2.jpeg', units="pix", pos=(300,0))
dog1.draw()
dog2.draw()
win.flip()
core.wait(2)



# lets make a trial
# show an image, get a response, 3 times
# i want to build in saving for error trials
responses = []
rts = []
for t in range(3): # python counts from 0!
	im = 'dog_cat/im' + str(t) + '.jpeg'
	dog = visual.ImageStim(win=win, image=im, units="pix", pos=(0,0))
	dog.draw()
	win.flip()
	# this line will wait for you to press one of the keys in keyList, and if nothing happens by
	# maxWait, it will not return anything and move on. try printing tup after this to see what's inside!
	tup = event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True, timeStamped=core.Clock())
	if tup:
		responses.append(tup[0][0])
		rts.append(tup[0][1])
	else:
		responses.append('NA')
		rts.append(np.nan)
	win.flip()


# we made those response lists, but we didn't do anything to save them
# lets write them to a dataframe and save that as a csv
df = pd.DataFrame({'responses': responses, 'rts': rts})
df.to_csv('data.csv')








# finish
win.close()


















# eof
