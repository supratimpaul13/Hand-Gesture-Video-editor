from moviepy.editor import *

# Suclip() function allows to cut a section of the video from 0 secs to 5 secs
video = VideoFileClip("vid1.mp4").subclip(00, 5)
# Creating gif file
video.write_gif("test2.gif")

# Rotating for 180 deg
video = VideoFileClip("vid1.mp4").subclip(00, 5).rotate(180)
video.write_gif("test3.gif")