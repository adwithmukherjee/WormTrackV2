import matplotlib.pyplot as plt
from HelpFxns import *

stepSize=10

imgs= folderToImgArray('ClassifierInput/', step=stepSize)
posList= getPosList(imgs)
print(imgs.shape)
print(posList.shape)

fg= plt.figure()
ax = fg.gca()

h = ax.imshow(imgs[0])

i=0
#for img in imgs:
for ii in range(1, posList.shape[0]):
    h.set_data(imgs[ii])
    plt.draw()
    a = plt.scatter(posList[ii,0],posList[ii,1],s=3)
    plt.pause(2)
    a.remove()
    i+=1