from pydub import AudioSegment

audio = AudioSegment.from_wav("test.wav")

# # increase the volume by 6db
# audio = audio + 6

# # repeat
# audio = audio * 2

# #fade in
# audio = audio.fade_in(2000)

audio.export("test.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("test.mp3")
print("done")