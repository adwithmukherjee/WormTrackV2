
from email.mime import image
import glob, os 
from skimage import io, transform
import numpy as np 
import matplotlib.pyplot as plt
import cv2
import pylab as plt
from scipy.ndimage.filters import gaussian_filter
import math

import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras import preprocessing
from keras import *


import matplotlib.pyplot as plt
import time
import os 

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from keras.models import Sequential, Model ##Might change this to Convolutional
from keras.layers import Activation, Dropout, Flatten, Dense
#from keras.optimizers import SGD, Adam
from keras.utils.np_utils import to_categorical
from keras.layers.convolutional import Convolution2D, MaxPooling2D, Convolution3D
from keras.layers.convolutional import Conv2D
from sklearn.preprocessing import scale
from sklearn.metrics import confusion_matrix, classification_report
plt.rcParams['axes.grid']=False
import matplotlib as mpl
import cv2
mpl.rcParams['image.cmap'] = 'viridis'
from keras import Model



import matplotlib.pyplot as plt
from keras.models import load_model




# model : Model = load_model('D:/WormTrack/WormData/TrainedModels/Model1')
# model.summary()

print("============================================")

# returns ( is_worm, certainty )
def makeSinglePrediction(imagePath):
    model : Model = load_model('D:/WormTrack/WormData/TrainedModels/Model1')

    img = preprocessing.image.load_img(imagePath, grayscale=False, target_size=(224,224,3))

    img = preprocessing.image.img_to_array(img)

    img = keras.applications.mobilenet.preprocess_input(img)

    img = np.array([img])

    dist = model.predict(img)[0]

    is_wormy = np.argmax(dist)

    certainty = dist[is_wormy]
    
    print('WORM?', is_wormy)
    print('CERTAINTY: ', certainty)

    return is_wormy, certainty


#input batch of categorical distributions
def is_worm(categorical_dist): 

    c = np.array(categorical_dist)
    np.max()




# makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/NimgLabeled_0351.jpg') 
# makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/WimgLabeled_0005991.jpg')

#makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg'); 
# a=plt.imread('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg')
a=plt.imread('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg')
b= preprocessing.image.load_img('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/NimgLabeled_0006233.jpg', grayscale=False, target_size=(64,64,3))
plt.imshow(b)
plt.show()
print(makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/NimgLabeled_0006233.jpg'))