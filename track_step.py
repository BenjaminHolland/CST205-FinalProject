# Title: track_step.py
# Abstract: This module provides functionality that turns the
#           original video into tracking information.
# Author: Joseph Martineau
# Class: CST205 - Multimedia Programming
# Date: 12/11/2017
# Help from: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

import numpy as np
import cv2

# Define the lower and upper boundaries of the red
# ball in the HSV color space
redLower = (0, 100, 100)
redUpper = (10, 255, 255)


def run(video):

    # Array to return (x, y) coordinates
    coordinates = []

    # Array to return how the radius changes per frame
    radius_change = []

    radius = -1
    previous_radius = -1

    # get framerate.
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    fps=30
    length=0;
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))/float(fps)
    width=video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    while True:
        returned, frame = video.read()


        # Once the video has not returned a frame, the video is over
        if returned == 0:
            break

        # Convert the frame to the HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Construct a mask for the red ball, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, redLower, redUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # Find contours in the mask and initialize the current
        # (x, y) center of the ball
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # Only proceed if at least one contour was found
        if len(contours) > 0:
            # find the largest contour in the mask, then use
            # it to get (x, y) coordinates of the ball's center
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Add ball's center position to coordinate array
        coordinates.append(center)

        # Get the change in radius
        if previous_radius == -1:
            previous_radius = radius;
        change_in_size = (radius - previous_radius)

        # Append change in radius to radius_change array
        radius_change.append(int(change_in_size))

    return ((fps,length,width,height),zip(coordinates,radius_change)) #, radius_change
