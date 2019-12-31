import torch
import torchvision


dummy_input = torch.randn(10, 3, 224, 224, device='cpu')
model = torchvision.models.alexnet(pretrained=True)

input_names = ['actual_input_1']+['learned_%d' % i for i in range(16)]
output_names = ['output_1']
torch.onnx.export(model, dummy_input, 'alexnet.onnx', verbose=True, input_names=input_names, output_names=output_names)
