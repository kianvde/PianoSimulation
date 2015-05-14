from pygame.locals import *

## Pointers ##
notes = ['c3', 'cd3', 'd3', 'dd3', 'e3', 'f3', 'fd3']
wav = {}                            # wav format file names
identifier = {'c3':K_1,             # identifiers in a dictionary
              'cd3':K_2,
              'd3':K_3,
              'dd3':K_4,
              'e3':K_5,
              'f3':K_6,
              'fd3':K_7}

for n in notes: wav[n] = "wav/" + n + ".wav"