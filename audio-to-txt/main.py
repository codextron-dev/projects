// pip install whisper
import whisper

// your audio file here
file = "audio.mp3"

model = whisper.load_model("base")
text = model.transcribe(file)["text"]

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\nTranscript: \n", text)