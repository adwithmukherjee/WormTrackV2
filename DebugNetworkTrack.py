from HelpFxns import *
from tracker import getPosListNew
import numpy as np
import pandas as pd
import pickle

##load image array
# Posfile='PositionListMem'
NetPosListFile='NetPosList'
# imgArray= folderToImgArray('Classifier2/',step=5)
# np.save('imageArr.npy',imgArray)

# array=np.load('imageArr.npy')
array= folderToImgArray('Classifier2/',5)
print(array.shape)


##run position tracker

# PosList= getPosList(array) ####### THIS ONE WORKS
# listToFile(PosList, Posfile) 
# # print(PosList)

## run position tracker Neural Network

netPosList= getPosListNew(array) 
listToFile(netPosList, NetPosListFile) 

print(netPosList)

## 


netPosList=listFromFile(NetPosListFile)
#print(posList)

showLabeledVid(array,netPosList)
