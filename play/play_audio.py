__author__ = 'kian'
import pyglet
player = pyglet.media.Player()
song = pyglet.media.load('starwars.wav')
player.queue(song)
player.play()
pyglet.app.run()









import scipy.io.wavfile
import os
import matplotlib.pyplot as plt
import numpy as np
import binascii
# import wave
# os.chdir('/home/kian/Documents/PianoSimulation')
# filename = 'thousand.wav'
#
# f = wave.open(filename, 'rb')
# a = f.readframes(2)
# print
# a = scipy.io.wavfile.read(filename)[1]
# x= range(len(a))
# plt.figure()
# plt.plot(x[0:1000],a[0:1000])
# plt.show()