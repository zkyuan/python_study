"""
 * @author: zkyuan
 * @date: 2025/3/9 13:19
 * @description: torch.autograd 简易入门  ， PyTorch 的自动微分引擎
"""
"""
神经网络 (NN) 是嵌套函数的集合，这些函数在某些输入数据上执行。这些函数由参数（包括权重和偏差）定义，这些参数在 PyTorch 中存储在张量中。

NN 的训练分两步进行

前向传播：在前向传播中，NN 对正确的输出做出最佳猜测。它通过其每个函数运行输入数据以做出此猜测。

反向传播：在反向传播中，NN 根据其猜测中的错误按比例调整其参数。
        它通过从输出向后遍历，收集误差相对于函数参数的导数（梯度），并使用梯度下降优化参数来实现这一点。
"""
import torch
from torchvision.models import resnet18, ResNet18_Weights

# 从 torchvision 加载预训练的 resnet18 模型：Deep Residual Learning for Image Recognition <https://arxiv.org/abs/1512.03385>
# Downloading: "https://download.pytorch.org/models/resnet18-f37072fd.pth" to C:\Users\HP/.cache\torch\hub\checkpoints\resnet18-f37072fd.pth
model = resnet18(weights=ResNet18_Weights.DEFAULT)

# 创建一个随机数据张量来表示具有 3 个通道、高度和宽度为 64 的单个图像
data = torch.rand(1, 3, 64, 64)
# 初始化为一些随机值
labels = torch.rand(1, 1000)

print(data)
print(labels)

# forward pass 通过模型的每一层运行输入数据以进行预测。这是前向传播。
prediction = model(data)

# 使用模型的预测和相应的标签来计算误差（loss）。下一步是通过网络反向传播此误差。
# 当对误差张量调用 .backward() 时，反向传播开始。
# 然后，Autograd 计算并将每个模型参数的梯度存储在参数的 .grad 属性中。
loss = (prediction - labels).sum()

print("loss:", loss)
# backward pass 反向传播
loss.backward()

# 加载一个优化器
optim = torch.optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
print(optim)

# 调用 .step() 以启动梯度下降。优化器通过存储在 .grad 中的梯度调整每个参数
optim.step()
