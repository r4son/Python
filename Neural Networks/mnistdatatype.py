#! /usr/local/bin/python3

"""
This Neural Network is analyzing MNIST Data Types. Handwriting in different shapes and forms.
See the MNIST_Data_Example link in the class to see an example.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torch.autograd as Variable
import torch.nn.functional as F
import numpy as np
import matplotlib
from torchvision import datasets, transforms


kwargs = {}
train_data = torch.utils.data.DataLoader(datasets.MNIST("data", train=True, download=True, transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,),(0.3081,))])),batch_size=64, shuffle=True, **kwargs)

test_data = torch.utils.data.DataLoader(datasets.MNIST("data", train=False, download=False, transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,),(0.3081,))])),batch_size=64, shuffle=True, **kwargs)


class neuralNetwork(nn.Module):
    
    MNIST_Data_Example = "https://en.wikipedia.org/wiki/MNIST_database#/media/File:MnistExamples.png"
    
    def __init__(self):
        super(neuralNetwork, self).__init__()
        self.conv1 = nn.Conv2d(1, 10,kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5) 
        self.conv_dropout = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 60) #* 20x4x4 = 320 // 20 Pictures multiplied by 4 multiplied by 4 Pixel
        self.fc2 = nn.Linear(60, 10)


    def forward(self, x):
        x = self.conv1(x)
        x = F.max_pool2d(x, 2)
        x = F.relu(x) #! REctified Linear Unit
        x = self.conv2(x)
        x = self.conv_dropout(x)
        x = F.max_pool2d(x, 2)
        x = F.relu(x)
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x)


model = neuralNetwork()
#* model.cuda()

optimizer = optim.SGD(model.parameters(), lr= 0.10, momentum=0.8)


def train(epoch):
    model.train() # Train
    #model.eval() # evaluate
    for batch_id, (data, target) in enumerate(train_data):
        #data = data.cuda() #data --> GPU
        #target = target.cuda() #target --> GPU
        #data = Variable(data) #data --> GPU
        #target = Variable(target) #target --> GPU
        optimizer.zero_grad()
        out = model(data)
        criterion = F.nll_loss
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
        print("Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}".format(epoch, batch_id * len(data), len(train_data.dataset), 100. * batch_id / len(train_data), loss.data[0]))


def test():
    model.eval()
    loss = 0
    correct = 0
    for data, target in test_data:
        #data = Variable(data.cuda(), volatile=True)
        #target = Variable(target.cuda())
        out = model(data)
        loss += F.nll_loss(out, target, size_average=False).data[0] #Negative Loglikelyhood Loss
        #print(out.data)
        prediction = out.data.max(1, keepdim=True)[1]
        correct += prediction.eq(target.data.view_as(prediction)).cpu().sum()
    loss = loss / len(test_data.dataset)
    print("Average loss: ", loss)
    print("Accuracy: ", 100. * correct / len(test_data.dataset))


for epoch in range (1, 3):
    train(epoch)
    test()
