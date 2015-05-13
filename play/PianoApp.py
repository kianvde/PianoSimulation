# app for playing the wav sounds created by a Piano simulation

try:
    import sys
    from wav_thread import *
    import pygame
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % err
    sys.exit(2)

## Pointers ##
notes = ['c', 'd']                 # the notes
wav = {}                           # wav format file names
identifier = {'c':K_c,             # identifiers in a dictionary
              'd':K_d}
for note in notes: wav[note] = note + ".wav"

class PianoApp:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((800,500), pygame.HWSURFACE)
        pygame.display.set_caption('Piano')
        self._running = True
        self.key_down = False

        # images
        self.key_up_surf = pygame.image.load("key_up.png").convert()
        self.key_down_surf = pygame.image.load("key_down.png").convert()

        self.threads = []                       # running .wav threads
        self.isPressed = {}                     # holds key press booleans

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        if self.key_down:
            self._display_surf.blit(self.key_down_surf,(0,0))
        else:
            self._display_surf.blit(self.key_up_surf,(0,0))
        for i in range(8):
            self._display_surf.blit(self.key_up_surf,((i+1)*self.key_up_surf.get_width(),0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):

            keys = pygame.key.get_pressed()
            for note in notes:
                if keys[identifier[note]] and not self.isPressed[note]:
                    self.isPressed[note] = True
                    self.play_note(note)
                elif not keys[identifier[note]]:
                    self.isPressed[note] = False

            self.key_down = self.isPressed['c'] or self.isPressed['d']

            self.remove_finished_threads()

            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

    def play_note(self, note):
        try:
            self.threads.append(WavThread(wav[note]))
            self.threads[-1].start()
            print note
        except IOError: pass

    def remove_finished_threads(self):
        for t in self.threads:
            if not t.isAlive():
                t.handled = True
        self.threads = [t for t in self.threads if not t.handled]

# run the app
pianoApp = PianoApp()
pianoApp.on_execute()
