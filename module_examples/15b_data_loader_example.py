# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:10:27 2022

@author: taylo
"""
import os

cwd = os.getcwd()


with open('data_to_read/data1.txt') as f:
    lines = f.readlines()
    

import numpy as np

data_list = []
path = '/data_to_read/'
for file in os.listdir(cwd+path):
    data = np.loadtxt(cwd+path+file)
    data_list.append(data)

data1 = data_list[0]
modified_data1 = data1*86
