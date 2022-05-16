from HelpFxns import * 
import tensorflow

### A lot of this is adapted from the Bee-Neural Net class demo to simplify network architecture for us
#John worked on using this to create our own model on self-created labeled data
# ~5 hours


#dataPath = '/content/drive/My Drive/WormTracker/LabeledImgs/'
dataPath = 'D:/WormTrack/WormData/Labeled/'
#imgsList= glob.glob(os.path.join(dataPath, '*.jpg')) #pulls list of all files in folder
imgsList= getImgList(dataPath)
listlen= len(imgsList)
imgsList.sort() #this sorts them alphabetically ASSUMES IMAGES ARE NUMBERED ALREADY/PROPERLY
print(imgsList)
trainData,labels= dataset(imgsList, (64,64)) #trainData is now an array of images, labels is an array of label values 0/1
print(labels)
print(trainData.shape)
# Create a training and testing dataset with 25% of the samples
X_train, X_test, y_train, y_test = train_test_split(trainData,labels, test_size=.25,random_state=0,)
#ids=np.array(range(data.shape[0]))
#X_train, X_ids, y_train, y_ids = train_test_split(data,ids, test_size=.25,random_state=0,)
#X_test=labels[X_ids]; y_test=labels[y_ids]
print('Done')


# check shape of the input image to fit with the network 
print(X_train.shape)
print(X_test.shape)

####

import skimage
#These were original values, I reduced to 64x64 because we already took down to that size
X_train_resized = np.asarray([skimage.transform.resize(image, (224,224)) for image in X_train])
X_test_resized = np.asarray([skimage.transform.resize(image, (224,224)) for image in X_test])

#X_train_resized = np.asarray([skimage.transform.resize(image, (64,64)) for image in X_train])
#X_test_resized = np.asarray([skimage.transform.resize(image, (64,64)) for image in X_test])

print(X_train_resized.shape)
print(X_test_resized.shape)
# plt.subplot(1,2,1)
# plt.imshow(X_train[2,:,:,:])
# plt.subplot(1,2,2)
# plt.imshow(X_train_resized[2,:,:,:])



y_train_encoded = to_categorical(y_train)
y_test_encoded = to_categorical(y_test)

y_train_encoded.shape


#


import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Dense, Activation,Dropout,Conv2D, MaxPooling2D,BatchNormalization, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras import regularizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model, load_model, Sequential
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import time
import os


train_gen=ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input,
                horizontal_flip=True,
                samplewise_center=True,
                width_shift_range=.2,
                height_shift_range=.2,                
                samplewise_std_normalization=True).flow(X_train_resized, y_train_encoded)
#val_gen=ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input,
#                samplewise_center=True,                
#                samplewise_std_normalization=True).flow(xValid, yValid, shuffle=False)        
test_gen=ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input,
                samplewise_center=True,                
                samplewise_std_normalization=True).flow(X_test_resized, y_test_encoded, shuffle=False)



#


Top=False
weights=None
layer_cut=-6
lr_rate=.001
rand_seed=128
epochs=25
mobile = tf.keras.applications.mobilenet.MobileNet( include_top=Top,
                                                           input_shape=(224,224,3),
                                                           pooling='avg', weights='imagenet',
                                                          )  #was 224,224,3
                 
x=mobile.layers[layer_cut].output
x = Flatten()(x)
x=Dense(128, kernel_regularizer = regularizers.l2(l = 0.015), activation='relu')(x)

x=Dropout(rate=.5, seed=rand_seed)(x)
predictions=Dense (2, activation='softmax')(x)
model = Model(inputs=mobile.input, outputs=predictions)
        
for layer in model.layers:
    layer.trainable=True
model.compile(Adam(lr=lr_rate), loss='categorical_crossentropy', metrics=['accuracy'])


#

print(mobile.layers)
x=mobile.layers[layer_cut].output
print(mobile.layers[-6].output)
x = Flatten()(x)
print(x)
x=Dense(128, kernel_regularizer = regularizers.l2(l = 0.015), activation='relu')(x)
print(x)

x,y  = train_gen.next()



# set ansi color values
Cblu ='\33[34m'
Cend='\33[0m'   # sets color back to default 
Cred='\033[91m'
Cblk='\33[39m'
Cgreen='\33[32m'
Cyellow='\33[33m'




start_epoch=0
start=time.time()
results = model.fit_generator(generator = train_gen, validation_data= test_gen, epochs=epochs, initial_epoch=start_epoch, verbose=1)
stop=time.time()
duration = stop-start
hrs=int(duration/3600)
mins=int((duration-hrs*3600)/60)
secs= duration-hrs*3600-mins*60
msg='{0}Training took\n {1} hours {2} minutes and {3:6.2f} seconds {4}'
print(msg.format(Cblu,hrs, mins,secs,Cend))
tacc=results.history['accuracy']
tloss=results.history['loss']
vacc=results.history['val_accuracy']
vloss=results.history['val_loss']

Epoch_count=len(tloss)
Epochs=[]
for i in range (0,Epoch_count):
    Epochs.append(i+1)
index_loss=np.argmin(vloss)#  this is the epoch with the lowest validation loss
val_lowest=vloss[index_loss]
index_acc=np.argmax(vacc)
val_highest=vacc[index_acc]
plt.style.use('fivethirtyeight')
sc_label='best epoch= '+ str(index_loss+1)
vc_label='best epoch= '+ str(index_acc + 1)
fig,axes=plt.subplots(nrows=1, ncols=2, figsize=(15,5))
axes[0].plot(Epochs,tloss, 'r', label='Training loss')
axes[0].plot(Epochs,vloss,'g',label='Validation loss' )
axes[0].scatter(index_loss+1,val_lowest, s=150, c= 'blue', label=sc_label)
axes[0].set_title('Training and Validation Loss')
axes[0].set_xlabel('Epochs')
axes[0].set_ylabel('Loss')
axes[0].legend()
axes[1].plot (Epochs,tacc,'r',label= 'Training Accuracy')
axes[1].plot (Epochs,vacc,'g',label= 'Validation Accuracy')
axes[1].scatter(index_acc+1,val_highest, s=150, c= 'blue', label=vc_label)
axes[1].set_title('Training and Validation Accuracy')
axes[1].set_xlabel('Epochs')
axes[1].set_ylabel('Accuracy')
axes[1].legend()
plt.tight_layout
#plt.style.use('fivethirtyeight')
plt.show()
