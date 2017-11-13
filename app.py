from flask import Flask,render_template,send_from_directory
from flask_bootstrap import Bootstrap
app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return None
