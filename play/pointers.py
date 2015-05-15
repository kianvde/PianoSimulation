from pygame.locals import *
import os

## Pointers ##
notes = ['C3',   'Cd3', 'D3', 'Dd3', 'E3', 'F3', 'Fd3', 'G3', 'Ab3', 'A3', 'B3',
         'C4',   'Cd4', 'D4', 'Dd4', 'E4', 'F4']
_keys = [ K_TAB,  K_1,   K_q,  K_2,   K_w,  K_e,  K_4,   K_r,  K_5,   K_t,  K_y,
          K_u,    K_8,   K_i,  K_9,   K_o,  K_p]

wav = {}                    # wav format file names
path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
for n in notes: wav[n] = path + "\Notes\piano" + n + ".wav"

identifier = {}            # identifiers in a dictionary
for i, n in enumerate(notes): identifier[n] = _keys[i]

