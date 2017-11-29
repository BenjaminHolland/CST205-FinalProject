from flask import Flask,render_template,send_from_directory
from flask_bootstrap import Bootstrap
import track_step
import audio_step
import merge_step

app=Flask(__name__)
Bootstrap(app)

@app.route('/' methods=['GET', 'POST'])
def home():
    #do some sort of upload storage before this point, and store in 'video'
    video=None
    tracking_info=track_step.run(video)
    audio_info=audio_step.run(tracking_info)
    new_video=merge_step.run(audio_info,video)




    return None
