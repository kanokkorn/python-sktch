# run and compare to numpy_warmup to see the different
import torch

dtype = torch.float
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
# N = batch size, D_in = input dimension
# H = hidden dimension, D_out = output dimension
N, D_in, H, D_out = 64, 1000, 100, 10

# random input and output
x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.randn(N, D_out, device=device, dtype=dtype)

# random weight
w1 = torch.randn(D_in, H, device=device, dtype=dtype)
w2 = torch.randn(H, D_out, device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(5000):
  # forward pass
  h = x.mm(w1)
  h_relu = h.clamp(min=0)
  y_pred = h_relu.mm(w2)

  # compute loss
  loss = (y_pred-y).pow(2).sum().item()
  if t % 100 == 99:
    print(t, loss)

  # Backprop to compute gradients of w1 and w2
  grad_y_pred = 2.0*(y_pred-y) 
  grad_w2 = h_relu.t().mm(grad_y_pred)
  grad_h_relu = grad_y_pred.mm(w2.t())
  grad_h = grad_h_relu.clone()
  grad_h[h<0] = 0
  grad_w1 = x.t().mm(grad_h)

  w1 -= learning_rate * grad_w1
  w2 -= learning_rate * grad_w2
