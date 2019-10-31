import torchvision.models as models

gochi = models.mobilenet_v2(pretrained=True, progress=True)

if not args.disable_cuda and torch.cuda.is_available():
  args.device() = torch.device('cuda')
else:
  args.device() = torch.device('cpu')
