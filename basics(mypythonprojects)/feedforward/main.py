import torch
from torch import nn
import torchvision
from torchvision.datasets import MNIST
import torch.utils.data as u
from torch.utils.data import dataloader as d
import numpy as np
import torch.nn.functional as f
import torch.optim.sgd as optim
import random
import matplotlib.pyplot as plt
import tkinter as tk
import time
# sample = torch.tensor([[73., 67, 43], [91., 88, 64], [87., 134, 58], [102., 43, 37], [69, 96, 70]])
# soln = torch.tensor([56., 81., 119., 22., 103.], requires_grad=True)
start = time.perf_counter()
dataset = MNIST(root='dataset', download=True, transform=torchvision.transforms.ToTensor())
datasetim = MNIST(root='datasetim', download=True)

def indices(n, valpct):
    valsize = int(n * valpct)
    indice = np.random.permutation(n)
    return indice[:valsize], indice[valsize:]

def accuracy(preds, labels):
    x = preds == labels
    return torch.sum(x, dtype=torch.float16).item() / len(x)
# returns valind, trainind

valind, trainind = indices(len(dataset), 0.2)

trainsampler = u.sampler.SubsetRandomSampler(trainind)
trainloader = d.DataLoader(dataset, 100, sampler=trainsampler)

valsampler = u.sampler.SubsetRandomSampler(valind)
valloader = d.DataLoader(dataset, 100, sampler=valsampler)

class Model(nn.Module):
    def __init__(self, insize, hiddensize, outsize):
        super().__init__()
        self.linear1 = nn.Linear(insize, hiddensize).cuda()
        self.linear2 = nn.Linear(hiddensize, hiddensize).cuda()
        self.linear3 = nn.Linear(hiddensize, outsize).cuda()

    def predict(self, raw):
        inp = raw.view(raw.size(0), 784)
        hid1 = self.linear1(inp)
        hid1 = f.relu(hid1)
        hid2 = self.linear2(hid1)
        hid2 = f.relu(hid2)
        out = self.linear3(hid2)
        return out

def move(tens):
#    tens[1] = torch.tensor(tens[1])
#    return  tens[0].to('cuda', non_blocking=True), tens[1].to('cuda', non_blocking=True)
    if isinstance(tens, (list, tuple)):
        return [move(x) for x in tens]
    return tens.to('cuda', non_blocking=True)

class deviceloader():
    def __init__(self, device, dl):
        self.device = device
        self.dl = dl

    def __iter__(self):
        for i in self.dl:
            yield move(i)

    def __len__(self):
        return len(self.dl)
trainloader = deviceloader('cuda', trainloader)
valloader = deviceloader('cuda', valloader)

model = Model(insize=784, hiddensize=32, outsize=10)

for im, label in trainloader:
    print(im.device)
    print(label.device)
    break

for im, label in valloader:
    print(im.device)
    break

opt = optim.SGD(model.parameters(), lr=0.1)

#im is not reshaped
def train(ims, labels, opt, train=False):
    global model
#    sets = ims.reshape(100, 784)
    preds = model.predict(ims)
    loss = f.cross_entropy(preds, labels)
    if train is False:
        return loss, len(ims)
    loss.backward()
    opt.step()
    opt.zero_grad()
    return loss, len(ims)

def trainer(epochs):
#    count, loss = 0, 0
    for i in range(0, epochs):
        for im, label in trainloader:
            loss, len = train(im, label, opt, train=True)
#            count += 1
#            if count == 500:
#                break
        print(loss)

def smarttrainer(opt, lim=1e-7):
    tracklist = [0, 0, 0, 0]
    run = True
    i = 1
    lr = 0.1
    while run is True:
        for im, label in trainloader:
            loss, len = train(im, label, opt, train=True)
        tracklist[(i % 4) - 1] = loss.item()
        i += 1
        if tracklist[0] < tracklist[1] and tracklist[1] < tracklist[2] and tracklist[2] < tracklist[3]:
            if lr <= 1e-7: # does not iter on limit itself
                run = False
                break
            lr = lr / 100
            opt = optim.SGD(model.parameters(), lr=lr)
            tracklist = [0, 0, 0, 0]
            print("lr to " + str(lr))
        if loss <= 0.0001:
            break
        print(loss)
    print("finished training")
    print("epochs:" + str(i - 1))

def evaluate(valloader, findacc=False):
    with torch.no_grad():
        result = (train(im, lens, opt=opt) for im, lens in valloader)
        losses, lens = zip(*result)
        losses = torch.tensor(losses)
        lens = torch.tensor(lens)
        losses = losses.numpy()
        lens = lens.numpy()
#        losses = move(losses)
#        lens = move(losses)
        total = np.sum(lens)
        avgloss = np.sum(np.multiply(losses, lens)) / total
        if findacc == True:
            for batch in valloader:
                datas = batch[0].reshape(100, 784)
                labels = batch[1]
                preds = model.predict(datas)
                probs = f.softmax(preds, dim=1)
                _, num = torch.max(probs, dim=1)
                acc = accuracy(num, labels)
                break
            return avgloss, total, acc
        return avgloss, total

def tryout():
    x = int(random.uniform(0, len(dataset)))
    im, _ = datasetim[x]
    datas, label = dataset[x]
    datavector = datas.reshape(1, 784)
    datavector = move(datavector)
    preds = model.predict(datavector)
    probs = f.softmax(preds, dim=1)
    _, num = torch.max(probs, dim=1)
    print(num.item())
    plt.imshow(im, cmap='Greys')
    plt.show()

loss, total, accb = evaluate(valloader, findacc=True)
#smarttrainer(opt, lim=1e-7)
trainer(15)
loss, total, acca = evaluate(valloader, findacc=True)
end = time.perf_counter()
delay = end - start
print("time taken: " + str(delay))
print("acc before: ")
print(accb)
print("acc after:")
print(acca)

root = tk.Tk()
test = tk.Button(root, text="test", padx=10, pady=10, command=lambda: tryout())
test.pack()
root.mainloop()
