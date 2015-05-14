try:
    import sys
    from WavThread import *
    from pointers import *
    from time import sleep, time
except ImportError, err:
    print "couldn't load module. %s" % err
    sys.exit(2)

# App playing sheet music

## INPUT ##
# 1 is play note
# -1 is stop note
bpm = 120.
music = {'c3':[1, 0, 1, 0, 1, -1, 1, -1, 1, -1],
         'cd3':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'd3':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'dd3':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'e3':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'f3':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         'fd3':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],}


## PROGRAM ##
threads = {}
p = pyaudio.PyAudio()

# start wav threads
for note in notes:
    t = time()
    while True:
        if time()-t > 5:
            print "problem accessing audio device, please close running instances"
            sys.exit(2)
        try:
            threads[note] = WavThread(wav[note])
        except IOError: continue
        break
    threads[note].start()

# loop over the notes
for i in range(min([len(music[note]) for note in notes])):
    t = time()
    # remove running note thread if the note is played and add a new one
    for note in notes:
        if music[note][i]==1:
            threads[note].play()
        elif music[note][i] == -1:
            threads[note].stop()

    sleep(60/bpm-(time()-t))

# terminate wav threads
for note in notes:
    threads[note].terminate()