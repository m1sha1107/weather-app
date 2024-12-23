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
# sample = torch.tensor([[73., 67, 43], [91., 88, 64], [87., 134, 58], [102., 43, 37], [69, 96, 70]])
# soln = torch.tensor([56., 81., 119., 22., 103.], requires_grad=True)
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

model = nn.Linear(28*28, 10)
opt = optim.SGD(model.parameters(), lr=0.0001)

#im is not reshaped
def train(ims, labels, train=False):
    global model
    global opt
    sets = ims.reshape(100, 784)
    preds = model(sets)
    loss = f.cross_entropy(preds, labels)
    if train is False:
        return loss, len(ims)
    loss.backward()
    opt.step()
    opt.zero_grad()
    return loss, len(ims)

def evaluate(valloader, findacc=False):
    global model
    with torch.no_grad():
        result = (train(im, lens) for im, lens in valloader)
        losses, lens = zip(*result)
        total = np.sum(lens)
        avgloss = np.sum(np.multiply(losses, lens)).item() / total
        if findacc == True:
            for batch in valloader:
                datas = batch[0].reshape(100, 784)
                labels = batch[1]
                preds = model(datas)
                probs = f.softmax(preds, dim=1)
                _, num = torch.max(probs, dim=1)
                acc = accuracy(num, labels)
                break
            return avgloss, total, acc
        return avgloss, total

def trainer(epochs):
    global trainloader
    count, loss = 0, 0
    for i in range(0, epochs):
        for im, label in trainloader:
            loss, len = train(im, label, train=True)
#            count += 1
#            if count == 500:
#                break
        print(loss)

def tryout():
    global datasetim
    global dataset
    global model
    x = int(random.uniform(0, len(dataset)))
    im, _ = datasetim[x]
    datas, label = dataset[x]
    datavector = datas.reshape(1, 784)
    preds = model(datavector)
    probs = f.softmax(preds, dim=1)
    _, num = torch.max(probs, dim=1)
    print(num.item())
    plt.imshow(im, cmap='Greys')
    plt.show()

loss, total, accb = evaluate(valloader, findacc=True)
#x = input("no of epochs:")
trainer(15)
loss, total, acca = evaluate(valloader, findacc=True)
print("acc before: ")
print(accb)
print("acc after:")
print(acca)

root = tk.Tk()
test = tk.Button(root, text="test", padx=10, pady=10, command=lambda: tryout())
test.pack()
root.mainloop()
