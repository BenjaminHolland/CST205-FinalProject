"""This module provides functionality that turns the original video into tracking information"""

import numpy as np
import cv2

# Define cascade to track object
casc_class = "haarcascade_frontalface_default.xml"
red_cascade = cv2.CascadeClassifier(casc_class)

# Define video file (For testing, will get passed in from app.py)


def run(video):
    pass
