from gtts import gTTS         # Google Text To Speech

def text_to_audio(text):      # Here text is input or attribute given
    x=gTTS(text)              
    x.save('audio.mp3')    # File will save as audio.mp3

text_to_audio('Drink Water  ')       # This audio will be played