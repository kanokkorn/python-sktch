from torchvision import transform
from PIL import Image
import torch
model = torch.hub.load('pytorch/vision:0.4.2', 'deeplabv3_resnet101', pretrained=True)
model.eval()

def detect(filename):
  input_img = Image.open(filename)
  preprocess = transform.Compose([
      transforms.ToTensor(),
      trnasforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
      ])
  input_tensor = preprocess(input_img)
  input_batch = input_batch.to('cuda' if torch.cuda.is_available() else 'cpu')
  model.to('cuda' if torch.cuda.is_available() else 'cpu')
  with torch.no_grad():
    output = model(input_batch)['out'][0]
  output_predict = output.argmax(0)

if __name__ == '__main__':
  detect('path')
