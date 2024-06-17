import whisper

model = whisper.load_model("tiny")
result = model.transcribe("output2.wav")
print(result["text"])