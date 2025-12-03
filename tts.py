from google.cloud import texttospeech
from google.oauth2 import service_account
import os
import uuid

cred_path = os.path.join(os.path.dirname(__file__), "service_account.json")
credentials = service_account.Credentials.from_service_account_file(cred_path)
client = texttospeech.TextToSpeechClient(credentials=credentials)

def generate_audio(text: str, filename: str = None, voice_type: str = "en-US-Female"):
    """
    Generate an MP3 audio file from text using Google Cloud Text-to-Speech
    """
    if filename is None:
        filename = f"{uuid.uuid4()}.mp3"

    synthesis_input = texttospeech.SynthesisInput(text=text)

    gender_map = {
        "es-ES-Neutral": texttospeech.SsmlVoiceGender.NEUTRAL,
        "es-ES-Female": texttospeech.SsmlVoiceGender.FEMALE,
        "es-ES-Male": texttospeech.SsmlVoiceGender.MALE,
        "en-US-Female": texttospeech.SsmlVoiceGender.FEMALE
    }

    language_map = {
        "es-ES-Neutral": "es-ES",
        "es-ES-Female": "es-ES",
        "es-ES-Male": "es-ES",
        "en-US-Female": "en-US"
    }

    ssml_gender = gender_map.get(voice_type, texttospeech.SsmlVoiceGender.NEUTRAL)
    language_code = language_map.get(voice_type, "en-US")

    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=ssml_gender
    )

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    try:
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
    except Exception as e:
        print(f"Error generating audio: {e}")
        raise

    os.makedirs("output", exist_ok=True)
    file_path = os.path.join("output", filename)

    with open(file_path, "wb") as out:
        out.write(response.audio_content)

    print(f"Audio generated: {file_path}")
    return file_path
