from parameters import SECONDS, FRAMES_PER_BUFFER, FORMAT, CHANNELS, RATE, VOICE_FILE
import pyaudio
import wave

class voice_record:
    
    def __init__(self, 
                seconds = SECONDS,
                frames_per_buffer = FRAMES_PER_BUFFER,
                format = FORMAT,
                channels = CHANNELS,
                rate = RATE):
        self.seconds           = seconds
        self.frames_per_buffer = frames_per_buffer
        self.format            = format
        self.channels          = channels
        self.rate              = rate
        self.audio             = pyaudio.PyAudio()
        self.output            = VOICE_FILE
        self.frames            = []

    def record(self):
        stream = self.audio.open(
            format              = self.format,
            channels            = self.channels,
            rate                = self.rate,
            input               = True,
            frames_per_buffer   = FRAMES_PER_BUFFER
        )
        print("start recording")
        seconds = self.seconds
        self.frames = []
        for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
            data = stream.read(FRAMES_PER_BUFFER)
            self.frames.append(data)
        stream.stop_stream()
        stream.close()
        self.audio.terminate()
        print("end recording")

    def output(self):
        if self.frames is not None:
            obj = wave.open(self.output,"wb")
            obj.setnchannels(CHANNELS)
            obj.setsampwidth(self.audio.get_sample_size(FORMAT))
            obj.setframerate(RATE)
            obj.writeframes(b"".join(self.frames))
            obj.close()
        else:
            print("No Voice Recorded Warning")
    
    def run(self):
        self.record()
        self.output()


# demo = input()
# demo.record()
# demo.final_output()