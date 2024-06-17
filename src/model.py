import whisper
from parameters import MODEL



class model:
    def __init__(self,model = MODEL):
        self.model             = whisper.load_model(model)
        self.input_audio_file  = None
        self.result = None
        self.text   = None
    
    def transcribe(self, input):
        self.input_audio_file  = input
        self.result = self.model.transcribe(self.input_audio_file,initial_prompt = "以下是简体中文。")
    
    def getText(self):
        self.text = self.result["text"]
        print(self.text)


# demo = model()
# demo.transcribe("output3.wav")
# demo.getText()
# print(demo.text)