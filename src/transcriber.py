import whisper
from parameters import MODEL, VOICE_FILE



class transcribe_model:
    
    def __init__(self,model = MODEL):
        self.model             = whisper.load_model(model)
        self.input_audio_file  = None
        self.result = None
        self.text   = None
    
    def transcribe(self,file = VOICE_FILE):
        self.input_audio_file  = file
        self.result = self.model.transcribe(self.input_audio_file,initial_prompt = "以下是简体中文。")
    
    def getText(self):
        self.text = self.result["text"]
        return self.text




# demo = model()
# demo.transcribe("output3.wav")
# demo.getText()
# print(demo.text)