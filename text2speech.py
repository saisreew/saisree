import os,time
from gtts import gTTS
mytext = 'welcome to vizag,my name is motu patulu!'
language = 'en'
time.sleep(9)
mytext1 = 'welcome to srkr!'
time.sleep(9)
mytext2 = 'welcome to cse!'
myobj = gTTS(text=mytext+mytext1+mytext2, lang=language, slow=False)
myobj.save("welcome.mp3")
os.startfile("welcome.mp3")
