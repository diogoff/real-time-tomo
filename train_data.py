from __future__ import print_function

import data
import h5py
import numpy as np

# ----------------------------------------------------------------------

fname = '/home/pcarval/kb/interp_tables/tomography_completed.reliable.ods'
print('Reading:', fname)
ods_data = pyexcel_ods.get_data(fname)

pulses = []
for page in ods_data:
    pulses += [row[0] for row in ods_data[page][1:]]

pulses = sorted(set(pulses))
print('pulses:', len(pulses))

# ----------------------------------------------------------------------

fname = 'train_data.hdf'
print('Writing:', fname)
f = h5py.File(fname, 'w')

for pulse in pulses:
    tomo, tomo_t = data.get_tomo(pulse)
    if len(tomo) > 0:
        bolo, bolo_t = data.get_bolo(pulse, tomo_t)
        g = f.create_group(str(pulse))
        g.create_dataset('bolo', data=bolo)
        g.create_dataset('bolo_t', data=bolo_t)
        g.create_dataset('tomo', data=tomo)
        g.create_dataset('tomo_t', data=tomo_t)
        print('-'*76)

f.close()
