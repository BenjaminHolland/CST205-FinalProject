import ffmpeg
"""This step takes the generated audio data and the original video, and merges them together, outputting the final video"""
def run(audio,video):
    local_audio=_convert_audio(audio)
    local_video=_convert_video(video)
    result=ffmpeg
        .input(local_video,c='copy')
        .input(local_audio,c='aac')
        .output('test.mp4')
        
    
    return 'test.mp4'
    pass
def _convert_audio(audio):
    return None
def _convert_video(video):
    return None