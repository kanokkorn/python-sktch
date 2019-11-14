from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from troch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision imoprt datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy

data_transfroms = {
  'train': transforms.Compose([
      transforms.RandomResizeCrop(224),
      transforms.RandomHorizontalFlip(),
      transforms.ToTensor(),
      transforms.Normalize([0.485,0.485, 0.406], [0.229, 0.224, 0.225])
      ]),
  'val': transforms.Compose([
      transforms.Resize(256),
      transforms.CenterCrop(244),
      transforms.ToTensor(),
      transforms.Normalize([0.485,0.485, 0.406], [0.229, 0.224, 0.225])
      ]),
}

data_dir = 'data/anime'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transfroms[x])
    for x in ['train', 'val']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4, shuffle=True, num_workers=4)
    for x in ['train', 'val']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
class_names = image_datasets['train'].classes

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

def imshow(inp, title=None):
  inp = inp.numpy().transpose((1, 2, 0))
  mean = np.array([0.485,0.485, 0.406])
  std = np.array([0.229, 0.224, 0.225])
  inp = std * inp + mean
  inp = np.clip(inp, 0, 1)

inputs, classes = next(iter(dataloaders['train']))
out = torchvision.utils.make_grid(inputs)
