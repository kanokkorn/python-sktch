from __future__ import print_function
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

import cntk as C
import cntk.tests.test_utils
C.cntk_py.set_fixed_random_seed(1)

np.random.seed(0)

def generate_random_data_sample(sample_size, feature_dim, num_classes):
  Y = np.random.randint(size=(sample_size, 1), low=0, high=num_classes)
  X = (np.random.randn(sample_size, feature_dim)+3) * (Y+1)
  X = X.astype(np.float32)
  class_ind = [Y==class_number for class_number in range(num_classes)]
  Y = np.asarray(np.stack(class_ind), dtype=np.float32)
  return X, Y

mysamplesize = 32
features, labels = generate_random_data_sample(mysamplesize, input_dim, num_output_classes)

