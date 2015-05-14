from pygame.locals import *

## Pointers ##
notes = ['c3', 'd3', 'e3', 'f3']    # the notes
wav = {}                            # wav format file names
identifier = {'c3':K_1,             # identifiers in a dictionary
              'd3':K_2,
              'e3':K_3,
              'f3':K_4}
for n in notes: wav[n] = "wav/" + n + ".wav"