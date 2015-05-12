# play sounds from wav files with key presses
# run from commandline: EG "python play_notes.py" in git Bash

import string
from msvcrt import getch
import pyaudio
import wave

chunk = 1024
# wav format file names in a dictionary
wav = {}
wav['c'] = r"stiffness/stiffness_4.50e03.wav"

# play a note upon key press
def play_note(note):
    # open wav file and stream
    current_note = wave.open(wav[note],"rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(current_note.getsampwidth()),
                    channels = current_note.getnchannels(),
                    rate = current_note.getframerate(),
                    output = True)

    # read and play
    data = current_note.readframes(chunk)
    while data != '':
        stream.write(data)
        data = current_note.readframes(chunk)

    # close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

# run while user does not press q
note = string.lower(getch())
while True:
    print note,
    if note in ['c']:
        play_note(note)
    elif note == 'q':
        break
    note = string.lower(getch())