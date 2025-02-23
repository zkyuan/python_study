import torch
from torch import tensor

# 梯度requires_grad，
x = torch.randn(5, 5)
y = torch.randn(5, 5)
z = torch.randn(5, 5)
z.requires_grad = True
a = x + y
print(a.requires_grad)
print(z.requires_grad)
print(z)
# tensor张量
# only Tensors of floating point and complex dtype can require gradients
c = tensor([
    [1., 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
c.requires_grad = True
print(type(c), type(z))
print(c)
