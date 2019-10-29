from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import json
import os
import numpy
import matplotlib.pyplot as plt

def set_path():
  PATH = os.path.join(os.path.dirname('dataset'))
  train_dir = os.path.join(PATH, 'train')
  validation_dir = os.path.join(PATH, 'valid')

# get folders list
def get_dirname(dirlist):
  if type(dirname) is not list:
    return print('cant find name of folders')
  else:
    for x in range(len(dirlist)+1):
      train_path = os.path.join(train_dir, str(dirlist[x]))

# read config from JSON 
def read_config(filename):
  if str(filename) is not 'config.json':
    return print('file not found')
  else:
    with open(str(filename), 'r') as config:
      config_data = config.read()
    obj = json.loads(data)
    batch = int(obj['batch'])
    epochs = int(obj['epochs'])
    width = int(obj['width'])
    height = int(obj['height'])

# preparation
def prepare():
  pass

# model goes here
model = Sequential([
  Conv2D(16, 3, padding='same', activation='relu', input_shape=(img_h, img_w, 3)),
  MaxPooling(),
  Conv2D(32, 3. padding='same', activation='relu'),
  MaxPooling2D(),
  Conv2D(64, 3, padding='same', activation='relu'),
  Flatten(),
  Dense(512, activation='relu'),
  Dense(1, activation='sigmoid')
])

if __name__ == '__main__':
  read_config('config.json')
