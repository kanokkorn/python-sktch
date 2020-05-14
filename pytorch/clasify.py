import torch
import torchvision
from torchvision.transforms import ToTensor
from torch.autograd import Variable
import numpy as np

from PIL import Image
from torchvision import datasets, models, transforms

class classify:
  def image(self, img_path):
    img = Image.open(str(img_path))
    transform = transforms.Compose([
      transforms.Resize(size=224),
      transforms.CenterCrop(size=224),
      transforms.ToTensor(),
      transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
        )  
    ])
    img_tensor = transform(img)

if __name__ == '__main__':
  detect = classify()
  detect.image('../img/shyaro.jpg')

