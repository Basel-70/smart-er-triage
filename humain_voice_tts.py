from humain_voice.tts import TTSClient
from humain_voice.tts.constants import TtsModel
import sounddevice as sd
import numpy as np

# This function uses the Humain TTS API to convert text to speech and play it through the speakers.
def speak(text):
 
 client =TTSClient(
 api_key = "HUMAIN_API_KEY",
 api_url="https://api.voice.humain.com"
 )

 voices =  client.list_voices_sync(timeout_seconds = 5.0)

 if not voices:
   raise RuntimeError("No voices found")


 voice = next(item for item in voices if "mul_abdullah" in item["label"].lower())

 model = TtsModel.Nebula


 pcm =  client.synthesize_sync(
    text,
    voice_id=voice["id"],
    model=model,
    timeout_seconds=10.0,
 )

 audio = np.frombuffer(pcm, dtype=np.int16)
 sd.play(audio, samplerate=24000)
 sd.wait()

 client.close_sync()