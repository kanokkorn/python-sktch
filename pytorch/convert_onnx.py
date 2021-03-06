import argparse
import torch
import torchvision
from torchvision import models

def convert_onnx(path):
  model = torch.load(path)
  model.load_state_dict(model)
  input_names = ['actual_input_1']+['learned_%d' % i for i in range(16)]
  if torch.cuda.is_available():
    mock_input  = torch.rand(10, 3, 224, 224, device='cuda')
  else:
    mock_input  = torch.rand(10, 3, 224, 224, device='cpu')
  output_names = ['output']
  torch.onnx.export(
      model, mock_input,'output.onnx', 
      verbose=True, 
      input_names=input_names,
      output_names=output_names
      )

if __name__ == '__main__':
  arg = argparse.ArgumentParser(
      description = 'Convert Pytorch model to ONNX format'
      )
  arg.add_argument(
      '-i',
      '--input',
      required = True,
      help = 'Path to model file, the output will be the same place as the script'
      )
  args = vars(arg.parse_args())
  convert_onnx(args['input'])

