"""
 * @author: zkyuan
 * @date: 2024/12/20 16:24
 * @Description: 函数
"""
# define定义函数
"""
def 函数名(参数1,参数2...):
    函数体
"""


# 调用函数：函数名(实参1，实参2...)
# 函数返回值 return（执行return函数结束），没有返回值默认为None，多个返回值为元组的形式返回

# 参数
# 必备参数（位置参数）：传递和定义参数的顺序及个数必须一致
def fun1(parameter1, parameter2):
    print("fun1函数体：")


fun1(1, 2)


# 默认参数：为参数提供默认值，调用函数可以不穿该参数的值（所有位置参数必须出现在默认参数前面）
def fun2(parameter1, parameter2, a=1):
    print("fun2函数体:")


fun2(1, 2)


# 可变参数：*args，传入的值的数量是可以改变的，可以传多个，也可以不传
def fun3(*args):
    print("fun3函数体：")


fun3()


# 关键字参数：**keyWordsArgs,实参使用键值对的形式(变量名=值)，以字典的形式接收
def fun4(**kwargs):
    print("fun4函数体：")
    print(kwargs)


fun4(name="zky", age="18")

# 函数嵌套：在一个函数里面调用另一个函数
# 嵌套定义

# 作用域  全局变量、局部变量
# 申请为全局变量 global
# nonlocal 申明外一层的局部变量，用此申明，能对上一层的变量进行修改
a = 100


def fun5(*args):
    print("fun5函数体：")
    a = 110
    b = 200
    global c  # 全局变量先申明，再赋值
    c = 300
    print(a)


fun5()  # 110
print(a)  # 100
# print(b) # 报错没有b变量
print(c)  # 300
c = 111
print(c)  # 111


# 匿名函数：函数名 = lambda 形参 : 返回值
# 普通函数
def add(a, b):
    return a + b


print(add(1, 2))
# 匿名函数
add = lambda a, b: a + b
print(add(1, 3))

# 没有参数
fun6 = lambda: "fun1：无参的匿名函数"
print(fun6())

# 默认参数(默认参数必须写在非默认参数后面)
fun7 = lambda name, age=18: (name, age)
print(fun7("zky", 20))
print(fun7("zky"))

# 关键字参数
fun8 = lambda **kwargs: kwargs
print(fun8(name="zhangkyuan", age="22"))

# lambda与if结合

# 内置函数
# 查看所有内置函数
import builtins

print(dir(builtins))  # 大写开头：内置常量名 ； 小写开头：内置函数名

