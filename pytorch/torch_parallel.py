import torch
from typing import List

def foo(x):
  return torch.neg(x)

@torch.jit.script
def example(x):
  futures = [torch.jit.fork(foo, x) for _ in range(100)]
  results = [torch.jit.wait(future) for future in futures]
  return torch.sum(torch.stack(results))

print(example(torch.ones([])))