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
music = {notes[0]: [0],
         notes[1]: [0],
         notes[2]: [0],
         notes[3]: [0],
         notes[4]: [0],
         notes[5]: [0],
         notes[6]: [0],
         notes[7]: [0],
         notes[8]: [0],
         notes[9]: [0],
         notes[10]: [0]}


## PROGRAM ##
threads = {}

# start wav threads
for note in notes:
    t = time()
    while True:
        if time()-t > 10:
            print "problem accessing audio device, please close running instances"
            sys.exit(2)
        try:
            threads[note] = WavThread(wav[note])
        except IOError:
            continue
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