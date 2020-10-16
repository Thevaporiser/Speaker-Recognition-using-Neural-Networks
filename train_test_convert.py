'''
import os
os.chdir("/Users/priyanshringe/Documents/College_Stuff/Codes-and-stuff/minorProject")
'''

import numpy as np
import pandas as pd
from wavToSpectrogram_2 import wave2Spec as w2s

path = 'Path/to/folder/--/data/'
saveImg = '/Path/to/folder/--/data/TEST' #change TRAIN to TEST
#in below line, change train_data to test_data and select the path column name for windows and change nrows value ( for TRAIN = 23100, for TEST = 8400)
Data = pd.read_csv("/Path/to/csv/file/--/test_data.csv", dtype = {"dialect_region": str, "speaker_id": str, "path_from_data_dir": str,"filename": str, "is_audio": bool}, nrows=8400, usecols =['dialect_region','speaker_id','filename','path_from_data_dir','is_audio'])
audioBool = np.array(Data["is_audio"])
#change to windows file path column as stated in the csv file in the below line 
audio_path = np.array(Data["path_from_data_dir"])
filename = np.array(Data["filename"])

audio_fPath = list()
appPath = list()
images = list()
imgFile = list()
im = list()
imgSave = list()

for index in range(len(audioBool)-1):
    if audioBool[index] == True:
        audio_fPath.append(audio_path[index])
        imgFile.append(filename[index])
    else:
        pass

for jndex in range(len(audio_fPath)):
     appPath.append(path + audio_fPath[jndex])

appPath = np.array(appPath)
imgfileArray = np.array(imgFile)

for i in range(len(imgfileArray)):
    im.append(audio_path[i][6:-4] + '.png') #change to [5:-4] for TEST and [6:-4] for TRAIN 

imArray = np.array(im)

for j in range(len(imArray)):
    imgSave.append(saveImg + '/' + imArray[j])

imgSave  = np.array(imgSave)
print(len(appPath))

for lndex in range(len(appPath)):
    w2s.convert(appPath[lndex], imgSave[lndex])
    print(lndex + " files converted out of " + len(appPath))
