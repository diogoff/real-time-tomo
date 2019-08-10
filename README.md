# Towards real-time tomography for JET

1. Run `python tomo_data.py` to gather the training data.

    - This script will only run on the JET computing cluster (e.g. Freia).

    - The training data consists in the bolometry + tomography data for reliable reconstructions.
    
    - An output file `tomo_data.hdf` will be created.

2. Run `python model_train.py` to train the model.
