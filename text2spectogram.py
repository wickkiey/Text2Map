 # -*- coding: utf-8 -*-

from gtts import gTTS
import os
from os import path
import librosa
import librosa.display
from pydub import AudioSegment

names = open('name_list.txt','r').read().split('\n')

audio = gTTS(names[0]*66)
audio.save('aranmagan.mp3')


sound = AudioSegment.from_mp3(r"C:\code_base\wickkiey_git\audio_map\aranmagan.mp3")
sound.export("a.wav", format="wav")

x , sr = librosa.load("a.wav",sr=44100)
for name in names:
    if not path.exists("audio/"+name+".mp3"):
        