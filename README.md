# Summer of Innovation 2022 EMOTOR

### This software is shared under MIT License.

## Team Know

This is a web application created for facial emotion recognition.

### Techstacks Used
1. HTML
2. Css
3. JavaScript
4. Flask (python)

### Libraries Used
1. Tensorflow
2. Keras
3. OpenCV
4. DeepFace

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
4. Create virtual environment and activates the virtual environment on executing the following commands.

```
sudo apt-get install python3-tk
```
```
sudo apt-get install python-tk
```

5. Later run the following commands to install the required libraries and modules
```
pip install -r requirements.txt
```

6. Once the setup is complete, the web-app can be opened using _loalhost_ **_[Port 5000](http://localhost:500)_**.
**Use Ctrl+C inside the terminal to stop.**

### Important

**_Once the app is setup, you can host the web-app using only step 6._**

### Using the application

1. Once you start the web app the camera opens up by default and detects the emotion you stop the camera by using start/stop button.
2. Navigation bar can be used to go the image uplaod section.
3. In the image upload section you can determine the emotion of our own image by uploadin the image and can get the result after the page get reloaded.


### Note
- For the live detection of emotion we have used model created by us and for the image upload part we used DeepFace module to get the emotion detected.
- The notebook and data used for training can be found under the following directories:

  1. `ML/SDS_MODEL.ipynb`
  2. `ML/data_full.csv`
     <br>
     <br>

- Documentation for ML model is named as `Documentation_Kepler.pdf`
- Documentation for the Web-App can be found under the `Docs` tab of the Web-App itself.
- The predictions are present in the `predicted` coloumn in downloaded files.

_The Random Forest Model couldn't be incorporated as it's size was around 3.5 GB and would not be feasible for a stand-alone application. The model can be run on Google Colab._

- Link to Model: [Random Forest](https://drive.google.com/file/d/1MTWGQinxfvbYmVzOYc4AGZO26kWE11xA/view?usp=sharing)
