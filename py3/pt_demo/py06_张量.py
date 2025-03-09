import numpy as np
import torch

print(torch.__version__, torch.cuda.is_available())

data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

x_ones = torch.ones_like(x_data)  # retains the properties of x_data
# print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)  # overrides the datatype of x_data
# print(f"Random Tensor: \n {x_rand} \n")

shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

# print(f"Random Tensor: \n {rand_tensor} \n")
# print(f"Ones Tensor: \n {ones_tensor} \n")
# print(f"Zeros Tensor: \n {zeros_tensor}")

tensor = torch.rand(3, 4)
# print(f"Shape of tensor: {tensor.shape}")
# print(f"Datatype of tensor: {tensor.dtype}")
# print(f"Device tensor is stored on: {tensor.device}")

# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = tensor.to('cuda')
    print(f"Device tensor is stored on: {tensor.device}")

tensor = torch.ones(4, 4)
"""
从0开始
[:,1] 表示第1列
[:1,1]，[1,1]表示第1行第1列
[1:,1]表示除第1行外的第1列
[1,]  表示第一行
"""
tensor[1, 1] = 0
# print(tensor)
tensor[1,] = 0
# print(tensor)

t1 = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
t2 = torch.tensor([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
t3 = torch.tensor([[3, 3, 3], [3, 3, 3], [3, 3, 3]])

# 张量连接 dim：-2 -1 0 1 张量矩阵拼在 下、右、下、右方向
t = torch.cat([t1, t2, t3], dim=1)
# print(t)

# 张量乘法
# print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
# print(f"tensor * tensor \n {tensor * tensor}")
# # 矩阵乘法
# print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
# print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

# 原地操作 带有 _ 后缀的操作是原地操作。例如：x.copy_(y), x.t_(), 将会更改 x。
# CPU 上的张量和 NumPy 数组可以共享它们的底层内存位置，更改其中一个将更改另一个。

# t = torch.ones(5)
# print(f"t: {t}")
# n = t.numpy()
# print(f"n: {n}")
# t.add_(1)
# print(f"t: {t}")
# print(f"n: {n}")

n = np.ones(5)
t = torch.from_numpy(n)

np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")