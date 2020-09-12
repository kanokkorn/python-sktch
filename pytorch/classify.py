import torch
import torchvision
from torchvision.transforms import ToTensor
from torch.autograd import Variable
import numpy as np

from PIL import Image
from torchvision import datasets, models, transforms

class classify:
  def image(self, img_path):
    mobilenet = models.mobilenet_v2(pretrained=True)
    img = Image.open(img_path)
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
    batch_trans = torch.unsqueeze(img_tensor, 0)
    mobilenet.eval()
    output = mobilenet(batch_trans)
    with open('./imagenet-classes.txt') as f:
      labels = [line.strip() for line in f.readlines()]
    _, idx = torch.max(output, 1)
    percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100
    print(labels[idx[0]], percentage[idx[0]].item())

if __name__ == '__main__':
  detect = classify()
  detect.image('../img/shyaro.jpg')