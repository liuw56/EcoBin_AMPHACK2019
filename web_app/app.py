import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
import base64
from flask import Flask, render_template, request, redirect
import threading
from pathlib import Path
from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
from glob2 import glob
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np
import os
import zipfile as zf
import shutil
import re
import seaborn as sns
tfms = get_transforms(do_flip=True, flip_vert=True)
path = Path(os.getcwd())/"data"
data = ImageDataBunch.from_folder(path,test="test", ds_tfms=tfms,bs=4,num_workers=0)
learn=cnn_learner(data,models.resnet34, metrics=error_rate)

learn = learn.load("trained_model")
app = Flask('app', template_folder='templates')

def get_prediction(learn):
    return None

@app.route('/tryit')
def try_it():
    return render_template('test.html')

app.route('/menu')
def menu():
    return render_template('manual.html')

@app.route('/api', methods=['POST'])
def model_predict():
    data = request.form.get("image").replace('data:image/jpeg;base64,','')
    
    imgdata = base64.b64decode(data)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    global trash
    trash = learn.predict(open_image('some_image.jpg'))[0]
    # while not flag:
    # trash = learn.predict(open_image('some_image.jpg'))[0]

    # print(trash)
    return render_template('info.html', type_trash=trash)


# home button
@app.route('/')
def index():
    return render_template('index.html')

# the x mark-cancelling 
@app.route('/cancel')
def cancel():
    return render_template('camera.html')

# checkmark
@app.route('/predict')
def predict():
    # print(trash)
    return render_template('info2.html', type_trash=trash)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')
# @app.route('/test')
# def test():
#     return render_template('test.html', type_trash=predict)



if __name__ == "__main__": 
    # print(trash)
    app.run("localhost", "9999", debug=True)

