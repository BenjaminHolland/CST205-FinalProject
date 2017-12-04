from flask import Flask,render_template,send_from_directory
from flask_bootstrap import Bootstrap
import track_step
import audio_step
import merge_step

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    #do some sort of upload storage before this point, and store in 'video'
    video='static/VideoTest1.mp4'
    tracking_coordinates, tracking_radius_change = track_step.run(video)
    audio_info=audio_step.run(tracking_coordinates)
    new_video=merge_step.run(audio_info,video)
