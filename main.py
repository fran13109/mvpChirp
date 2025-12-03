from flask import Flask, render_template, request, send_from_directory
from tts import generate_audio
import os
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form.get("texto")
    voice = request.form.get("voz", "en-US-Female") 

    if not text:
        return "No text received", 400

    filename = f"{uuid.uuid4()}.mp3" 

    try:
        generate_audio(text, filename, voice)
    except Exception as e:
        return f"Error generating audio: {e}", 500

    return send_from_directory(os.path.abspath("output"), filename)

@app.route("/audios")
def list_audios():
    """Returns list of previously generated audios"""
    output_dir = os.path.abspath("output")
    if not os.path.exists(output_dir):
        return {"audios": []}

    audios = [f for f in os.listdir(output_dir) if f.endswith(".mp3")]
    audios.sort(reverse=True) 
    return {"audios": audios}

@app.route("/output/<filename>")
def serve_audio(filename):
    return send_from_directory(os.path.abspath("output"), filename)

if __name__ == "__main__":
    app.run(debug=True)
