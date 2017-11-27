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

        # Convert the frame to the HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # construct a mask for the red ball, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, redLower, redUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

run(video)
