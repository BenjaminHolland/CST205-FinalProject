"""This module provides functionality that turns the original video into tracking information"""
""" Help from: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/ """

import numpy as np
import cv2

# Define the lower and upper boundaries of the red
# ball in the HSV color space
redLower = (0, 100, 100)
redUpper = (10, 255, 255)

# Define video file (For testing, will get passed in from app.py)
video = cv2.VideoCapture('static/VideoTest1.mp4')

def run(video):
    while True:
        returned, frame = video.read()

        # Once the video has not returned a frame, the video is over
        if returned == 0:
            break

run(video)
