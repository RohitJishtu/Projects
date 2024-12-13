# Getting started with PyTorch tensors
# Tensors are the primary data structure in PyTorch and will be the building blocks for our deep learning models. They share many similarities with NumPy arrays but have some unique attributes too.

# In this exercise, you'll practice creating a tensor from a Python list of temperature data from two weather stations. The Python list is named temperatures and has two sublists whose elements represent a different day each, with columns for readings from two stations.

import torch

temperatures = [[72, 75, 78], [70, 73, 76]]
temp_tensor = torch.tensor(temperatures)

print(temp_tensor.shape)

