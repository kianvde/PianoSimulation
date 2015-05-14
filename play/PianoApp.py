try:
    import sys
    from WavThread import *
    import pygame
    from pygame.locals import *
    from pointers import *
except ImportError, err:
    print "couldn't load module. %s" % err
    sys.exit(2)

# app for playing the wav sounds created by a Piano simulation
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

        # images
        self.up = pygame.image.load("img/key_up.png").convert()
        self.down = pygame.image.load("img/key_down.png").convert()

        self.threads = {}       # dict .wav threads
        self.isPressed = {}     # holds key press booleans
        for note in notes:
            self.isPressed[note] = False
            self.threads[note] = WavThread(wav[note])
            self.threads[note].start()

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

            # play notes
            for note in notes:
                if keys[identifier[note]]:
                    if not self.isPressed[note]:
                        self.threads[note].play()
                        self.isPressed[note] = True
                else:
                    self.isPressed[note] = False

            # act on events
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()

        self.on_cleanup()

# run the app
pianoApp = PianoApp()
pianoApp.on_execute()
