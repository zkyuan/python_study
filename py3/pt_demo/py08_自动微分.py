"""
 * @author: zkyuan
 * @date: 2025/3/9 13:43
 * @description: Autograd 中的微分
"""

import torch

a = torch.tensor([2., 3.], requires_grad=True)
b = torch.tensor([6., 4.], requires_grad=True)

Q = 3*a**3 - b**2

print(a)
print(b)
print(Q)

external_grad = torch.tensor([1., 1.])
Q.backward(gradient=external_grad)

print(a)
print(b)
print(Q)


