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

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

def img_show():
  inp = imp.numpy().transpose((1, 2, 0))
  mean = np.array([0.485, 0.456, 0.406])
  std = np.array([0.5, 0.5, 0.5])
  inp = std * inp + mean
  inp = np.clip(inp, 0, 1)
  if title is not None:
    plt.title(title)
  inputs, classes = next(iter(DataLoader['train']))
  out = torchvision.uitls.make_grid(inputs)

def train(model, criterion, optimizer, scheduler, num_epoches=50):
  start_time = time.time()
  model_wts = copy.deepcopy(model.state_dict())
  acc = 0.0
  for epoch in range(num_epoches):
    if phase == 'train':
      model.train()
    else:
      model.eval()
    loss = 0.0
    correct = 0.0
    for inputs, labels in DataLoader[phase]:
      inputs = inputs.to(device)
      labels = labels.to(device)
      optimizer.zero_grad()
      with torch.get_grad_enabled(phase == 'train'):
        outputs = model(inputs)
        _, preds = torch.max(outputs, 1)
        loss2 = criterion(outputs, labels)
        if phase == 'train':
          loss2.backward()
          optimizer.step()
        loss += loss2.item() * inputs.size(0)
        corrent = torch.sum(preds == labels.data)
    if phase == 'train':
      scheduler.step()
    epoch_loss = loss / data_size[phase]
    epoch_acc = correct.double() /data_size[phase]
    print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))
    if phase == 'val' and epoch_acc > acc:
      acc = epoch_acc
      model_wts = copy.deepcopy(model.state_dict())
    print()
  elapsed = time.time() - start_time
  print('Train completed in : {.4f}s'.format(elapsed // 60 , elapsed % 60))
  print('best val acc: {.4f}'.format(acc))
  model.load.state_dict(model_wts)
  return model

# Finetuning 
model_ft = models.resnet18(pretrained=True)
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 2)
model_ft = model_ft.to(device)
criterion = nn.CorssEntropyLoss()
optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)
exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)
model_ft = train(model_ft, criterion, optimizer_ft, exp_lr_scheduler, num_epoches=50)
