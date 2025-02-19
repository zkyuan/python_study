"""
 * @author: zkyuan
 * @date: 2025/2/19 17:12
 * @description: pytorch
"""
# 安装模块：pip install torch
# 安装模块：pip install numpy
# from  __future__ import print_function
import torch

# 创建没有初始化的矩阵
# x = torch.empty(5, 3)
# print(x)

# 创建一个初始化的矩阵
x = torch.rand(5, 3)
print(x)

# 创建一个全零的矩阵并指定数据元素的类型
y = torch.zeros(5, 3, dtype=torch.long)
print(y)

# 直接通过数据来创建张量
z = torch.tensor([2.5, 3.5])
print(z)

# 通过已有的张量，创建相同尺寸的新张量
a = x.new_ones(5, 3, dtype=torch.double)
print(a)

# 利用randn_like方法来得到相同尺寸的张量，并且采用随机初始化的方法为其赋值
b = torch.randn_like(a, dtype=torch.float)
print(b)

print("a:", a.size(), ",b:", b.size())  # 都是5行3列

# 元组类型接收矩阵行列
m, n = a.size()
print("行：", m, "，列：", n)
