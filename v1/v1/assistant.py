import tkinter as tk
import threading
from speech_to_text import listen
from text_to_speech import speak

def speak_from_mic():
    status.set("🎤 Listening...")
    window.update()

    text = listen()

    if text.strip() == "":
        status.set("No speech detected.")
        return

    show(text)

def speak_from_text():
    text = entry.get()
    if text.strip():
        show(text)

def show(text):
    output.config(state="normal")
    output.insert("end", f"You: {text}\n")
    output.see("end")
    output.config(state="disabled")

    speak(text)
    status.set("Ready")

# ---------------- GUI ----------------
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("500x420")

title = tk.Label(window, text="🎙 Voice Assistant", font=("Arial", 18))
title.pack(pady=10)

output = tk.Text(window, height=12, wrap="word")
output.pack(padx=10, pady=5)
output.config(state="disabled")

entry = tk.Entry(window, width=40)
entry.pack(pady=5)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

mic_btn = tk.Button(btn_frame, text="🎤 Speak", width=15,
                    command=lambda: threading.Thread(target=speak_from_mic).start())
mic_btn.grid(row=0, column=0, padx=10)

text_btn = tk.Button(btn_frame, text="⌨ Send Text", width=15,
                     command=speak_from_text)
text_btn.grid(row=0, column=1, padx=10)

status = tk.StringVar(value="Ready")
tk.Label(window, textvariable=status).pack(pady=5)

window.mainloop()
