import torch
import torch.nn as nn
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
# trying pathlib
# from pathlib import Path 
import copy

data_transfrom = {
  'train': transforms.Compose([
      transforms.RandomResizedCrop(224),
      transforms.RandomHorizontalFlip(),
      transforms.ToTensor(),
      transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
      ]),
  'val': transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    ])
}
print(Path('./dl_data'))
# trying pathlib 
#image_data = {x: datasets.ImageFolder(Path('./dl_data'), data_transfrom[x])
#              for x in ['train', 'val']}

data_dir = 'data/dl_data'

image_data = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transfrom[x])
              for x in ['train', 'val']}
data_loader = {x: torch.utils.data.DataLoader(image_datap[x], batch_size=4, shuffle=True, num_workers=4)
              for x in ['train', 'val']}
data_size = {x: len(image_data[x]) for x in ['train', 'val']}
classes = image_data['train'].classes

device = torch.device('cuda:0' fi torch.cuda.is_available() else 'cpu')

def img_show():
  inp = imp.numpy().transpose((1, 2, 0))
  mean = np.array([0.485, 0.456, 0.406])
  std = np.array
