from gtts import gTTS
import os,time
mytext = 'welcome to vizag,my name is motu patulu!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
# Playing the converted file
os.system("mpg321 welcome.mp3")
os.startfile('welcome.mp3')
time.sleep(9)
mytext1 = 'welcome to srkr!'
language = 'en'
# myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.startfile("welcome.mp3")
time.sleep(9)
mytext2 = 'welcome to cse!'
language = 'en'
myobj = gTTS(text=mytext+mytext1+mytext2, lang=language, slow=False)
myobj.save("welcome.mp3")
os.startfile("welcome.mp3")
