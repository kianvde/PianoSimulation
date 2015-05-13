import pygame

def init_pygame(notes):
    # init pygame screen
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    pygame.display.set_caption('Piano')

    # Fill background
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((250, 250, 250))

    # welcome text
    str = "press:"
    for note in notes: str += " '{0}',".format(note)
    str = str[0:len(str)-1]
    str += " to play"

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render(str, 1, (10, 10, 10))
    position = text.get_rect()
    position.centerx = bg.get_rect().centerx
    bg.blit(text, position)

    # Blit everything to the screen
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    return screen, bg

# update pygame frame
def display(screen, bg):

    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    return screen, running
