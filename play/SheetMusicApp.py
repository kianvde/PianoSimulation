try:
    import sys
    import os
    from WavThread import *
    from time import sleep, time
    import string
except ImportError, err:
    print "couldn't load module. %s" % err
    sys.exit(2)

# App playing sheet music
def main():

    ## INPUT ##
    bpm = 220.
    input_file = "Greensleeves.txt"

    ## PROGRAM ##
    notes, music, wav = read_file(input_file)
    threads = start_wav_threads(notes, wav)

    countdown(bpm)
    # loop over the notes
    for i in range(min([len(music[note]) for note in notes])):
        t = time()
        # remove running note thread if the note is played and add a new one

        play_notes = {threads[note] for note in notes if music[note][i] is 1}
        stop_notes = {threads[note] for note in notes if music[note][i] is -1}

        for thread in stop_notes: thread.stop()
        for thread in play_notes: thread.play()

        sleep_time = 60/bpm-(time()-t)
        sleep(sleep_time)

    # terminate wav threads
    for note in notes:
        threads[note].terminate()

def read_file(input_file):
    music = {}
    notes = []
    f = open(input_file)
    lines = f.readlines()
    for line in lines:
        content = [x.rstrip() for x in line.split(" ")]
        notes.append(content[0].rstrip())
        music[content[0]] = [int(x) for x in content[1:] if x in ["-1", "0", "1"]]

    wav = {}
    path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    for n in notes: wav[n] = path + "\Notes\piano" + n + ".wav"

    print notes
    return notes, music, wav

def start_wav_threads(notes, wav):
    threads = {}
    for note in notes:
        t = time()
        while True:
            if time()-t > 10:
                print "problem accessing audio device, please close running instances"
                print note
                sys.exit(2)
            try:
                threads[note] = WavThread(wav[note])
            except IOError:
                continue
            break
        threads[note].start()

    return threads

def countdown(bpm):
    print "3",
    sleep(60/bpm)
    print "2",
    sleep(60/bpm)
    print "1",
    sleep(60/bpm)

main()
