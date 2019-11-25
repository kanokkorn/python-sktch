import torch
import torch.nn as nn
import torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
from pathlib import Path
import copy

data_transfrom = {
  'train': transfrom.Compose([
      transforms.RandomResizedCrop(224),
      transforms.RandomHorizontalFlip(),
      transforms.ToTensor(),
      transforms.normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
      )],
  'val': transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    )]
}

image_data = {x: datasets.ImageFolder(Path('./dl_data'), data_transfrom[x])
              for x in ['train', 'val']}

