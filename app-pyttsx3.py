import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')  # Get the available voices
# Select a voice that sounds realistic
# For example, to select the first available voice:
engine.setProperty('voice', voices[0].id)

# Adjust the speech rate (default is 200)
# You can experiment with different values to find the desired pace
engine.setProperty('rate', 150)

with open('script.txt', 'r') as file:
    text = file.read()

output_file = 'output-p.mp3'
engine.save_to_file(text, output_file)

engine.runAndWait()
