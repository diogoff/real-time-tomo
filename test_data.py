from __future__ import print_function

import sys
import data
import h5py
import numpy as np

# ----------------------------------------------------------------------

if len(sys.argv) < 2:
    print('Usage: %s pulse pulse pulse ...' % sys.argv[0])
    exit()
    
pulses = [int(pulse) for pulse in sys.argv[1:]]

# ----------------------------------------------------------------------

fname = 'test_data.hdf'
print('Writing:', fname)
f = h5py.File(fname, 'w')

for pulse in pulses:
    print('pulse:', pulse)

    bolo, bolo_t = get_bolo(pulse)
    print('bolo:', bolo.shape, bolo.dtype)
    print('bolo_t:', bolo_t.shape, bolo_t.dtype)
    
    pulse = str(pulse)
    if pulse in f:
        del f[pulse]

    g = f.create_group(pulse)
    g.create_dataset('bolo', data=bolo)
    g.create_dataset('bolo_t', data=bolo_t)

f.close()
