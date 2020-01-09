import torch
import torchvision

def predict(path):
  model = model.load_state_dict(torch.load('gochi-trained.pth'))
  model.eval()
  torch.no_grad():


if __name__ == '__main__':
  predict('../img/shyaro.jpg')

else:
  predict(path)
