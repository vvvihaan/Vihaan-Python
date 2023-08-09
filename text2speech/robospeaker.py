# gtts= google text to speech
from gtts import gTTS
speech = gTTS("Vihaan is a good boy")
speech.save("audio.mp3")