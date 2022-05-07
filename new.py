from HelpFxns import *
from tracker import getPosListNew
import numpy as np
import pandas as pd
import pickle

##load image array
Posfile='PositionListMem'
#imgArray= folderToImgArray('Classifier2/',step=5)
#np.save('imageArr.npy',imgArray)

array=np.load('imageArr.npy')
print(array.shape)


##run position tracker

# PosList= getPosList(array) ####### THIS ONE WORKS
# listToFile(PosList, Posfile) 
# # print(PosList)

## run position tracker Neural Network

PosList= getPosListNew(array) 
listToFile(PosList, Posfile) 












## 


posList=listFromFile(Posfile)
print(posList)

showLabeledVid(array,posList)
