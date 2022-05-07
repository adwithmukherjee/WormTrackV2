

import pandas as pd
from HelpFxns import folderToImgArray, getPosList

##rn even importing this throws an error
#from tracker import getPosListNew


imgArray= folderToImgArray('Classifier2/', step=1)
#noNetOutput= getPosListNew(imgArray,useNeuralNet=False)
noNetOutput= getPosList(imgArray)

print(noNetOutput)
df= pd.DataFrame(columns=['filename','xpos', 'ypos'])
df.append({"filename":filenames[0]})
df.to_csv('filename')

