#! /usr/local/bin/python3

"""
Training data not included!!!

This Neural Network recognizes animals, at the time cats and dogs.
"""

import torch
import torchvision
from torchvision import transforms
from PIL import Image
import torch.nn as nn
import torch.optim as optim
import torch.autograd as Variable
import torch.nn.functional as F
import numpy as np
from os import listdir
import random


normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225] 
)


transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(256),
    transforms.ToTensor(),
    normalize
])


#! TARGET: [isCat, isDog]
train_data_list = []
target_list = []
train_data = []
files = listdir('train_data_ani/train/')

for i in range(len(listdir('train_data_ani/train/'))):
    f = random.choice(files)
    files.remove(f)
    img = Image.open('train_data_ani/train/' + f)
    img_tensor = transform(img)
    #img_tensor.unsqueeze_(0) #(1, 3, 256, 256)
    #print(img_tensor)
    train_data_list.append(img_tensor)
    isCat = 1 if 'cat' in f else 0 #* 1 Cat
    isDog = 1 if 'dog' in f else 0 #* 0 Dog
    target = [isCat, isDog]
    target_list.append(target)
    if len(train_data_list) >= 64:
        train_data.append((torch.stack(train_data_list), target_list))
        train_data_list = []
        break

print(train_data)

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, kernel_size=5)
        self.conv2 = nn.Conv2d(6, 12, kernel_size = 5)
        self.conv3 = nn.Conv2d(12, 18, kernel_size=5)
        self.fc1 = nn.Linear(14112, 1000)
        self.fc2 = nn.Linear(1000, 2)

    def forward(self, x):
        x = self.conv1
        #x = torch.Tensor(x)
        F.max_pool2d(x, 2)
        x = F.relu(x)
        x = self.conv2
        #x = torch.Tensor(x)
        F.max_pool2d(x, 2)
        x = F.relu(x)
        x = self.conv3
        #x = torch.Tensor(x) 
        F.max_pool2d(x, 2)
        x = F.relu(x)
        x = x.view(-1, 14112)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.softmax(x)
    
model = Network()

optimizer = optim.Adam(model.parameters(), lr=0.01)

def train(epoch):
    model.train()
    batch_id = 0
    for data, target in train_data:
        #data = data.cuda()
        target = torch.Tensor(target).cuda()
        target = torch.Tensor(target)
        #data = Variable(data)
        #target = Variable(target)
        optimizer.zero_grad()
        out = model(data)
        criterion = F.binary_cross_entropy
        loss = criterion(out, target)
        loss.backward()
        optimizer.step()
        print("Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}".format(epoch, batch_id, * len(data), len(train_data), 100. * batch_id / len(train_data),loss.data[0]))
        batch_id = batch_id + 1

for epoch in range(1, 10):
    train(epoch)
