from PIL import Image
import numpy as np
import sys
import os
import csv
import pandas as pd
import sys
np.set_printoptions(threshold=10000000)

def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

fileList = createFileList('test')
emotions = {'angry':0,'disgust':1,'fear':2,'happy':3,'neutral':6,'sad':4,'surprise':5}
for file in fileList:
    print(file)
    emotion = emotions[file.split('\\')[1]]
    print(emotion)
    img_file = Image.open(file)
    img_grey = img_file.convert('L')
    value = np.asarray(img_grey.getdata(), dtype=np.int64).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    new_row = {'emotion':emotion,'pixels':value}
    with open("img_pixels_test.csv", 'a') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow([emotion,value])
