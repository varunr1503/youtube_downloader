from moviepy.editor import *

mp4_file = r'C:\Users\varun\PycharmProjects\ITE project\SAVE_PATH\rickroll.mp4'
mp3_file = r'C:\Users\varun\PycharmProjects\ITE project\SAVE_PATH\rickroll-converted-file.mp3'


videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()





