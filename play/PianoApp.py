# app for playing the wav sounds created by a Piano simulation

try:
    import sys
    from WavThread import *
    import pygame
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % err
    sys.exit(2)

## Pointers ##
notes = ['c', 'd', 'e']             # the notes
wav = {}                            # wav format file names
identifier = {'c':K_c,              # identifiers in a dictionary
              'd':K_d,
              'e':K_e}
for n in notes: wav[n] = n + ".wav"

## class ##
class PianoApp:
    def __init__(self):
        self.running = True
        self.scr = None
        self._image_surf = None

    def on_init(self):
        pygame.init()
        self.scr = pygame.display.set_mode((1,1), pygame.HWSURFACE)
        pygame.display.set_caption('Piano')
        self.font = pygame.font.SysFont('Arial', 60)
        self.running = True
        self.stop_on_release = False

        # images
        self.up = pygame.image.load("key_up.png").convert()
        self.down = pygame.image.load("key_down.png").convert()

        self.threads = []           # array .wav threads
        if self.stop_on_release:
            self.threads = {}       # dict .wav threads
        self.isPressed = {}         # holds key press booleans

        self.scr = pygame.display.set_mode((len(notes)*self.up.get_width(),
                                            self.up.get_height()), pygame.HWSURFACE)

    def on_event(self, event):
        if event.type == QUIT:
            self.running = False

    def on_render(self):
        for i, note in enumerate(notes):
            w = self.down.get_width()
            h = self.down.get_height()
            if self.isPressed[note]:
                self.scr.blit(self.down,((i*w,0)))
            else:
                self.scr.blit(self.up,((i*w,0)))

            self.scr.blit(self.font.render(note.upper(), True, (0,0,0)), ((i+.5)*w-16, 10))

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while(self.running):

            keys = pygame.key.get_pressed()
            for note in notes:
                if keys[identifier[note]] and not self.isPressed[note]:
                    self.isPressed[note] = True
                    self.play_note(note)
                elif not keys[identifier[note]]:
                    if note in self.isPressed:
                        if self.stop_on_release and self.isPressed[note] and note in self.threads:
                            self.threads[note].stop()
                            self.threads[note].join()
                    self.isPressed[note] = False

            self.remove_finished_threads()

            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

    def play_note(self, note):

        try:
            if self.stop_on_release:
                self.threads[note] = WavThread(wav[note])
                self.threads[note].start()
            else:
                self.threads.append(WavThread(wav[note]))
                self.threads[-1].start()
        except IOError: pass

    def remove_finished_threads(self):

        if self.stop_on_release:
            for note in self.threads:
                if not self.threads[note].isAlive():
                    self.threads[note].handled = True
            self.threads = {note:self.threads[note] for note in self.threads if not self.threads[note].handled}
        else:
            for t in self.threads:
                if not t.isAlive():
                    t.handled = True
            self.threads = [t for t in self.threads if not t.handled]

# run the app
pianoApp = PianoApp()
pianoApp.on_execute()
