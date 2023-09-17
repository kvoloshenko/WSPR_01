# https://analyzingalpha.com/openai-whisper-python-tutorial
import whisper
model = whisper.load_model("base")
result = model.transcribe("20230913_ARS_Job_ODDT.m4a", verbose = True)
print(result["text"])