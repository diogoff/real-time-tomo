from __future__ import print_function

import numpy as np

# ----------------------------------------------------------------------

fname = 'weights.txt'
print('Reading:', fname)
weights = np.loadtxt(fname)

print('weights:', weights.shape, weights.dtype)

# ----------------------------------------------------------------------

fname = 'bolo.txt'
print('Reading:', fname)
bolo = np.loadtxt(fname)

print('bolo:', bolo.shape, bolo.dtype)

fname = 'bolo_t.txt'
print('Reading:', fname)
bolo_t = np.loadtxt(fname)

print('bolo_t:', bolo_t.shape, bolo_t.dtype)

# ----------------------------------------------------------------------

tomo = np.matmul(bolo, weights)
tomo_t = bolo_t

print('tomo:', tomo.shape, tomo.dtype)
print('tomo_t:', tomo_t.shape, tomo_t.dtype)

# ----------------------------------------------------------------------

fname = 'tomo.txt'
print('Writing:', fname)
np.savetxt(fname, tomo)

fname = 'tomo_t.txt'
print('Writing:', fname)
np.savetxt(fname, tomo_t)
