from pygame.locals import *
import os

## Pointers ##
notes = ['C3', 'Cd3', 'D3', 'Dd3', 'E3', 'F3', 'Fd3', 'G3', 'Ab3', 'A3', 'B3']
_keys = [ K_w,  K_3,   K_e,  K_4,   K_r,  K_t,  K_6,   K_y,  K_7,   K_u,  K_i]

wav = {}                    # wav format file names
path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
for n in notes: wav[n] = path + "\Notes\piano" + n + ".wav"

identifier = {}            # identifiers in a dictionary
for i, n in enumerate(notes): identifier[n] = _keys[i]

