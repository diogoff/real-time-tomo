# Towards real-time plasma tomography for JET

### Introduction

With a view towards real-time applications, this code computes tomographic reconstructions from bolometer data based on a simple matrix multiplication Y = X*W where:

    - X is a row vector of shape 1x56 containing the measurements collected from the 56 channels of the bolometer system.

    - Y is a row vector of shape 1x22540 containing the tomographic reconstruction corresponding to the measurements in X. The tomographic reconstruction has a resolution of 196x115 but here it is being represented in flattened form (196x115 = 22540).

    - W is a weight matrix of shape 56x22540 where each entry represents how much each measurement in X contributes to each pixel in Y. This weight matrix is trained on existing reconstructions, using gradient descent to minimize the mean absolute error between a true reconstruction Y and the result of X*W.

When the bolometer data has been collected at N different time points, then X becomes a matrix of shape Nx56, and Y becomes a matrix of shape Nx22540. However, W has still a shape of 56x22540 and the tomographic reconstructions for all time points in X can be calculated in one sweep by the matrix multiplication Y = X*W.

Numerical libraries, such as NumPy, implement matrix multiplication in vectorized form, using routines that can take advantage of multiple cores. For real-time applications, it will be important to use vectorized multiplication, which can be much faster than a naive implementation.

### Instructions

1. Run `python train_data.py` to gather the training data.

    - The training data consists in a subset of high-quality tomographic reconstructions that have been validated by the RO, and are therefore referred to as _reliable reconstructions_.
    
    - Together with the reconstructions, the script also gathers the corresponding bolometer data. Currently, these bolometer data come from the PPF system but it is expected that, in real-time, they will come from another source (e.g. JPF).
    
    - An output file `train_data.hdf` will be created with the bolometer and tomography data.

2. Run `python train_weights.py` to train the model.

    - This script requires TensorFlow and should be run on a GPU machine for better performance.

    - Precede the command with `CUDA_VISIBLE_DEVICES=0` to use a single GPU.

    - Precede the command with `TF_CPP_MIN_LOG_LEVEL=3` to suppress most of TensorFlow output.
 
    - An output file `weights.npy` will be created with the trained weights.
    
3. Run `python test_data.py 92213` to get the bolometer data for a test pulse.

    - Again, the bolometer data come from the PPF system but it is expected that, in real-time, they will come from another source (e.g. JPF).

    - The bolometer data will be appended to `test_data.hdf`. This file will be created if it does not exist.

4. Run `python test_weights.py` to generate the reconstructions from the bolometer data.

    - This script will go through every pulse in `test_data.hdf` and multiply the bolometer data by the weights in order to generate the corresponding reconstructions.

    - The results will be appended to `test_data.hdf`.

5. Run `python test_plot.py 92213 46.40 54.39 0.01` to plot the reconstructions for the test pulse, between t=46.40s and t=54.39s with a time step of 0.01s.

    - This script will read the tomographic reconstructions from `test_data.hdf` and reshape them into 196x115 for display.

