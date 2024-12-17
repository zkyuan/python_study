"""
 * @author: zkyuan
 * @date: 2024/12/18 5:04
 * @Description: 列表（集合）
 * l = list  # 赋值后虽然是两个变量，但是指向同一块内存空间，
"""
# 列表格式：列表名 = [元素1,元素2,元素3...] 元素的数据类型可以不一样
list = [1, 2, "zhang", 'a', "zkyuan"]
print(list)
print(list[0:3])
# 列表是可迭代对象
for i in range(0, 4):
    print(list[i], end=" ")
print()

# 列表的操作
# 1.添加：append() extend() insert()
"""
    append()：整体添加，添加在最后面
    extend()：分散添加，将另外一个类型的元素逐一添加，参数必须为可迭代对象，否则报错
    insert(插入位置,插入元素)：在指定位置插入元素,没有指定位置会报错
"""
list.append("zhangkuiyuan")
list.extend("zky")  # [1, 2, 'zhang', 'a', 'zkyuan', 'zhangkuiyuan', 'z', 'k', 'y']
list.insert(2, "zky")  # [1, 2, 'zky', 'zhang', 'a', 'zkyuan', 'zhangkuiyuan', 'z', 'k', 'y']
print(list)

# 2.修改元素，用下标进行修改
list[0] = "ok"
print(list)

# 3.查询： in 与 not in
flag = "zky" in list
print(flag)

while True:
    username = input("请输入账号")
    if username in list:
        print("已存在！请重新输入")
        continue
    else:
        list.append(username)
        print("保存成功")
        break
print(list)

# index()：返回指定数据位置的下标，如果查找不到就报错
# count()：统计指定元素在列表中的个数

# 4.删除元素 del、pop()、remove()
# 删除整个列表
l = list
del l
# 根据下标删除
del list[1]
print(list)

# pop ：删除指定下标的元素，默认最后一个
l = list  # 赋值后虽然是两个变量，但是指向同一块内存空间，
l.pop()
l.pop(2)
print(l)

# remove：根据元素值进行删除，列表中不存在则报错，默认删除出现的第一个元素
l.remove("z")

# 5.排序  sort()、reverse()
# sort()：将列表排序，默认升序
list.sort()
print(list)
# reverse()：列表倒置
list.reverse()
print(list)

# 6.列表推到式
# 格式1：[表达式 for 变量 in 列表] （in后面可以放列表、range()、可迭代对象）
[list.append(i) for i in range(0, 6)]  # 循环简写添加0-5
print(list)
# 格式2：[表达式 for 变量 in 列表 if 条件]
[list.append(i) for i in range(0, 6) if i % 2 == 1]  # 循环简写添加0-5的奇数
print(l)

# 7.列表嵌套：列表里面有列表元素
l1 = [1, 2, 3, 4, 5, 6, 7]
list.insert(0, l1)
print(list[0][2])  # 3
