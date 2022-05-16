#This block of code is so cool and took me ages- J
#Use this block to auto-generate annotated images to use for training
#Give an input path containing a series of sequential worm images
#It will track the worm with motion sensing, guess where it is
#Based on that guess, it will save an image containing the worm, labeled with a W
#Then grab a random image from another portion of the original, that will not contain a worm, labeled N

#WRitten by John  ~15 hours


import cv2
import random
from HelpFxns import *
import io


def labeledSubImg(imgA,imgB,imgDim):
  #returns sub image pulled from input images by frame_compare
  motionPos= frame_compare(imgA, imgB)

  motionImg= pullSub(imgB,motionPos,imgDim)

  randx= random.randrange(0+imgDim[1],imgB.shape[1]-imgDim[1])
  randy= random.randrange(0+imgDim[0],imgB.shape[0]-imgDim[0])
  count=0
  while (randx>(motionPos[0]-round(imgDim[1]/2)) and randx<(motionPos[0]+round(imgDim[1]/2))) and (randy>(motionPos[1]-round(imgDim[0]/2)) and randy<(motionPos[1]+round(imgDim[0]/2))):
    randx= random.randrange(0+imgDim[1],imgB.shape[1]-imgDim[1])
    randy= random.randrange(0+imgDim[0],imgB.shape[0]-imgDim[0])
    count+= 1
    if count >30:
      randx= 0+imgDim[1]
      randy= 0+imgDim[0]
      print('randomization took too long')
      break
  nonMotionImg= pullSub(imgB,[randx,randy],imgDim)
  plt.subplot(1,2,1)
  plt.imshow(motionImg)
  plt.subplot(1,2,2)
  plt.imshow(nonMotionImg)
  print(motionPos)
  print(randx,randy)
  return motionImg, nonMotionImg
  
def labeledSubImgWorm(imgB,imgDim):
  
  motionImg= pullSub(imgB,location,imgDim)

  plt.imshow(motionImg)

  return motionImg

    

def makeClassifierImages(imgPath, outputPath, imgDimensions, stepSize=1, indexStart=0):
  #ImgDimensions in a Rows,Columns notation
  #pos as X,Y notation
  path=imgPath
  imgDimensions= list(imgDimensions)
  #imgList= glob.glob(os.path.join(path, '*.jpg'))
  imgList= getImgList(path)
  listLen= len(imgList)
  imgList.sort()

  for i in range(0,listLen-1,stepSize):
    # imgA= io.imread(imgList[i])
    # imgB= io.imread(imgList[i+1])
  #imgA= io.imread(imgList[1])
  #imgB= io.imread(imgList[2])
    imgA= plt.imread(imgList[i])
    imgB= plt.imread(imgList[i+1])
    subImg,nonMotionImg= labeledSubImg(imgA,imgB,imgDimensions)
    
    cv2.imwrite(outputPath+ '{0}imgLabeled_{1}.jpg'.format("W",(numToIndex(i+indexStart,7))), subImg)
    cv2.imwrite(outputPath+ '{0}imgLabeled_{1}.jpg'.format("N",(numToIndex(i+indexStart,7))), nonMotionImg)

def makeGridClassifiedImgs(imgPath, outputPath, subLocation, subDims, imgDimensions, stepSize=1, indexStart=0):
  #ImgDimensions in a Rows,Columns notation
  #pos as X,Y notation
  path=imgPath
  #imgDimensions= list(imgDimensions)
  #imgList= glob.glob(os.path.join(path, '*.jpg'))
  imgList= getImgList(path)
  listLen= len(imgList)
  imgList.sort()

  for i in range(0,listLen-1,stepSize):
    # imgA= io.imread(imgList[i])
    # imgB= io.imread(imgList[i+1])
  #imgA= io.imread(imgList[1])
  #imgB= io.imread(imgList[2])
    imgA= plt.imread(imgList[i])
    subImg= pullSub(imgA,subLocation,subDims)

    
    cv2.imwrite(outputPath+ '{0}imgLabeled_{1}.jpg'.format("W",(numToIndex(i+indexStart,7))), subImg)
    #cv2.imwrite(outputPath+ '{0}imgLabeled_{1}.jpg'.format("N",(numToIndex(i+indexStart,7))), nonMotionImg)

# #makeClassifierImages("C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/","C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/", [64,64],10
# makeClassifierImages("D:/WormTrack/WormData/12","C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/", [64,64],5,6028)
# a=getImgList("C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/")
# print(a[-1])
# #print(int('006050'))
# #print(a[-1].split('_')[-1][0:7])
# index= int(a[-1].split('_')[-1][0:7])
# makeClassifierImages("D:/WormTrack/WormData/13","C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/", [64,64],5,index+2)

# index= int(a[-1].split('_')[-1][0:7])
# makeClassifierImages("D:/WormTrack/WormData/14","C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/", [64,64],5,index+2)

# index= int(a[-1].split('_')[-1][0:7])
# makeClassifierImages("D:/WormTrack/WormData/15","C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/", [64,64],5,index+2)
# #was 10


subLocation=[140,100]
subDims=[90,90]
a= getImgList("C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput")
print(a[-1])
imgA=plt.imread(a[-1])
#imgB= io.imread("C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/vid1_035.jpg")
#print(a)
#imgA= imgA[subLocation[1]-(subDims[1]/2):subLocation[1]+(subDims[1]/2),subLocation[0]-(subDims[0]/2):subLocation[0]+(subDims[0]/2)]
imgB= pullSub(imgA,subLocation,[90,90])
plt.imshow(imgA)
plt.scatter(subLocation[0],subLocation[1])
plt.show()

index=7477
for x in range(0,4):
  for y in range(0,4):
    makeGridClassifiedImgs("C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierInput/","C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/",[140+x*80,100+y*80],subDims,[64,64],15,index+2)
    a= getImgList("C:/Users/jmara/OneDrive/Documents/GitHub/WormTrackV2/ClassifierOutput/")
    index= int(a[-1].split('_')[-1][0:7])


