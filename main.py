

import pandas as pd
from HelpFxns import folderToImgArray, getPosList, listToFile, listFromFile
from 
import pickle



#rn even importing this throws an error
from tracker import getPosListNew


#imgArray= folderToImgArray('ClassifierInput/', step=10)
#noNetOutput= getPosListNew(imgArray,useNeuralNet=False)




noNetOutput= [[25,23],[10,10]] #just test values
filename='PositionListMem'
# noNetOutput= getPosList(imgArray)
listToFile(noNetOutput,filename)

savedPosList= listFromFile(filename)

print(savedPosList)
print(len(savedPosList))

# print(noNetOutput)
# df= pd.DataFrame(columns=['filename','xpos', 'ypos'])
# df.append({"filename":filenames[0]})
# df.to_csv('filename')

