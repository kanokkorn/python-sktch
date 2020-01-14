import torch
import torchvision
from torchvision import transforms
from PIL import Image


model = model.load_state_dict(torch.load('gochi-trained.pth'))
model.eval()
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
      mean=[0.485, 0.456, 0.406],
      std=[0.229, 0.224, 0.225])
    ])

def predict(path):
  img = Image.open(path)
  img_trans = transform(img)
  if torch.cuda.is_available():
    img_tensor = img_trans.view(1, 3, 224, 224).cuda
  else:
    img_tensor = img_trans.view(1, 3, 224, 224).cuda
  
  with torch.no_grad():
    out = model(img_tensor)
    pred = torch.exp(out)
    top_k, top_class = pred.top_k(1, dim=1)
    print('Output: ', idx_to_class[top_class.cpu().numpy()[0][0]])

if __name__ == '__main__':
  predict('../img/shyaro.jpg')

else:
  predict(path)
