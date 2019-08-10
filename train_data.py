from __future__ import print_function

import data
import h5py
import numpy as np
import pyexcel_ods

# ------------------------------------------------------------------------------

fname = '/home/pcarval/kb/interp_tables/tomography_completed.reliable.ods'
print('Reading:', fname)
ods_data = pyexcel_ods.get_data(fname)

# ------------------------------------------------------------------------------

fname = 'train_data.hdf'
print('Writing:', fname)
f = h5py.File(fname, 'w')

# ------------------------------------------------------------------------------

for page in ods_data:
    uid = page.split()[1]
    print('uid:', uid)
    g = f.create_group(uid)
    pulses = [row[0] for row in ods_data[page][1:]]
    pulses = sorted(set(pulses))
    print('pulses:', len(pulses), '(%s ... %s)' % (pulses[0], pulses[-1]))
    for pulse in pulses:
        tomo, tomo_t = data.get_tomo(uid, pulse)
        bolo, bolo_t = data.get_bolo(pulse, tomo_t)
        h = g.create_group(str(pulse))
        h.create_dataset('bolo', data=bolo)
        h.create_dataset('bolo_t', data=bolo_t)
        h.create_dataset('tomo', data=tomo)
        h.create_dataset('tomo_t', data=tomo_t)
        print('-'*76)

# ------------------------------------------------------------------------------

f.close()
