try:
    import sys
    from WavThread import *
    import pygame
    from pygame.locals import *
    from pointers import *
    from time import time
except ImportError, err:
    print "couldn't load module. %s" % err
    sys.exit(2)

# app for playing the wav sounds created by a Piano simulation
class PianoApp:
    def __init__(self):
        self.running = True
        self.scr = None
        self._image_surf = None

        # initialize pygame
        pygame.init()
        self.scr = pygame.display.set_mode((1,1), pygame.HWSURFACE)
        pygame.display.set_caption('Piano')
        self.font = pygame.font.SysFont('Arial', 60)
        self.running = True

        # images
        self.up = pygame.image.load("img/key_up.png").convert()
        self.down = pygame.image.load("img/key_down.png").convert()
        self.w = self.up.get_width()
        self.h = self.up.get_height()

        self.threads = {}       # dict .wav threads
        self.isPressed = {}     # holds key press booleans

        # initialize .wav threads
        for note in notes:
            self.isPressed[note] = False
            t = time()
            while True:
                if time()-t > 5:
                    print "problem accessing audio device, please close running instances"
                    sys.exit(2)
                try:
                    self.threads[note] = WavThread(wav[note])
                except IOError: continue
                break
            self.threads[note].start()

        # set screen to correct size
        self.scr = pygame.display.set_mode((len(notes)*self.w,
                                            self.h), pygame.HWSURFACE)

    def event(self, event):
        if event.type == QUIT:
            self.running = False

    def render(self):
        for i, note in enumerate(notes):
            if self.isPressed[note]:
                self.scr.blit(self.down,((i*self.w,0)))
            else:
                self.scr.blit(self.up,((i*self.w,0)))

            self.scr.blit(pygame.transform.rotate(self.font.render(note, True, (0,0,0)),90),
                         ((i+.5)*self.w-30, 10))

        pygame.display.flip()

    def cleanup(self):
        for note in notes:
            self.threads[note].terminate()
        pygame.quit()

    def run(self):

        while(self.running):

            keys = pygame.key.get_pressed()
            (lm, mm, rm) = pygame.mouse.get_pressed()
            (x, y) = pygame.mouse.get_pos()

            # play notes
            for i, note in enumerate(notes):
                if keys[identifier[note]] or \
                   (lm and x<(i+1)*self.w and x>i*self.w):
                    if not self.isPressed[note]:
                        self.threads[note].play()
                        self.isPressed[note] = True
                else:
                    self.isPressed[note] = False

            # act on events
            for event in pygame.event.get():
                self.event(event)
            self.render()

        self.cleanup()

# run the app
pianoApp = PianoApp()
pianoApp.run()
