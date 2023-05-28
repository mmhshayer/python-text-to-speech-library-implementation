from gtts import gTTS

# Read the text file
with open('script.txt', 'r') as file:
    text = file.read()

# Convert the text to speech
tts = gTTS(text, lang='en-us', slow=False)

# Save the file
tts.save("output-g.mp3")