# Title: merge_step.py
# Abstract: This module takes in tracking information generated
#           by the track_step module, and generates audio data
#           based on that information.
# Author: Ben Holland
# Class: CST205 - Multimedia Programming
# Date: 12/11/2017

import subprocess

def run(video_id):
    audio_file=f'static/{video_id}.wav'
    video_file=f'static/{video_id}.mp4'

    output_file=f'static/{video_id[0:-9]}.mp4'
    inputs=f"-i {video_file} -i {audio_file}"
    mapping="-map 0:0 -map 1:0"
    codecs="-c:v copy -c:a aac"
    bitrate="-b:a 256k"
    # -loglevel verbose
    subprocess.call(f"./bin/ffmpeg/bin/ffmpeg {inputs} {mapping} {codecs} {bitrate} {output_file}")
    return f'{video_id[0:-9]}.mp4'

if(__name__=='__main__'):
    _test()
