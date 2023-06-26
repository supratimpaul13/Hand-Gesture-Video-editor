from moviepy.editor import *

clip = VideoFileClip("vid2.mp4").subclip(00, 20)

txt_clip = TextClip("Shown Text", fontsize=100, color= "White")

txt_clip = txt_clip.set_position("center").set_duration(10)

video = CompositeVideoClip([clip, txt_clip])

video.write_videofile("txt_text.mp4")
