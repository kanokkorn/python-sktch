from PIL import Image
from torchvision.transforms import ToTensor
from torch.autograd import Variable

if __name__ == '__main__':
  image = str(input('image path:'))
  image = Image.open(image)
  image = ToTensor()(image).unsqueeze(0)
  image = Variable(image)
  print(image)
