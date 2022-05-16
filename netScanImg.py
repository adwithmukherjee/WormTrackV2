


from HelpFxns import *
from tracker import getPosListNew
import numpy as np
import pandas as pd
import pickle
from Predict import makeSinglePrediction, predictSingleImg
import tensorflow as tf
from keras.models import Sequential, Model, load_model
import matplotlib.pyplot as plt
import matplotlib.patches as patches


NetPosListFile='NetPosList'

array= folderToImgArray('Classifier2/',1)

model : Model = load_model('TrainedModels/Model1')

print(array.shape)

#John ~18 hours
#This was a bit of a side project that works but does not have a demo script written yet
#It takes overlapping sub-images from a larger image and runs each through the neural net predictor
#The centerpoint of the set of positive worm-identification sub-images is determined to be the worms location

#input an image
#returns x and y position of the worm

def scanImage(image): 

    x_left, y_left, _ = image.shape
    window_size = 128
    stride = 64
    discovered_points_sum = np.zeros((2,))
    num_discovered_points = 0
    for i in range(0, (x_left - window_size)//stride):
        for j in range(0, (y_left - window_size)//stride): 
            sub_img = image[i*stride:i*stride+window_size,j*stride:j*stride+window_size]

            isworm = predictSingleImg(sub_img, model)
            if isworm[0]==1:
                discovered_points_sum = discovered_points_sum + np.array([i*stride + window_size//2, j*stride + window_size//2])
                # discovered_points.concatenate(np.array([i*stride + window_size//2, j*stride + window_size//2]))
                num_discovered_points += 1

                
    avg_worm_point = discovered_points_sum/num_discovered_points

    # x = print(avg_worm_point[0])
    # y = print(avg_worm_point[1])

    y_left = round(avg_worm_point[0])-window_size//2
    x_left = round(avg_worm_point[1])-window_size//2

    worm_img = image[y_left:y_left+window_size,x_left:x_left+window_size]

    fig, ax = plt.subplots()

    ax.imshow(image)
    rect = patches.Rectangle((x_left, y_left), window_size, window_size, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    plt.show()

    return y_left+window_size//2 , x_left+window_size//2

###THIS IS USEFUL
# k = 0 
# for img in array:
#     k+=1
#     if(k%10 == 0):
#         print(k)
#         scanImage(img)
            
def ScanImgBatch(imageArray):
    ar=imageArray
    #ar= folderToImgArray(folderPath)
    k=0
    for img in ar:
        k+=1
        if (k%10 == 0):
            print(k)
            x,y=scanImage(img)
            print(x,y)



 

# scanImage(array[0])
# netPosList= getPosListNew(array) 
# listToFile(netPosList, NetPosListFile) 

# print(netPosList)

# ## 


# netPosList=listFromFile(NetPosListFile)
# #print(posList)

# showLabeledVid(array,netPosList)
