import ffmpeg
from ffmpeg.nodes import *
"""This step takes the generated audio data and the original video, and merges them together, outputting the final video"""

def run(audio,video):
    local_audio=_convert_audio(audio)
    local_video=_convert_video(video)
    result=ffmpeg.input(local_video,c='copy').input(local_audio,c='aac').output('test.mp4')
    return 'test.mp4'
def _test():
    audio_file='TestAudio1.wav'
    video_file='VideoTest1.mp4'
    vi=ffmpeg.input(video_file,c='copy')
    ai=ffmpeg.input(audio_file,c='aac')
    help(ai)
    (ffmpeg
    
        .input(video_file,c='copy')
        .input(audio_file,c='aac')
        .output('test.mp4')
        .run())

def _convert_audio(audio):
    return None
def _convert_video(video):
    return None

if(__name__=='__main__'):
    _test()