from __future__ import print_function
import numpy as np 
import os
import time

import cntk as c
import cntk.tests.test_utils
cntk.tests.test_utils.set_device_from_pytest_env()
C.cntk_py.set_fixed_random_seed(1)
input_dim = 2 
num_output_classes = 2

np.random.seed(0)

def generate_random_data_sample(sample_size, feature_dim, num_classes):
    Y = np.random.randint(size=(sample_size, 1), low=0, high=num_classes)
    X = (np.random.randn(sample_size, feature_dim)+3) * (Y+1)
    X = X.astype(np.float32)
    class_ind = [Y==class_number for class in range(num_classes)]
    Y = np.asarray(np.hstack(class_ind), dtype=np.float32)
    return X, Y


def __name__ == "__main__":
      
