"""
 * @author: zkyuan
 * @date: 2025/2/19 17:41
 * @description:
"""
import torch

x = torch.rand(5, 3)

y = torch.randn_like(x, dtype=torch.float)

# 矩阵相加四种方式
print(x + y)

print(torch.add(x, y))

# 创建空矩阵
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)

# 相加后直接存在其中一个矩阵
y.add_(x)  # 相加   存在y里
print(y)

print("-------------------------------")
print(x)
# numpy打印
# 打印第1列（0开始）
print(x[:, 1])
# 打印前两列
print(x[:, :2])
# 打印前一行
print(x[:1, :])
print("-------------------------------")

# 改变张量的形状view()
x = torch.randn(4, 4)
# 单一维度
y = x.view(16)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())
print(y)

# item()取出值

# Torch Tensor 和Numpy array 转化


# GPU 和CPU
# 安装cuda  nvcc -V
# 查看pytorch官网，根据版本拿到安装对应pytorch的命令
if torch.cuda.is_available():
    print("=====在GPU上做数据计算=====")
    # 定义一个设备对象，这里指定成cuda，即GPU
    device = torch.device("cuda")
    # 直接在GPU上创建一个Tensor
    y = torch.ones_like(x, device=device)
    # 将在cpu上的x张量移动到GPU上
    x = x.to(device)
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))
