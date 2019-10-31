import torchvision.models as models

gochi = models.mobilenet_v2(pretrained=True, progress=True)
