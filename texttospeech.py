from gtts import gTTS
import os

Script= input("Enter Filename to ReadFrom (With Extension): ")
file = open(Script)
text = file.read()

language = 'en'

obj= gTTS(text=text, lang=language, slow=False, )
Filename= input("Enter Audio Filename to Save (With Extension): ")
obj.save(Filename)

os.system("start " + Filename)