
from HelpFxns import *
import glob, os 
from skimage import io, transform
import numpy as np 
import tensorflow as tf
from tensorflow import keras
from keras import preprocessing
from keras.applications.mobilenet import preprocess_input
#from keras import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import PIL as pil 
from PIL import Image
import cv2

from keras.models import Sequential, Model
plt.rcParams['axes.grid']=False
mpl.rcParams['image.cmap'] = 'viridis'
from keras import Model

from keras.models import load_model

#John ~8 hours
#This is a set of functions that make neural net predictions on images passed to them
#They can either label WORM or NO WORM


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
    
    # print('WORM?', is_wormy)
    # print('CERTAINTY: ', certainty)

    return is_wormy, certainty

def predictSingleImg(imgAny, model): ###THIS FUNCTION WORKS
    
    imgAny= cv2.resize(imgAny,dsize=(224,224))
    # print(imgAny.shape)
    imgAny= keras.applications.mobilenet.preprocess_input(imgAny)

    imgAny= np.array([imgAny])
    dist = model.predict(imgAny)[0]

    is_wormy = np.argmax(dist)

    certainty = dist[is_wormy]
    
    # print('WORM?', is_wormy)
    # print('CERTAINTY: ', certainty)   

    return is_wormy, certainty


#input batch of categorical distributions
def is_wormAdwith(categorical_dist): 

    c = np.array(categorical_dist)
    np.max()

def batchPrediction(folderPath, model):
    imgs=ImgArrayResize(folderPath, (224,224,3))
    listlen= imgs.shape[0]

    pred_key= np.zeros((listlen))
    conf_key= np.zeros((listlen))
    for x in range(0,listlen):
        prepped_img= keras.applications.mobilenet.preprocess_input(imgs[x])
        prepped_img= np.array([prepped_img])
        dist= model.predict(prepped_img)[0]
        #print(dist)
        is_wormy = np.argmax(dist)
        certainty= dist[is_wormy]
        pred_key[x]=is_wormy
        conf_key[x]= certainty
    return pred_key, conf_key




#model1 : Model = load_model('D:/WormTrack/WormData/TrainedModels/Model1')
model1 : Model = load_model('TrainedModels/Model1')

# makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/NimgLabeled_0351.jpg') 
# makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/WimgLabeled_0005991.jpg')

#makeSinglePrediction('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg'); 
# a=plt.imread('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg')


# a=plt.imread('ClassifierInput/wormy.jpg')
# b= preprocessing.image.load_img('ClassifierInput/wormy.jpg', target_size=(64,64,3))
# plt.imshow(b)
# plt.show()
# print(makeSinglePrediction('ClassifierInput/wormy.jpg', model1))


# imgArray1=[]
# w=preprocessing.image.load_img('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy.jpg', grayscale=False, target_size=(64,64,3))
# imgArray1.append(w)
# #print(len(imgArray1))

# q= preprocessing.image.load_img('C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/wormy2.jpg', grayscale=False, target_size=(64,64,3))
# imgArray1= imgArray1.append(q)
# #print(len(imgArray1))
# p=np.asarray(imgArray1)
# print(p.shape)

# array1= folderToResizeImgArray('ClassifierInput/',(64,64,3))
# print(array1.shape)
# plt.imshow(array1[2])
# plt.show()

#a=plt.imread('ClassifierInput/wormy.jpg')
# iArray= np.array
# a= np.asarray(preprocessing.image.load_img('ClassifierInput/chicken.jpg', target_size=(64,64,3)))
# b= np.asarray(preprocessing.image.load_img('ClassifierInput/wormy.jpg', target_size=(64,64,3)))
# c= np.array((a,b))
# a= np.asarray(a)
# print(a.shape)
# print(b.shape)
# print(c.shape)
# plt.imshow(c[1,:,:,:])
# plt.show()


# out= ImgArrayResize('ClassifierInput/',(64,64,3))
# print(out.shape)

#out= batchPrediction('ClassifierInput/',model1)


# a=plt.imread('Classifier2/vid7_001.jpg')
# a=pullSub(a,[340,225],(64,64))
# print(a.shape)
# plt.imshow(a)
# plt.show()
# predictSingleImg(a,model1)

