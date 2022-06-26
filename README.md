# Summer of Innovation 2022 EMOTOR

### This software is shared under MIT License.

## Team Know

This is a web application created for facial emotion recognition and also a python script named face.py is created in which you can detect your emotions using opencv and that can be executed using the command `python face.py`. predict.py file is used to detect the emotions for images present in the EMOTOR_TEST.zip and generate predictions.csv.

### Techstacks Used
1. HTML
2. Css
3. JavaScript
4. Python

### Libraries Used
1. Tensorflow
2. Keras
3. OpenCV
4. DeepFace
5. Flask
6. OpenCV

### Prerequisites

1. Python / Python3 installed.
2. Latest version of `pip` installed.

### Steps To SetUp

1. Open your terminal.
2. Clone this repository in any directory of your choice.

```
https://github.com/kasv-p/SOI-ML.git
```

3. Run the following command to move into the cloned repository.

```
cd SOI-ML
```

4. Later run the following commands to install the required libraries and modules
```
pip install -r requirements.txt
```

5. Once the setup is complete, the web-app can be opened by executing a python script named app.py using the command `python app.py` and application can be seen on port 5000 with the url _loalhost_ **_[Port 5000](http://localhost:500)_**.
**Use Ctrl+C inside the terminal to stop.**

### Important

**_Once the app is setup, you can host the web-app using only step 5._**

### Using the application

1. Once you start the web app the camera opens up by default and detects the emotion you stop the camera by using start/stop button.
2. Navigation bar can be used to go the image uplaod section and detect emotion section.
3. In the image upload section you can determine the emotion of our own image by uploadin the image and can get the result after the page get reloaded.


### Note
- For the live detection of emotion we have used model created by us and for the image upload part we used DeepFace module to get the emotion detected.
- [EMOTOR.ipynb](https://colab.research.google.com/drive/11KhTIPHSFAqxEwO42AwgD8hwVEl-mLpA?usp=sharing) file contains the python script to the models we tried.
- kaggle.json file should be uploaded to download dataset from kaggle.
- fer2013.csv should be uploaded to colab.
- Documentation for ML model is named as `Documentation_EMOTOR.pdf`

_CNN Model couldn't be incorporated as it's size was around 150MB and would not be feasible to store in github. The model can be downloaded fom Google Drive._

- Link to Model: [CNN Model](https://drive.google.com/file/d/1MfVbOqYQuAe-sZ60HBUwri7BpFbqCfOy/view?usp=sharing)
