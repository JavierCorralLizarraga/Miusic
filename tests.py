# -*- coding: utf-8 -*-

# play files 

from playsound import playsound
playsound('soniditos/StarWars3.wav')

#%%  sounddevice for np arrays containing audio signals

import sounddevice as sd
import soundfile as sf

data, fs = sf.read('soniditos/StarWars3.wav')
sd.play(data, fs)
sd.wait()

# definitely better library

#%%