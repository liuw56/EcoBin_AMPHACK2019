import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
import base64


app = Flask('app', template_folder='/Users/liuwei/Desktop/AMPHACKS_CYCLING/web_app/templates')


@app.route('/api/', methods=['POST'])
def test():
    data = request.form.get("image").replace('data:image/jpeg;base64,','')
    
    imgdata = base64.b64decode(data)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return data


app.run("localhost", "9999", debug=True)
