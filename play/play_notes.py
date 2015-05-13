# play sounds from wav files with key presses
# run from commandline: EG
#
# >> python play_notes.py

# NB: PyAudio needs to be installed

from wav_thread import *
from pygame_helper import *
import pygame

notes = ['c', 'd']
wav = {}                        # wav format file names in a dictionary
wav['c'] = r"test.wav"
wav['d'] = r"test.wav"
identifier = {}                 # identifiers in a dictionary
identifier['c'] = pygame.K_c
identifier['d'] = pygame.K_d

def main():

    # init pygame screen
    scr, bg = init_pygame(notes)

    t = []              # holds the running wav threads
    isPressed = {}      # isPressed dictionary with boolean isPressed? for all notes

    running = True
    while running:

        # acquire key press and play keys
        keys = pygame.key.get_pressed()
        for note in notes:
            if keys[identifier[note]] and not isPressed[note]:
                isPressed[note] = True
                play_note(note, t)
            elif not keys[identifier[note]]:
                isPressed[note] = False

        t = remove_finished_threads(t)  # remove finished threads
        scr, running = display(scr, bg) # display

    # quit pygame
    pygame.quit()

# helper functions

# play a note from notes if it is pressed down and update isPressed
def play_note(note, threads):
        try:
            threads.append(WavThread(wav[note]))
            threads[-1].start()
            print note
        except IOError: pass


# remove finished WavThreads
def remove_finished_threads(threads):
    for t in threads:
        if not t.isAlive():
            t.handled = True
    threads = [t for t in threads if not t.handled]
    return threads

main()
