
import whisper

model = whisper.load_model("base")
result = model.transcribe("FilePath")
print(result["text"])
