from flask import Flask,render_template,send_from_directory
from flask_bootstrap import Bootstrap
import track_step
import audio_step
import merge_step

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return None
