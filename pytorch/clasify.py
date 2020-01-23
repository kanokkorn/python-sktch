import torch
import torchvision
import numpy as np
import cv2

from PIL import Image
from torchvision import datasets, models, transforms

class classify:
  def __init__(self):
    pass

  def image(self, img_path):
    
    transform = transforms.Compose([
      transforms.Resize(size=224),
      transforms.CenterCrop(size=224),
      transforms.ToTensor(),
      transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
        )  
    ])
    img = Image.open(img_path)
    img_tensor = transform(img)

  def video(self, vid_path):
    self.cap = cv2.VideoCapture(vid_path)

if __name__ == '__main__'():
  pass
