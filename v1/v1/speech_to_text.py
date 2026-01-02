import sounddevice as sd
import numpy as np
import whisper
import scipy.io.wavfile as wav

RATE = 16000
DURATION = 5
FILENAME = "input.wav"

model = whisper.load_model("base")

def listen():
    print("🎤 Listening...")
    audio = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=1, dtype="int16")
    sd.wait()

    wav.write(FILENAME, RATE, audio)

    print("🧠 Transcribing...")
    result = model.transcribe(FILENAME)
    return result["text"].strip()
