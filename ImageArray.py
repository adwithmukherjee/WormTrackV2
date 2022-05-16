import matplotlib.pyplot as plt
import PIL
import numpy as np

#John 

def ImgArray(file_list):
	outputArray=[]
	for i, file in enumerate(file_list):
		image = plt.imread(file)
		outputArray.append(image)
	return np.array(outputArray)

a= ImgArray('/ClassifierInput/')
print(a.shape)