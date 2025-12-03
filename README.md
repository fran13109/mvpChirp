# MVP Chirp TTS



A MVP Text-to-Speech (TTS) project using Flask and Google Cloud Text-to-Speech

It allows generating audios from text, playing them immediately, and browsing all previously generated audios in a scrollable media player.



## Features



Text to speech (TTS) audio generation with multiple voices:



English Female (US)



Spanish Neutral



Spanish Female



Spanish Male



Main audio player plays the latest generated audio automatically.



Scrollable list of previously generated audios with individual players.



Modern dark UI with custom font (Science Gothic).



Cross-platform browser support.



## Requirements



Python 3.10+



Google Cloud Service Account with Text-to-Speech permissions



Python packages (listed in requirements.txt)



## Installation



1. Clone the repository:

   git clone <REPO\_URL>
   cd MVP-Chirp-TTS
   
2. Create a virtual environment:

   python -m venv venv
   # Linux / Mac
   source venv/bin/activate
   # Windows
   venv\\Scripts\\activate
   
3. Install dependencies:



pip install -r requirements.txt



## Usage

## 

1. Run the application:

   python main.py
   
2. Open browser

   http://127.0.0.1:5000
   
3. Use the interface (UI)



Enter the text to convert into audio.



Select the voice.



Click Generate Audio.



The main audio player plays the newly generated audio automatically.



All previously generated audios appear in a scrollable list with individual players.

&nbsp;	

## How It Works

## 

##### Frontend:



* index.html: main interface.



* style.css: modern dark UI styling.



* script.js: handles:



&nbsp;	-Sending text to backend.



&nbsp;	-Playing the main audio.



&nbsp;	-Loading previous audios in the scrollable container.



##### Backend (Flask):

#### 

* / → renders the main page.



* /generate → receives text and voice, generates audio using tts.py, and returns the audio.



* /audios → returns JSON list of generated audios.



* /output/<filename> → serves audio files.





#### tts.py:



* Uses Google Cloud Text-to-Speech.



* Supports multiple voices and genders.



* Saves audios in output/.

## 

## requirements.txt



Flask==2.3.4

google-cloud-texttospeech==2.16.1

google-auth==2.22.0



Versions can be adjusted according to your environment.





