from HelpFxns import *
from Predict import makeSinglePrediction, predictSingleImg
import cv2
from keras.models import Sequential, Model, load_model

def frame_compare(img1,img2,showImg=False):
  #plt.imshow(img1)
  #plt.imshow(img2)
  #sum=img2-img1
  sum= np.zeros(img2.shape)

  rowLen=sum.shape[0]
  colLen=sum.shape[1]

  for pixelx in range(0,colLen):
    for pixely in range(0,rowLen): #here
      for pixelrgb in range(0,3):
        if img2[pixely,pixelx,pixelrgb] >= img1[pixely,pixelx,pixelrgb]:
          sum[pixely,pixelx,pixelrgb]= img2[pixely,pixelx,pixelrgb]-img1[pixely,pixelx,pixelrgb]
        else:
          sum[pixely,pixelx,pixelrgb]= img1[pixely,pixelx,pixelrgb]-img2[pixely,pixelx,pixelrgb]

  ##print(img1[1:5,1:5])
  #print(img2[1:5,1:5])
  #print(sum[1:5,1:5])

  #print(sum.shape[0])


  dif_sens=40 #remove later
  dif_sense= 10 #was 10

  motion_sensitivity=1.1 * 1000

  xavg=0
  yavg=0


  #for xx in range(0, sum.shape[1]):
  # for yy in range(0, sum.shape[0]):
  #   for zz in range(0, sum.shape[2]):
  #     if sum[yy, xx, zz]<= dif_sens:
  #        sum[yy,xx,zz]=0


  #print(sum[0:10, 0:10])

  difArray= np.zeros((sum.shape[0],sum.shape[1]))
  #print(difArray.shape)
  totPixelDif=0
  numNonZpixels=0
  for pixelx in range(0,colLen):
    for pixely in range(0,rowLen):
      for pixelrgb in range(0,3):
        chanPixelDif= sum[pixely,pixelx,pixelrgb]
        totPixelDif = totPixelDif + chanPixelDif
      if totPixelDif > dif_sense*3:
        #print('hi')
        difArray[pixely,pixelx]=totPixelDif
      totPixelDif=0

  #print(difArray)
  difArray[:,:]= difArray[:,:]/3
  #print(difArray)

  #print(difArray)
  weightTot=0
  for pixelx in range(0,colLen):
    for pixely in range(0,rowLen):
      xavg=xavg + (difArray[pixely,pixelx]*pixelx)
      yavg=yavg + (difArray[pixely,pixelx]*pixely)

      weightTot= weightTot + difArray[pixely,pixelx]

  if xavg>motion_sensitivity:
    xavg=round(xavg/weightTot)
    yavg=round(yavg/weightTot)
    pos=[xavg, yavg]
  else: #returns 1,1 if change below threshold
    xavg=1
    yavg=1
    pos=[xavg, yavg]

  size=3

  #imshow
  #print(difArray)
  if showImg==True:
    plt.subplot(2,2,1)
    plt.imshow(sum)
    plt.subplot(2,2,2)
    plt.imshow(difArray)
    plt.subplot(2,2,3)
    difArrayMarked= difArray
    #difArrayMarked[round(yavg-size):round(yavg+size), round(xavg-size):round(xavg+size)]= 1000000
    plt.imshow(difArrayMarked)
    print(xavg,yavg)
    plt.scatter(xavg,yavg)
    plt.subplot(2,2,4)
    plt.imshow(img2)

  #Bring Back
  # plt.subplot(1,1,1)
  # plt.imshow(img2)
  # plt.scatter(xavg,yavg)

  return pos

def getPosListNew(imgArray, stepSize=1, useNeuralNet=False):
  #poslist= np.zeros((listlen-1, 2)) #x,y
  poslist= np.empty((0,2), int)
  prev=[0,0]
  imgRowSize= imgArray.shape(1)
  imgColSize= imgArray.shape(2)
  subDim= int(max(imgRowSize,imgColSize)/8)
  subSize= (subDim,subDim,3)
  if useNeuralNet:
      model : Model = load_model('TrainedModels/Model1')

  for i in range(0,imgArray.shape[0]-1,stepSize):
    img1=imgArray[i,:,:,:]
    img2=imgArray[i+1,:,:,:]

    pos=frame_compare(img1,img2)
    #print(pos)
    if pos==[1,1] and useNeuralNet==False:
        print('no movement at frame(', i+1, ')')
        pos=prev
    elif pos==[1,1] and useNeuralNet:
        print('No movement, checked with Net at frame: ', i+1)
        #pull subImg at previous location and check for worm
        #checkimg= pullSub(img2,prev,[64,64,3])   ### later could pull different size Subs based on image size
        checkimg= pullSub(img2,prev,subSize)
        isworm= predictSingleImg(checkimg, model)
        if isworm[0]==1:
            pos= prev
        else:
            print('lost worm at frame: ', i+1)
    elif abs(pos[0]-prev[0])>subDim or abs(pos[1]-prev[1])>subDim and useNeuralNet:
        print('abnormally fast movement detected at frame(', i+1,') checking with Neural Net')
        check= pullSub(img2,pos,subSize)
        check= cv2.resize(check, dsize=())
        iswormNew= predictSingleImg(check, model)
        checkprev= pullSub(img2,prev,subSize)
        iswormPrev= predictSingleImg(checkprev,model)
        if iswormNew==1 and iswormPrev==1:
            print('worm at both previous and old locations in frame(',i+1),"). Not designed for multi-worm tracking in this version"
        elif iswormPrev==1:
            pos=prev
            print('abnormal movement successfully ignored at frame(',i+1,')')
        elif iswormNew==0 and iswormPrev==0:
            pos=[1,1]
            print("worm found at neither location in frame(",i+1,'). Worm lost')

    if pos!= [1,1]:
        prev=pos

    poslist= np.append(poslist,np.array([pos]),axis=0)
    
  return poslist


a=getPosListNew()