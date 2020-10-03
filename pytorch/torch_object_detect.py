import torch
from pathlib import Path
from PIL import Image
from torchvision import models, transforms
from torchvision.models.mobilenet import mobilenet_v2

class object_detect:
  def image(self, image_path):
    mobilenet = models.mobilenet_v2(pretrained=True)
    img = Image.open(image_path)
    transform = transforms.Compose([
      # resize image to fit a tensor
      transforms.Resize(size=224),
      transforms.CenterCrop(size=224),
      transforms.ToTensor(),
      # normalize image, this is standard value
      transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
        )  
    ])
    img_tensor = transform(img)
    batch_trans = torch.unsqueeze(img_tensor, 0)
    mobilenet.eval()
    output = mobilenet(batch_trans)
if __name__ == '__main__':
  objects = object_detect()
  objects.image('image path')