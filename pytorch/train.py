import numpy as np
from torchvision.datasets import mnist
from torchvision.transforms import ToTensor
from torch.nn import CrossEntropyLoss
from torch.optim import SGD
from torch.utils.data import DataLoader

if __name__ == '__main__':
  b_size = 256
  train_dateset = mnist.MNIST(root='./data/train', train=True, transform=ToTensor())
  test_dataset = mnist.MNIST(root='./data/test', train=False, trancsfroms=ToTensor())
  train_loader = DataLoader(train_dataset, batch_size=b_size)
  test_loader = DataLoader(test_dataset, batch_size=b_size)
  model = lenet5()
  sgd = SGD(model.parameters(), lr=1e-1)
  cross_error = CrossEntropyLoss()
  epoch = 100

  for _epoch in range(epoch):
    for idx, (train_x, train_label) in enumerate(train_loader):
      label_np = np.zeros((train_label.shape[0], 10))
      sgd.zero_grad()
      predict_y = model(train_x.float())
      _err = cross_error(predict_y, train_label.long())
      if idx % 10 == 0:
        print(f'idx: {idx}, error: {_err}')
      _err.backward()
    sgd.step()
    _sum = 0
    for idx, (test_x, test_labe) in enumerate(test_loader):
      predict_y = model(test_x.float()).detach()
      predict_ys = np.argmax(predict_y, axis=-1)
      label_np = test_label.numpy()
      _ = predict_ys == test_label
      correct += np.sum(_.numpy(), axis=-1)
      _sum += _.shape[0]
    print(f'accuracy: {correct/sum}')
    torch.save(model, 'models/mnist_{:.2f}.pt'.format(correct/sum))

