# Title: audio_step.py
# Abstract: This module takes in tracking information generated
#           by the track_step module, and generates audio data
#           based on that information.
# Author: Jacob Erickson
# Class: CST205 - Multimedia Programming
# Date: 12/11/2017

import numpy as np

from scipy.io.wavfile import write

def run(tracking):
    pass
#<<<<<<< HEAD
#=======
    create_audio(tracking)

#>>>>>>> 7671fd093b3fcd980a062f0494aa34907698b8be
def create_audio(tracking):
    samples_s = 44100
    duration_s = 0.15

    waveform = []
    waveform_2 = []

    for item in tracking:
        note = 400 + item[0]
        speed = item[1] / 1000

        sample_nums_x = np.arange((duration_s - speed) * samples_s)
        sample_nums_y = np.arange(speed * samples_s)

        waveform = np.append(waveform, np.sin(2 * np.pi * sample_nums_x * note / samples_s))
        waveform_2 = np.append(waveform, np.sin(2 * np.pi * sample_nums_y * speed / samples_s))

    waveform_quiet = waveform * 0.3
    waveform_quiet_2 = waveform * 0.3

    waveform_integers = np.int16(waveform_quiet * 32767)
    waveform_integers_2 = np.int16(waveform_quiet_2 * 32767)

    write('static/created_sound.wav', samples_s, waveform_integers)
