# play sounds from wav files with key presses
# run from commandline: EG
#
# >> python play_notes.py

# NB: PyAudio needs to be installed

import string
try:
    from msvcrt import getch
except ImportError:
    import getch

from wav_thread import *

chunk = 1024
# wav format file names in a dictionary
wav = {}
wav['c'] = r"test.wav"
wav['d'] = r"test.wav"

notes = ['c', 'd']
threads = []

# run while user does not press q
note = string.lower(getch())
while True:

    # remove finished threads
    for t in threads:
        if not t.isAlive():
            t.handled = True
    threads = [t for t in threads if not t.handled]

    # play the note pressed if it is in notes
    if note in notes:
        # print note
        try:
            threads.append(WavThread(wav[note]))
            threads[-1].start()
        except IOError: pass
    elif note == 'q':
        break
    note = string.lower(getch())