from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')

@app.post("/upload_file")
def upload_file():
    f = request.files['file']
    f.save('upload.wav')
    return render_template('upload_file.html')

@app.get("/download_file")
def download_file():
    file_path = 'upload.wav'
    mime_type = 'audio/wav'

    return send_file(file_path, mimetype=mime_type)

