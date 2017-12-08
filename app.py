
import sys
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
from flask_bootstrap import Bootstrap
import track_step
import audio_step
import merge_step

UPLOAD_FOLDER = '/uploads'

app=Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def home():
    #do some sort of upload storage before this point, and store in 'video'
    video=None
    #tracking_info=track_step.run(video)
    #audio_info=audio_step.run(tracking_info)
    #new_video=merge_step.run(audio_info,video)

    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('home.html')
