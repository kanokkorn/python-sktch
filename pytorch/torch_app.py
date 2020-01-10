import torch
import torchvision
from torchvision import transforms
from PIL import Image

def predict(path):
  img = Image.open(path)
  transforms = transforms.Compose([
      transforms.Resize(256),
      transforms.CenterCrop(224),
      transforms.ToTensor(),
      transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])
      ])
  model = model.load_state_dict(torch.load('gochi-trained.pth'))
  model.eval()
  img_trans = transforms(img)
  batch_trans = torch.unsqueeze(img_trans, 0)
  out = model(batch_trans)
  

if __name__ == '__main__':
  predict('../img/shyaro.jpg')

else:
  predict(path)
