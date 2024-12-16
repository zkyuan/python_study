# 字符串
str1: str = "字符串"
str2 = "字符串"
# 编码
"""
Unicode：所有字符都是2个字节
优点：字符和数字转换速度快
缺点：占用空间大

UTF-8：精准，不同字符用不同的长度表示
优点：节省空间
缺点：字符和数字转换速度慢，每次都需要计算字符要用多少个字节来表示

GKB
"""
# 字符编码转换
s = "hello"
print(s, type(s))  # 输出：hello <class 'str'>
# 编码
s_encode = s.encode()
print(s_encode, type(s_encode))  # 输出： b'hello' <class 'bytes'>
# 解码
s_encode_decode = s_encode.decode()
print(s_encode_decode, type(s_encode_decode))  # 输出： hello <class 'str'>
# 指定编码标准
str1 = "中文编码十六进制aaa"
encode = str1.encode(encoding="UTF-8")
print(encode)  # b'\xe4\xb8\xad\xe6\x96\x87\xe7\xbc\x96\xe7\xa0\x81\xe5\x8d\x81\xe5\x85\xad\xe8\xbf\x9b\xe5\x88\xb6aaa'
decode = encode.decode("UTF-8")
print(decode)

# 字符串拼接
print("10" + "10")  # 1010
fname = "张"
name = "三"
print(fname + name)  # 张三
print(fname, name)  # 张 三
print(fname, name, sep="")  # 张三

# 字符串重复 *
print("张起灵\t" * 10)

# 成员运算符：检查字符串中是否包含了某个子字符串
# in：包含返回True，不包含返回False
# not in：包含返回False，不包含返回True
name = "zhangkuiyuan"
print("yuan" in name) #True
print("yuan" not in name) #False
print("zkyuan" in name) #False
print("zkyuan" not in name) #True


