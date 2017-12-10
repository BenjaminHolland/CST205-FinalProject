
import sys
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
from flask_bootstrap import Bootstrap
import track_step
import audio_step
import merge_step
import numpy as np
import cv2

UPLOAD_FOLDER = '/uploads'

app=Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    #do some sort of upload storage before this point, and store in 'video'
    video=None
    tracking_info=None
    audio_info=None
    new_video=None

    if request.method == 'POST':
        video = request.files['file']
        video.save('static/uploaded_video.mp4')
        tracking_info = track_step.run(cv2.VideoCapture('static/uploaded_video.mp4'))
        audio_info=audio_step.run(tracking_info)
        new_video=merge_step.run(audio_info,video)
        return redirect(url_for('home'))
    return render_template('home.html')
