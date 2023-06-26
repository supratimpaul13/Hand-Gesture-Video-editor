from moviepy.editor import *

clip = VideoFileClip("merge/vid2.mp4").subclip(27, 45)
clip = clip.margin(60)

clip.write_videofile("screenshot/margin_video.mp4")