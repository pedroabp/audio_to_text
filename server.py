from flask import Flask, render_template, request, send_file
import speech_recognition as sr
import random
import sys

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')

@app.post("/upload_file")
def upload_file():
    file_path = 'upload.wav'
    f = request.files['file']
    f.save(file_path)
    text = convert_audio_to_text(file_path)
    random_number = random.randint(0, sys.maxsize)

    return render_template('upload_file.html', text=text, random_number=random_number)

@app.get("/download_file")
def download_file():
    file_path = 'upload.wav'
    mime_type = 'audio/wav'

    return send_file(file_path, mimetype=mime_type)

def convert_audio_to_text(audio_file):
    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Read the audio data from the file
        audio_data = r.record(source)
        
        try:
            # Use the recognizer to convert audio to text
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
    
    return None
