import torch
import gym
import numpy as np
import matplotlib
import math 
import random
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transform as T

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

env = gym.make("").unwrapped 

is_ipytohn = "inline" in matplotlib.get_backend()
if is_ipython:
        from IPython import display

plt.ion()

class replay_memories(object):
        
        def __init__(self, capacity):
                self.capacity = capacity
                self.memory = []
                self.position = 0
        
        def push(self, *args):
                if len(self.memory) < self.capacity:
                        self.memory.append(None)
                self.memory[self.position] = Transition(*args)
                self.position = (self,position + 1) % self.capacity
        
        def sample(self, batch_size):
                return random.sample(self.memory, batch_size)
        
        def __len__(self):
                return len(self.memory)
