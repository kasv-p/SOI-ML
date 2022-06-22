import cv2
from keras.models import load_model
import numpy as np
import tensorflow as tf

model = load_model('CNNv2.h5')
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
class Video(object):
    def __init__(self):
        print('iiiiiiiiiiiiii')
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        print('kkkkkkkkkkkkk')
        self.video.release()
        cv2.destroyAllWindows()
    def get_frame(self):
        ret,frame=self.video.read()
        faces=faceDetect.detectMultiScale(frame, 1.3, 5)
        for x,y,w,h in faces:
            x1,y1=x+w, y+h
            pred_img=frame[y:y+h,x:x+w]
            # cv2.imshow('kk',pred_img)
            # cv2.waitKey(0)
            # pred_img=cv2.cvtColor(pred_img, cv2.COLOR_BGR2GRAY)
            pred_img=cv2.resize(pred_img,(48,48))
            print(pred_img.shape)
            pred_img=np.reshape(pred_img,(1,48,48,3))
            prediction=model.predict(pred_img)
            print(prediction)
            label_map=['Anger','Disgust','Fear','Happy','Neutral','Sad','Surprise']
            prediction=np.argmax(prediction)
            final_prediction=label_map[prediction]
            cv2.putText(img=frame, text=final_prediction, org=(150, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 255, 0),thickness=3)
            print(final_prediction)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 1)
            cv2.line(frame, (x,y), (x+30, y),(255,0,255), 6) #Top Left
            cv2.line(frame, (x,y), (x, y+30),(255,0,255), 6)

            cv2.line(frame, (x1,y), (x1-30, y),(255,0,255), 6) #Top Right
            cv2.line(frame, (x1,y), (x1, y+30),(255,0,255), 6)

            cv2.line(frame, (x,y1), (x+30, y1),(255,0,255), 6) #Bottom Left
            cv2.line(frame, (x,y1), (x, y1-30),(255,0,255), 6)

            cv2.line(frame, (x1,y1), (x1-30, y1),(255,0,255), 6) #Bottom right
            cv2.line(frame, (x1,y1), (x1, y1-30),(255,0,255), 6)
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()
