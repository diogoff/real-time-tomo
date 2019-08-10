from __future__ import print_function

import sys
import data
import numpy as np

# ----------------------------------------------------------------------

if len(sys.argv) < 2:
    print('Usage: %s pulse' % sys.argv[0])
    exit()
    
pulse = int(sys.argv[1])
print('pulse:', pulse)

# ----------------------------------------------------------------------

bolo, bolo_t = data.get_bolo(pulse)

fname = 'bolo.txt'
print('Writing:', fname)
np.savetxt(fname, bolo)

fname = 'bolo_t.txt'
print('Writing:', fname)
np.savetxt(fname, bolo_t)
