from __future__ import print_function

import h5py
import numpy as np
import tensorflow as tf

# ----------------------------------------------------------------------

fname = 'train_data.hdf'
print('Reading:', fname)
f = h5py.File(fname, 'r')

X = []
Y = []

for uid in f:
    g = f[uid]
    for pulse in g:
        h = g[pulse]
        bolo = h['bolo'][:]
        tomo = h['tomo'][:]
        for i in range(bolo.shape[0]):
            X.append(bolo[i])
            Y.append(tomo[i].flatten())

X = np.array(X)
Y = np.array(Y)

print('X:', X.shape, X.dtype)
print('Y:', Y.shape, Y.dtype)

# ----------------------------------------------------------------------

X = tf.constant(X, dtype=tf.float32)
Y = tf.constant(Y, dtype=tf.float32)

W = np.zeros((X.shape[1], Y.shape[1]), dtype=np.float32)
print('W:', W.shape, W.dtype)

W = tf.Variable(W)

loss = tf.reduce_mean(tf.abs(Y - tf.tensordot(X, W, 1)))

optimizer = tf.train.AdamOptimizer()

train = optimizer.minimize(loss)

# ----------------------------------------------------------------------

sess = tf.Session()

init = tf.global_variables_initializer()
sess.run(init)

print('%10s %10s' % ('epoch', 'loss'))
for epoch in range(10000):
    loss_value = sess.run([train, loss])[1]
    print('\r%10d %10.6f' % (epoch+1, loss_value), end='')

print()

# ----------------------------------------------------------------------

weights = sess.run(W)
print('weights:', weights.shape, weights.dtype)

fname = 'weights.txt'
print('Writing:', fname)
np.savetxt(fname, weights)
