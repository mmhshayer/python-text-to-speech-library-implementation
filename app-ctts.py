from TTS.api import TTS

model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)

with open('script.txt', 'r') as file:
    text = file.read()

# Text to speech to a file
tts.tts_to_file(text=text, speaker=tts.speakers[0], language=tts.languages[0], file_path="output-c.mp3")