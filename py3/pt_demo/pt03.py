"""
 * @author: zkyuan
 * @date: 2025/2/19 21:15
 * @description: Tensor
"""
import torch

x1 = torch.ones(3, 3)
print(x1)

x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x + 2
print(y)

z = y * y * 3
print(z)

out = z.mean()
print(out)
