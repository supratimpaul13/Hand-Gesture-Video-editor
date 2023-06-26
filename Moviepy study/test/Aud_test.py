from moviepy.editor import *

main_vid = VideoFileClip("test/vid5.mp4").subclip(0, 30)
main_vid = main_vid.without_audio()

main_audio = AudioFileClip("test/aud_test2.mp3")

final_vid = main_vid.set_audio(main_audio)
final_vid.write_videofile("test/Aud_testVid.mp4")