# Title: audio_step.py
# Abstract: This module takes in tracking information generated
#           by the track_step module, and generates audio data
#           based on that information.
# Author: Jacob Erickson
# Class: CST205 - Multimedia Programming
# Date: 12/11/2017

import numpy as np

from scipy.io.wavfile import write
from scipy.interpolate import interp1d
def calc_note(n):
    return 440*np.power(np.power(2,1/12.0),n-49)
notes=list([calc_note(i) for i in range(40,52)])

def lerp(a,b,x):
    return a+x*(b-a)
def run(tracking,video_id,herz):
    create_audio2(tracking,video_id,herz)
class SinWave:
    def __init__(self,sample_rate,freq,amp):
        self.phase_step=np.pi*2*freq/sample_rate
        self.current_frequency=freq
        self.current_amplitude=amp
        self.target_frequency=freq
        self.target_amplitude=amp
        self.phase=0
        self.sample_rate=sample_rate
    def sample(self):
        self.current_frequency=self.current_frequency+(self.target_frequency-self.current_frequency)*0.001
        self.phase_step=(np.pi*2*self.current_frequency)/self.sample_rate
        self.phase=self.phase+self.phase_step
        return self.current_amplitude*np.sin(self.phase)

    def change_frequency(self,freq):
        self.target_frequency=freq
    def change_amplitude(self,amp):
        self.current_amplitude=amp


def create_audio2(tracking,video_id,herz):

    sample_rate=44100
    #extract a bunch of info from the tracking step. We should probably be using dictionaries
    #but it's fine for now
    video_info=tracking[0]
    tracking_info=tracking[1]

    #calculate some stuff about the video that we need to generate audio
    samples_per_frame=int(sample_rate/video_info[0])
    total_samples=sample_rate*video_info[1]
    target_note=0


    sample=0
    waveform=np.array([0])
    width=video_info[2]
    height=video_info[3]

    wave1=SinWave(44100,herz,0.2)
    wave2=SinWave(44100,herz,0.2)

    #make some generators that let us wiggle the frequency around without
    #getting choppy phase crap
    wave1=SinWave(44100,440,0.2)
    wave2=SinWave(44100,440,0.2)

    dx=0
    dy=0
    px=0
    py=0
    first=True
    for center,dr in tracking_info:

        #get sample range for this frame. need to check if the range is actually correct.
        sample_start=sample;
        sample_end=sample+samples_per_frame
        #if we have a new center, update the wave
        if(center!=None):

            nx=(center[0]-width/2)/width
            ny=(center[1]-height/2)/height

            dx=0.5+nx; #[0,1]
            dy=0.5+ny; #[0,1]

            #do a bunch of math to calculate distance from the center and angle
            #normalized on the interval [0,1] so we cause use lerp for stuff

            #object coord on [-1,1] interval
            nx=2*((center[0]-width/2)/width)
            ny=2*((center[1]-height/2)/height)

            dx=nx; #[0,1]
            dy=ny; #[0,1]
            #calculate normalized distance away from center
            d=np.sqrt(dx*dx+dy*dy)/np.sqrt(2)

            #calculate normalized ange
            a=(1+np.arctan2(dy,dx)/np.pi)*0.5

            #update generator target frequencies
            wave1.change_frequency(calc_note(int(lerp(40,52,d))))
            wave2.change_frequency(calc_note(int(lerp(20,40,a))))

        #generate waveforms. If we dropped the tracked object, just use the stuff from last frame
        frame_waveform1=np.array([wave1.sample() for _ in range(0,samples_per_frame)])
        frame_waveform2=np.array([wave2.sample() for _ in range(0,samples_per_frame)])

        #add the waveforms together.
        frame_waveform=np.add(frame_waveform1,frame_waveform2)

        #increment the sample counter
        sample=sample+samples_per_frame

        #add the new samples to the list
        waveform=np.append(waveform,frame_waveform)

    #output the waveform
    formatted_waveform=np.int16(waveform * 32767)
    print(f'generated {len(formatted_waveform)} samples')
    write(f'static/{video_id}.wav',sample_rate, formatted_waveform)
    return 'static/{video_id}.wav'

def create_audio(tracking,video_id,intensity):

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

    write(f'static/{video_id}.wav', samples_s, (waveform_integers + waveform_integers_2))
    return 'static/{video_id}.wav'
