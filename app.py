# Title: app.py
# Abstract: Base of the whole program which operates through a webpage.
#           The webpage lets the user upload a video of a moving red dot.
#           Then a new video is created of the original dubbed with audio
#           that changes based on the dot's current coordinates in the video.
#           Additionally there is functionality for the user to change the
#           the intensity of the sound as well as view and or download multiple
#           different videos.
# Class: CST205 - Multimedia Programming
# Created by: Jacob A. Erickson
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

#Used for storage of generated videos, this allows the user to save multple videos
videos = []

@app.route('/', methods=['GET', 'POST'])
def home():

    global videos

    video=None
    tracking_info=None
    audio_info=None
    new_video=None

    if request.method == 'POST':

        #Get the user selected base herz for the audio
        herz = int(request.form.get('herz'))

        #give the video a unique name
        #video_id=uuid.uuid4().hex;
        video_id=f'video_{len(videos)}.original'
        print(f"procing file {video_id}")

        #make a path for the video
        video_path=f"static/{video_id}.mp4";

        #take the video submitted by the user
        # and save it into the previously made path
        video = request.files['file']
        video.save(video_path)

        #Obtains information from the video about
        # the position of the ball at each frame
        print(f"getting track info for {video_id}")
        tracking_info = track_step.run(cv2.VideoCapture(video_path))

        #Gets the audio information based off of the tarcking information
        print(f"generating audio for {video_id}")
        audio_path=audio_step.run(tracking_info,video_id,herz)

        #Merges the audio with the original video to create a new video
        print(f"mergin {video_id}")
        new_video_file=merge_step.run(video_id)

        #Adds the video name to a list for future referencing
        videos.append(new_video_file)

        #Changes the page to one where the newly created video can be viewed
        return redirect(url_for('brand'))

    #its necessary to pass the list of videos so that
    # they can be listed out on the webpage
    return render_template('home.html', videos=videos)

@app.route('/created', methods=['GET', 'POST'])
def brand():
    global videos

    if request.method == 'POST':
        return redirect(url_for('home'))

    return render_template('video.html', video=videos[len(videos) - 1])

@app.route('/videos/<video_number>', methods=['GET', 'POST'])
def film(video_number):
    global videos

    if request.method == 'POST':
        return redirect(url_for('home'))

    #its necessary to pass the list of videos so that
    # they can be listed out
    return render_template('video.html', video=str(video_number) + ".mp4", videos=videos)
