from WavThread import *
from pointers import *
from time import sleep, time

# App playing sheet music

## INPUT ##
bpm = 120.
music = {'c3':[1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
         'd3':[1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
         'e3':[0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
         'f3':[0, 0, 0, 1, 1, 0, 0, 0, 1, 1]}


## PROGRAM ##
threads = {}
p = pyaudio.PyAudio()

# start wav threads
for note in notes:
    threads[note] = WavThread(wav[note])
    threads[note].start()

# loop over the notes
for i in range(min([len(music[note]) for note in notes])):
    t = time()
    # remove running note thread if the note is played and add a new one
    for note in notes:
        if music[note][i]==1:
            threads[note].play()

    sleep(60/bpm-(time()-t))

# terminate wav threads
for note in notes:
    threads[note].terminate()