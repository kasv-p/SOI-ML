from flask import Flask, render_template, Response, request, url_for, redirect, flash,redirect,session
# from werkzeug import secure_filename
from camera import Video
import json
import cv2
from deepface import DeepFace
import os
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    global emotion
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n'+frame+
        b'\r\n\r\n')



@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    global emotion
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            directory=os.getcwd()
            photo.save(os.path.join(directory+'/static', photo.filename))
            path='static/'+photo.filename
            faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            cv_image=cv2.imread(path)
            face=faceDetect.detectMultiScale(cv_image, 1.3, 5)
            try:
                x,y,w,h=face[0]
                cv_image=cv_image[y:y+h,x:x+w]
                analysis=DeepFace.analyze(cv_image,enforce_detection=False)
            except:
                render_template('index.html')
    return render_template('index.html',happ=analysis['emotion']['happy'],fear=analysis['emotion']['fear'],dis=analysis['emotion']['disgust'],
    ang=analysis['emotion']['angry'],sad=analysis['emotion']['sad'],sup=analysis['emotion']['surprise'],neu = analysis['emotion']['neutral'],domin=analysis['dominant_emotion'],emotion=emotion)


@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)
