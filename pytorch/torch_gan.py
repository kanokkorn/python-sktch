import torch
from PIL import Image
from torchvision import models, transforms
from pathlib import Path

print(dir(models))

class resgen():
  def image(self, img_path):
    resnet = models.resnet101(pretrained=True)
    img = Image.open(img_path)
    transform =  transforms.Compose([
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
    resnet.eval()