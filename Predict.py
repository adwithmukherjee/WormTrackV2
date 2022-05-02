

import glob, os 
from skimage import io, transform
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from keras import preprocessing
#from keras import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import PIL as pil 
from PIL import Image

from keras.models import Sequential, Model
plt.rcParams['axes.grid']=False
mpl.rcParams['image.cmap'] = 'viridis'
from keras import Model

from keras.models import load_model




# model : Model = load_model('D:/WormTrack/WormData/TrainedModels/Model1')
# model.summary()

print("============================================")

# returns ( is_worm, certainty )
def makeSinglePrediction(imagePath, model):
    #model : Model = load_model('D:/WormTrack/WormData/TrainedModels/Model1')

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
def is_wormAdwith(categorical_dist): 

    c = np.array(categorical_dist)
    np.max()

#def 

model1 : Model = load_model('D:/WormTrack/WormData/TrainedModels/Model1')

# makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/NimgLabeled_0351.jpg') 
# makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/WimgLabeled_0005991.jpg')

#makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg'); 
# a=plt.imread('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg')
a=plt.imread('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg')
b= preprocessing.image.load_img('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/NimgLabeled_0006233.jpg', grayscale=False, target_size=(64,64,3))
plt.imshow(b)
plt.show()
print(makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/NimgLabeled_0006233.jpg', model1))

imgArray1=[]
w=preprocessing.image.load_img('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg', grayscale=False, target_size=(64,64,3))
imgArray1.append(w)
#print(len(imgArray1))

q= preprocessing.image.load_img('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy2.jpg', grayscale=False, target_size=(64,64,3))
imgArray1= imgArray1.append(q)
#print(len(imgArray1))
p=np.asarray(imgArray1)
print(p.shape)
