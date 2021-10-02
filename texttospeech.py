from gtts import gTTS
import os

Script= input("Enter Filename to ReadFrom (With Extension): ")
file = open(Script)
text = file.read()

language = 'en'
accent = input("Enter the accent you want UK/USA/India/Australia:")
if accent.lower()=='uk':
    accent='co.uk'
elif accent.lower()=='usa':
    accent='com'
elif accent.lower()=='india':
    accent='co.in'
else:
    accent='com.au'
obj= gTTS(text=text, lang=language, slow=False,  tld=accent )

Filename= input("Enter Audio Filename to Save (With Extension): ")
obj.save(Filename)

os.system("start " + Filename)