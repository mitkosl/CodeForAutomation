from urllib.request import urlopen
from playsound import playsound
from subprocess import call
from io import BytesIO
from gtts import gTTS
import pygame
import os
import sys

def checkInternet():
    try:
        urlopen("http://www.google.com")
        return True
    except urllib.error.URLError as e:
        print( "Network currently down." )
        return False

def speak(text):
    if checkInternet():
        speakBad(text)
    else:
        speakBad(text)

def speakGood(text):
#language = 'en'
#text = "Hello litle frogy"
#tts = gTTS(text=text, lang=language, slow=False) 
#tts.save("sound1.mp3")
#playsound("sound1.mp3")

    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False) 
    mp3_fp = BytesIO()

    ##tts.save("sound1.mp3")
    ##playsound("sound1.mp3")
    tts.save("audio.mp3")
    os.system("mpg321 -q  audio.mp3")
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    #pygame.mixer.init()
    #pygame.mixer.music.load(mp3_fp)
    #pygame.mixer.music.set_volume(0.9)
    #pygame.mixer.music.play()



def speakBad(text):
    #cmd_beg= 'espeak -vfr '
    cmd_beg = 'flite -voice awb -t "'
    cmd_end= '" 2>/dev/null'
    #text = text.replace(' ', '_')
    call([cmd_beg+text+cmd_end], shell=True)
