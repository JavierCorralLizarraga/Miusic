# -*- coding: utf-8 -*-

# play files 

from playsound import playsound
playsound('soniditos/StarWars3.wav')

#%%
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("sound.wav")
play(song)

#%%
