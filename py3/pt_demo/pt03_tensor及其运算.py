"""
 * @author: zkyuan
 * @date: 2025/2/19 22:03
 * @description: Tensor及其运算
 https://blog.csdn.net/CltCj/article/details/120060543?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522f1124a9908ad4dd0519a158c40e93091%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=f1124a9908ad4dd0519a158c40e93091&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-120060543-null-null.142^v101^pc_search_result_base4&utm_term=pytorch&spm=1018.2226.3001.4187
"""
import torch

# 1、tensor
# torch.FloatTensor用于生成数据类型为浮点型的Tensor，传递给torch.FloatTensor的参数可以是列表，也可以是一个维度值。
a = torch.FloatTensor(2, 3)
b = torch.FloatTensor([2, 3, 4, 5])

# torch.IntTensor用于生成数据类型为整型的Tensor,传递给传递给torch.IntTensor的参数可以是列表，也可以是一个维度值。
c = torch.IntTensor(2, 3)
d = torch.IntTensor([2, 3, 4, 5])

# torch.randn用于生成数据类型为浮点数且维度指定的随机Tensor，和在numpy中使用的numpy.randn生成的随机数的方法类似，随机生成的浮点数的取值满足均值为0，方差为1的正态分布。
e = torch.randn(2, 3)

# torch.range用于生成数据类型为浮点型且起始范围和结束范围的Tensor，所以传递给torch.range的参数有三个，分别为起始值，结束值，步长，其中步长用于指定从起始值到结束值得每步的数据间隔。
f = torch.range(1, 20, 2)

# torch.zeros用于生成数据类型为浮点型且维度指定的Tensor，不过这个浮点型的Tensor中的元素值全部为0。
# torch.ones生成全1的数组。
# torch.empty创建一个未被初始化数值的tensor, tensor的大小是由size确定, size: 定义tensor的shape ，这里可以是一个list也可以是一个tuple
g = torch.zeros(2, 3)

# 2、Tensor运算
# 将参数传递到torch.abs后返回输入参数的绝对值作为输出，输入参数必须是一个Tensor数据类型的变量
a = torch.abs(a)

# 将参数传递到torch.add后返回输入参数的求和结果作为输出，输入参数既可以全部是Tensor数据类型的变量，也可以一个是Tensor数据类型的变量，另一个是标量
a = torch.add(a, b)

a = torch.add(a, 10)

# torch.clamp是对输入参数按照自定义的范围进行裁剪，最后将参数裁剪的结果作为输出，所以输入参数一共有三个，分别是需要进行裁剪的Tensor数据类型的变量、裁剪的上上边界和裁剪的下边界，具体的裁剪过程是：使用变量中的每个元素分别和裁剪的上边界及裁剪的下边界的值进行比较，如果元素的值小于裁剪的下边界的值，该元素被重写成裁剪的下边界的值；同理，如果元素的值大于裁剪的上边界的值，该元素就被重写成裁剪的上边界的值
b = torch.clamp(a, -0.1, 0.1)

# torch.div是将参数传递到torch.div后返回输入参数的求商结果作为输出，同样，参与运算的参数可以全部是Tensor数据类型的变量，也可以是Tensor数据类型的变量和标量的组合。
a = torch.div(a, b)

# torch.pow：将参数传递到torch.pow后返回输入参数的求幂结果作为输出，参与运算的参数可以全部是Tensor数据类型的变量，也可以是Tensor数据类型的变量和标量的组合。
""" pow(a,b):a的b次方，若两个矩阵，则对应位置元素a的b次方
>>> a = torch.randn(4)
>>> a
tensor([ 0.4331,  1.2475,  0.6834, -0.2791])
>>> torch.pow(a, 2)
tensor([ 0.1875,  1.5561,  0.4670,  0.0779])
>>> exp = torch.arange(1., 5.)
 
>>> a = torch.arange(1., 5.)
>>> a
tensor([ 1.,  2.,  3.,  4.])
>>> exp
tensor([ 1.,  2.,  3.,  4.])
>>> torch.pow(a, exp)
tensor([   1.,    4.,   27.,  256.])
 
>>> torch.pow(2, a)
tensor([ 2.,  4.,  8., 16.])
>>> torch.pow(a, 2)
tensor([ 1.,  4.,  9., 16.])
"""

# torch.mm：将参数传递到torch.mm后返回输入参数的求积结果作为输出，不过这个求积的方式和之前的torch.mul运算方式不太一样，
# torch.mm运用矩阵之间的乘法规则进行计算，所以被传入的参数会被当作矩阵进行处理，参数的维度自然也要满足矩阵乘法的前提条件，即前一个矩阵的行数必须和后一个矩阵列数相等
# 即满足线性代数矩阵乘法
a = torch.mm(a, b)

# 将参数传递到torch.mv后返回输入参数的求积结果作为输出，torch.mv运用矩阵与向量之间的乘法规则进行计算，被传入的第1个参数代表矩阵，第2个参数代表向量，循序不能颠倒
# 矩阵 * 向量
a = torch.mv(a, b)

# 也可以用 + * - / 等符号

