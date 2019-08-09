from __future__ import print_function

import sys
import h5py
import time
import numpy as np
np.random.seed(0)
import tensorflow as tf
tf.set_random_seed(0)

# ----------------------------------------------------------------------

fname = 'tomo_data.hdf'
print('Reading:', fname)
f = h5py.File(fname, 'r')

X = []
Y = []

for pulse in f:
    g = f[pulse]
    bolo = g['bolo'][:]
    tomo = g['tomo'][:]
    for i in range(bolo.shape[0]):
        X.append(bolo[i])
        Y.append(tomo[i].flatten())

X = np.array(X)
Y = np.array(Y)

print('X:', X.shape, X.dtype)
print('Y:', Y.shape, Y.dtype)

# ----------------------------------------------------------------------

X = tf.constant(X)
Y = tf.constant(Y)

input('Press any key...')
exit()

# ----------------------------------------------------------------------

import theano
import theano.tensor as T
from theano.printing import pydotprint

X = theano.shared(X, 'X')
Y = theano.shared(Y, 'Y')
M = theano.shared(M, 'M')

loss = T.mean(T.abs_(T.dot(M, Y) - X))

grad = T.grad(loss, M)

# ----------------------------------------------------------------------

lr = 0.01
momentum = 0.999

m = theano.shared(M.get_value() * np.float32(0.))
v = momentum * m - lr * grad

updates = []
updates.append((m, v))
updates.append((M, M + momentum * v - lr * grad))

# ----------------------------------------------------------------------

train = theano.function(inputs=[], outputs=[loss], updates=updates)

pydotprint(train, outfile='train.png', compact=False)  

# ----------------------------------------------------------------------

epochs = 1000000

fname = 'train.log'
print('Writing:', fname)
f = open(fname, 'w')

print('%-10s %10s %20s' % ('time', 'epoch', 'loss'))

try:
    t0 = time.time()
    for epoch in range(epochs):
        outputs = train()
        loss_value = outputs[0]
        t = time.strftime('%H:%M:%S', time.gmtime(time.time()-t0))
        print('\r%-10s %10d %20.12f' % (t, epoch+1, loss_value), end='')
        sys.stdout.flush()
        f.write('%-10s %10d %20.12f\n' % (t, epoch+1, loss_value))
except KeyboardInterrupt:
    pass
print()

f.close()

# -------------------------------------------------------------------------

M = M.get_value()

print('M:', M.shape, M.dtype)

fname = 'M.npy'
print('Writing:', fname)
np.save(fname, M)
