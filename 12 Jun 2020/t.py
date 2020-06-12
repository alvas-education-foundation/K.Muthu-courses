from gtts import gTTS
import os
s = 'hello how are u'
l = 'en'
speech = gTTS(text = s , lang = l , slow = False)
speech.save('text.mp3')
os.system("mpg123 text.mp3")