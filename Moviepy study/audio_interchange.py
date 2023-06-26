from moviepy.editor import *

# clip1 = VideoFileClip("vid5.mp4").subclip(00, 20)
# clip1.audio.write_audiofile("aud_test1.mp3")

# clip2 = VideoFileClip("vid6.mp4").subclip(00, 20)
# clip2.audio.write_audiofile("aud_test2.mp3")

# clip1 = VideoFileClip("vid5.mp4").subclip(0, 20)
# clip1 = clip1.without_audio()
# clip1.write_videofile("test_w1.mp4")

vid_file = VideoFileClip("test_w1.mp4")
audio_file = AudioFileClip("aud_test2.mp3")

final_vid = vid_file.set_audio(audio_file)

final_vid.write_videofile("aud_vid_test1.mp4")