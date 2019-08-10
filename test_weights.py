from __future__ import print_function

import h5py
import numpy as np

# ----------------------------------------------------------------------

fname = 'weights.npy'
print('Reading:', fname)
weights = np.load(fname)
print('weights:', weights.shape, weights.dtype)

# ----------------------------------------------------------------------

fname = 'test_data.hdf'
print('Reading:', fname)
f = h5py.File(fname, 'a')

# ----------------------------------------------------------------------

for pulse in f:
    print('pulse:', pulse)

    g = f[pulse]
    bolo = g['bolo'][:]
    bolo_t = g['bolo_t'][:]
    print('bolo:', bolo.shape, bolo.dtype)
    print('bolo_t:', bolo_t.shape, bolo_t.dtype)

    tomo = np.matmul(bolo, weights)
    tomo_t = bolo_t
    print('tomo:', tomo.shape, tomo.dtype)
    print('tomo_t:', tomo_t.shape, tomo_t.dtype)

    if 'tomo' in g:
        del g['tomo']
        del g['tomo_t']
    g.create_dataset('tomo', data=tomo)
    g.create_dataset('tomo_t', data=tomo_t)

# ----------------------------------------------------------------------

f.close()
