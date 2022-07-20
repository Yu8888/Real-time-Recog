#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : linjie
from flask import Flask, render_template, Response,  request, session, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from detect import *
import os
import torch
from importlib import import_module
from datetime import datetime
# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera
# from flack_cors import *

app = Flask(__name__)
# UPLOAD_FOLDER = "C:\Users\Arpit Sharma\Desktop\Friendship goals\content\yolov5\static\uploads"
DETECTION_FOLDER = r'./static/detections'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
#app.config['DETECTION_FOLDER'] = DETECTION_FOLDER




@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
    # the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    # return render_template('index.html')
    # return """
    # <h1>Hello heroku</h1>
    # <p>It is currently {time}.</p>
    # <img src="http://loremflickr.com/600/400" />
    # <h1>linjie</h1>
    # <img src="{{ url_for('video_feed') }}">
    # """.format(time=the_time)

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/videovideo_feedapt-get update && apt-get install libgl1')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





if __name__ == "__main__":
    app.run(debug = True)
