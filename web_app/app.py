import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
import base64
from flask import Flask, render_template, request, redirect
import threading

app = Flask('app', template_folder='templates')
trained_m = False

def get_prediction(trained_m):
    return None

@app.route('/tryit')
def try_it():
    return render_template('test.html')

@app.route('/api/', methods=['POST'])
def model_predict():
    data = request.form.get("image").replace('data:image/jpeg;base64,','')
    
    imgdata = base64.b64decode(data)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    # while not flag:


    return render_template('resultsForm.html', type_trash="trash")

# home button
@app.route('/')
def home():
    return render_template('index.html')

# the x mark-cancelling 
@app.route('/cancel')
def cancel():
    return render_template('camera.html')

# checkmark
@app.route('/predict')
def predict():
    return render_template('info.html', type_trash=trained_m)


@app.route('/test')
def test():
    return render_template('test.html', type_trash=predict)



if __name__ == "__main__": 
    app.run("localhost", "9999", debug=True)
