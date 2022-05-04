import matplotlib.pyplot as plt
from HelpFxns import folderToImgArray, getPosList

stepSize=10

imgs= folderToImgArray('ClassifierInput/', step=stepSize)
posList= getPosList(imgs)
print(imgs.shape)
print(posList.shape)



def showLabeledVid(imgArray,posList,fps=30,overlay=True):
    fg= plt.figure()
    ax = fg.gca()
    h = ax.imshow(imgArray[0])

    i=0
    if overlay:
        #for img in imgs:
        for ii in range(1, posList.shape[0]):
            h.set_data(imgArray[ii])
            plt.draw()
            a = plt.scatter(posList[ii-1,0],posList[ii-1,1],s=3)
            plt.pause(fps/60)
            a.remove()
            i+=1
    else:
        for ii in range(1, posList.shape[0]):
            h.set_data(imgArray[ii])
            plt.draw()
            plt.pause(1/fps)
            i+=1

showLabeledVid(imgs,posList,fps=30)