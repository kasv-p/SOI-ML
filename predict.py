import cv2
import os
from keras.models import load_model
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from os import listdir
import csv
model = load_model('model_csv.h5')

directory='EMOTOR_TEST'

f=open('predictions.csv','w',newline='')
writer=csv.writer(f)
writer.writerow(['img_name','label'])
for pred_img in os.listdir(directory):
    x=pred_img
    pred_img=cv2.imread(os.path.join(directory,pred_img))
    pred_img=cv2.cvtColor(pred_img,cv2.COLOR_BGR2GRAY)
    pred_img=cv2.resize(pred_img,(48,48))
    image_pixels=img_to_array(pred_img)
    image_pixels=np.expand_dims(image_pixels,axis=0)
    image_pixels/=255
    predictions=model.predict(image_pixels)
    max_index=np.argmax(predictions[0])
    label_map=['angry','disgust','fear','happy','sad','surprise','neutral']
    final_prediction=label_map[max_index]
    print(x,final_prediction)
    writer.writerow([x,final_prediction])
