# From https://phyblas.hinaboshi.com/tomoshibi14

import numpy as np
import matplotlib.pyplot as plt
import torch
import time

dev = torch.device('cuda')

relu = torch.nn.ReLU()
ha_entropy = torch.nn.CrossEntropyLoss()

khrongkhai = torch.nn.Sequential(
    torch.nn.Linear(2,64),
    relu,
    torch.nn.Linear(64,5))
khrongkhai.to(dev)


x = np.random.uniform(0,12,20000)
y = np.random.uniform(0,4,20000)
X = np.array([x,y]).T
z = (y+np.sin(x)).astype(int)
plt.scatter(x,y,c=z,edgecolor='k',cmap='rainbow',alpha=0.05)
plt.figure()

opt = torch.optim.Adam(khrongkhai.parameters(),lr=0.002)
lis_khanaen = []
X = torch.Tensor(X).to(dev)
z = torch.LongTensor(z).to(dev)
t_roem = time.time()
for o in range(10000):
    a = khrongkhai(X)
    J = ha_entropy(a,z)
    J.backward()
    opt.step()
    opt.zero_grad()
    khanaen = (a.argmax(1)==z).cpu().numpy().mean()
    lis_khanaen.append(khanaen)
    if(o%500==499):
        print('%d ครั้งผ่านไป ใช้เวลาไป %.1f วินาที ทำนายแม่น %.4f'%(o+1,time.time()-t_roem,khanaen))

plt.plot(lis_khanaen)
plt.show()