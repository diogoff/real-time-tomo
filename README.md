# Towards real-time plasma tomography for JET

1. Run `python train_data.py` to gather the training data.

    - The training data consists in a subset of high-quality tomographic reconstructions that have been validated by the RO, and are therefore referred to as _reliable reconstructions_.
    
    - Together with the reconstructions, the script also gathers the corresponding bolometer data. Currently, these bolometer data come from the PPF system but it is expected that, in real-time, they will come from another source (e.g. JPF).
    
    - An output file `train_data.hdf` will be created with the bolometer and tomography data.

2. Run `python train_weights.py` to train the model.

    - This script requires TensorFlow and should be run on a GPU machine for better performance.
    
    - An output file `train_weights.npy` is created with the trained weights.
    
3. Run `python test_data.py 92213` to get the bolometer data for a test pulse.

    - Again, the bolometer data come from the PPF system but it is expected that, in real-time, they will come from another source (e.g. JPF).

    - An output file `test_data.hdf` will be created with the bolometer data.

4. Run `python test_weights.py`
