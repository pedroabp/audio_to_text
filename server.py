from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')

@app.post("/")
def index_post():
    f = request.files['file']
    f.save('upload.wav')
    return 'Saved'
