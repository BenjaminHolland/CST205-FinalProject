# Title: app.py
# Abstract: This program tracks an object in a video, and re-encodes
#           that video with sound based on the object's movement.
# Authors: Jacob Erickson, Ben Holland, Joseph Martineau
# Class: CST205 - Multimedia Programming
# Date: 12/11/2017
# GitHub Link: https://github.com/BenjaminHolland/CST205-FinalProject


from flask import Flask, render_template, send_from_directory, url_for, request, redirect
from flask_bootstrap import Bootstrap
import track_step
import audio_step
import merge_step
import numpy as np
import cv2
import sys
import uuid

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
    
        video_id=uuid.uuid4().hex;
        print(f"procing file {video_id}")
        video_path=f"static/{video_id}.mp4";
        video = request.files['file']
        video.save(video_path)
        
        print(f"getting track info for {video_id}")
        tracking_info = track_step.run(cv2.VideoCapture(video_path))
        print(f"generating audio for {video_id}")
        audio_path=audio_step.run(tracking_info,video_id)
        print(f"mergin {video_id}")
        new_video_file=merge_step.run(video_id)
        return send_from_directory('static',new_video_file)

    return render_template('home.html')

