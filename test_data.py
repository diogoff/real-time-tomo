from __future__ import print_function

import sys
import data
import h5py
import numpy as np

# ----------------------------------------------------------------------

if len(sys.argv) < 2:
    print('Usage: %s pulse' % sys.argv[0])
    exit()
    
pulse = int(sys.argv[1])
print('pulse:', pulse)

# ----------------------------------------------------------------------

fname = 'test_data.hdf'
print('Writing:', fname)
f = h5py.File(fname, 'a')

bolo, bolo_t = data.get_bolo(pulse)

pulse = str(pulse)
if pulse in f:
    del f[pulse]

g = f.create_group(pulse)
g.create_dataset('bolo', data=bolo)
g.create_dataset('bolo_t', data=bolo_t)

f.close()
