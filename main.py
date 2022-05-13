

import pandas as pd
from HelpFxns import folderToImgArray, getPosList, listToFile, listFromFile, showLabeledVid, vidToImage
import pickle
from tracker import getPosListNew
from netScanImg import ScanImgBatch, scanImage


def trackerMain(imgLocation, methodNum, RefreshRate):
    #Choose filepath to video or file of images e.g.('ClassifierInput/')
    #vidToImage('/PractiveVid/')

    #imgLocation= 'Classifier2/'

    ###Choose an input for which tracking method
    #methodNum=3#2
    #RefreshRate=1 #make this a user input

    #Establish Array of Images to be tested

    imgArray= folderToImgArray(imgLocation, step=RefreshRate) #can be made 10 to go faster
    #noNetOutput= getPosListNew(imgArray,useNeuralNet=False)


    ### Get Position List 

    filename='PositionListMem'


    if methodNum==1:
        #Option 1: 
        PosList= getPosList(imgArray)
        listToFile(PosList,filename)
    elif methodNum==2:
        PosList= getPosListNew(imgArray, useNeuralNet=False)
        listToFile(PosList,filename)
    elif methodNum==3:
        PosList= getPosListNew(imgArray, useNeuralNet=True)
        listToFile(PosList,filename)
    elif methodNum==0:
        ScanImgBatch(imgArray)

    savedPosList= listFromFile(filename)
    print(savedPosList)
    print(len(savedPosList))
    showLabeledVid(imgArray,savedPosList,fps=30)


#trackerMain('Classifier2/', 3, 1)