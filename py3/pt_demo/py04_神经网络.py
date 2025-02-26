"""
 * @author: zkyuan
 * @date: 2025/2/19 22:03
 * @description: 神经网络工具箱torch.nn
"""

"""
torch.autograd库虽然实现了自动求导与梯度反向传播，但如果我们要完成一个模型的训练，仍需要手写参数的自动更新、训练过程的控制等，还是不够便利。
为此，PyTorch进一步提供了集成度更高的模块化接口torch.nn，该接口构建于Autograd之上，提供了网络模组、优化器和初始化策略等一系列功能。

nn.Module是PyTorch提供的神经网络类，并在类中实现了网络各层的定义及前向计算与反向传播机制。
在实际使用时，如果想要实现某个神经网络，只需继承nn.Module，在初始化中定义模型结构与参数，在函数forward()中编写网络前向过程即可。
"""
# 1．nn.Parameter函数

# 2．forward()函数与反向传播

# 3．多个Module的嵌套

# 4．nn.Module与nn.functional库

# 5．nn.Sequential()模块


from torch import nn


class MLP(nn.Module):
    """neural network modules，这里用torch.nn实现一个多层感知机MLP（Multilayer Perceptron）"""

    def __init__(self, in_dim, hid_dim1, hid_dim2, out_dim):
        super(MLP, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(in_dim, hid_dim1),
            nn.ReLU(),
            nn.Linear(hid_dim1, hid_dim2),
            nn.ReLU(),
            nn.Linear(hid_dim2, out_dim),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.layer(x)
        return x


import torch

batch_n = 100  # 一个批次输入数据的数量
hidden_layer = 100
input_data = 1000  # 每个数据的特征为1000
output_data = 10

x = torch.randn(batch_n, input_data)
y = torch.randn(batch_n, output_data)

w1 = torch.randn(input_data, hidden_layer)
w2 = torch.randn(hidden_layer, output_data)
print(x)
print(y)
print(w1)
print(w2)
print("---------------------------")
epoch_n = 20
lr = 1e-6

for epoch in range(epoch_n):
    h1 = x.mm(w1)  # (100,1000)*(1000,100)-->100*100
    print(h1.shape)
    h1 = h1.clamp(min=0)
    y_pred = h1.mm(w2)

    loss = (y_pred - y).pow(2).sum()
    print("epoch:{},loss:{:.4f}".format(epoch, loss))

    grad_y_pred = 2 * (y_pred - y)
    grad_w2 = h1.t().mm(grad_y_pred)

    grad_h = grad_y_pred.clone()
    grad_h = grad_h.mm(w2.t())
    grad_h.clamp_(min=0)  # 将小于0的值全部赋值为0，相当于sigmoid
    grad_w1 = x.t().mm(grad_h)

    w1 = w1 - lr * grad_w1
    w2 = w2 - lr * grad_w2

print("---------------------------")
print(x)
print(y)
print(w1)
print(w2)
