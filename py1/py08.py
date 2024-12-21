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
