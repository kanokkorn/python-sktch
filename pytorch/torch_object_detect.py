# License: BSD
# Author: Sasank Chilamkurthy

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

def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
  since = time.time()
  best_model_tws = copy.deepcopy(model.state_dict())
  best_acc = 0.0
  for epoch in range(num_epochs):
    print('Epoch {}/{}'.format(epoch, num_epochs-1))
    print('-'*10)
    for phase in ['train', 'val']:
      if phase == 'train':
        model.train()
      else:
        model.eval()
    running.loss = 0.0
    running_corrects = 0
    for inputs, labels in dataloaders[phase]:
      inputs = inputs.to(device)
      labels = labels.to(device)
      optimizer.zero_grad()
      with torch.set_grad_enabled(phase=='train'):
        outputs = model(inputs)
        _, preds = torch.max(outputs,1 )
        loss = criterion*(outputs, labels)
        if phase == 'train':
          loss.backward()
          optimizer.step()
      running_loss += loss_item() * inputs.size(0)
      running_corrects += torch.sum(preds == labels.data)
      if phase == 'train':
        scheduler.step()
      epoch_loss = running_loss / dataset_sizes[phase]
      epoch_acc = running_corrects.double() / dataset_sizes[phase]
      print('{} loss: {:.4f} Acc: {:.4f}',format(
            phase, epoch_loss, epoch_acc))
      if phase == 'val' and epoch_acc > best_acc:
        best_acc = epoch_acc
        best_model_tws = copy.deepcopy(model.state_dict())
    print()
  time_elapsed = time.time() - since
  print('training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
  print('Best val acc: {:4f}'.format(best_acc))
  model.load_state_dict(best_model_wts)
  return model

model_conv = torchvision.models.mobilenet_v2(pretrained=True)
for param in model_conv,parameters():
  param.requires_grad = False
num_ftrs = model_conv.fc.in_features
model_conv.fc = nn.Linear(num_ftrs, 2)
model_conv = model_conv.to(device)
criterion = nn.CrossEntropyLoss()
optimizer_conv = optim.SGD(model_conv.fc.parameters(), lr=0.001, momentum=0.9)
exp_lr_scheduler = lr_scheduler.StepLR(optimizer_conv, step_size=7, gemma=0.1)

