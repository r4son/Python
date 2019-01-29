#! /usr/local/bin/python3
#RECURRENT NEURAL NETWORK

"""
Training data not included!
This RNN takes names of a list in a given language and removes the unicode encoding and turns it into UTF-8
It is also able to tell you the origin of the name if trained enough.
Best to train it completely randomly.
[CODE NOT COMPLETED]
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
import unicodedata
import string


def toAscii(s):
    return ''.join(
        char for char in unicodedata.normalize('NFD', s)
        if unicodedata.category(char) != 'Mn'
        and char in string.ascii_letters + ".,:'"
    )

def lines(data):
    f = open(data, encoding='utf-8').read().strip().split('\n')
    return [toAscii(l) for l in f]


data = {}
for f in listdir('CharacterRNNs/data/names/'):
    lang = f.split('.')[0]
    ls = lines('CharacterRNNs/data/names/' + f)
    data[lang] = ls

print(data['German'])
