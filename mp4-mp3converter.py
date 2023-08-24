from moviepy.editor import *

mp4_file = r'C:\Users\varun\PycharmProjects\ITE project\SAVE_PATH\rickroll.mp4'
mp3_file = r'C:\Users\varun\PycharmProjects\ITE project\SAVE_PATH\rickroll-converted-file.mp3'


videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()


////


# importing the module
import pytube
# where to save
SAVE_PATH = r"C:\Users\varun\PycharmProjects\ITE project\SAVE_PATH"

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
#link="https://www.youtube.com/watch?v=z9tsfkdgByA&ab_channel=SuiseiChannel"
try:
	# object creation using YouTube
	yt = pytube.YouTube(link)
except:
	print("Connection Error")

# setting title
yt.title = ('rickroll')

# get the video resolution through get_by_function() function

d_video = yt.streams.get_highest_resolution()
#d_video = yt.streams.get_by_resolution('720p')
#d_video = yt.streams.get_audio_only()

try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')



