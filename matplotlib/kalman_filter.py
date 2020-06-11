import math
import random
from matplotlib import pyplot

est_err, mea, minus_est_err, mea_err = 0

gain = lambda est_err, mea_err: est_err/(mea_err+est_err) 

est = lambda minus_est, mea, gain: (minus_est+gain)*(mea-minus_est) 

est_err = lambda gain, minus_est_err: (1-gain)*minus_est_err 