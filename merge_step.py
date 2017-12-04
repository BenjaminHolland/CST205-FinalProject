# Title: merge_step.py
# Abstract: This module takes in tracking information generated
#           by the track_step module, and generates audio data
#           based on that information.
# Author: Ben Holland
# Class: CST205 - Multimedia Programming
# Date: 12/11/2017

import subprocess
"""This step takes the generated audio data and the original video, and merges them together, outputting the final video"""

def run(audio,video):
    local_audio=_convert_audio(audio)
    local_video=_convert_video(video)

    return 'test.mp4'
def _test():
    audio_file='static/TestAudio1.wav'
    video_file='static/VideoTest1.mp4'
    inputs=f"-i {video_file} -i {audio_file}"
    mapping="-map 0:0 -map 1:0"
    codecs="-c:v copy -c:a aac"
    bitrate="-b:a 256k"
    subprocess.call(f"./bin/ffmpeg/bin/ffmpeg {inputs} {mapping} {codecs} {bitrate} -loglevel verbose output.mp4")


def _convert_audio(audio):
    return None
def _convert_video(video):
    return None

if(__name__=='__main__'):
    _test()
