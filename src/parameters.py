import pyaudio

MODEL = "small"
SECONDS = 5
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
API_KEY = "yu8lgY4lwH94kiUJnQgxEBGu"
SECRET_KEY = "oE4trjoKjkrPKnpiKGYXjXxai3B9oWrG"
HEADERS = {'Content-Type': 'application/json'}
VOICE_FILE = "voice_record.wav"
