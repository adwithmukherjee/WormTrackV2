from HelpFxns import folderToImgArray, getPosList, pullSub, showImgArray, showLabeledVid
from Predict import predictSingleImg
import matplotlib.pyplot as plt

a= 'Classifier2/'
b= folderToImgArray(a,1)

c= getPosList(b)

d=pullSub()

showImgArray(d)

