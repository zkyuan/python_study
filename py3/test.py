"""
公式模板:
ts_regression(ts_zscore(A, 500),ts_zscore(B
500),500)
其中:A 和 B为两个不同的数据字段;tszscore 表示计算数据在过去500天的标准化值;ts_regression表示对两个时间序列进行回归分析。
题目要求:
从数据字段列表中选择所有可能的 A和 B 组合，要
求 A 和 B 必须不同。
将每组 A 和 B 代入公式模板，生成对应的公式。
输出所有公式，并统计总的组合数量。
数据字段列表:fnd17_oxlcxspebq,fnd17_shsoutbs,
fnd28 value 05191g,
fnd28 value 05301g,fnd28 value 05302g,
fnd17 pehigh, fnd17_pelow,
fnd17_priceavg150day,fnd17_priceavg200day,
fnd17 priceavg50day, fnd17_pxedra,
fnd28 newa3 value 18191a,fnd28 value 02300a,
mdl175 ebitda, mdl175 pain
参考的其中一个输出:
ts_regression(ts_zscore(fnd17_oxlcxspebq, 500)
ts zscore(fnd17 shsoutbs, 500),500)

"""

data = ["fnd17_oxlcxspebq",
        "fnd17_shsoutbs",
        "fnd28_value_05191g",
        "fnd28_value_05301g",
        "fnd28_value_05302g",
        "fnd17_pehigh",
        "fnd17_pelow",
        "fnd17_priceavg150day",
        "fnd17_priceavg200day",
        "fnd17_priceavg50day",
        "fnd17_pxedra",
        "fnd28_newa3_value_18191a",
        "fnd28_value_02300a",
        "mdl175_ebitda",
        "mdl175_pain"]


def merge(text1, text2):
    return f"ts_regression(ts_zscore({text1}, 500), ts_zscore({text2}, 500), 500)"

result = []
len = len(data)
i = 0
while i < len - 1:
    j = i + 1
    while j < len:
        result.append(merge(data[i], data[j]))
        j += 1
    i += 1
print(result)
for i in result:
    print(i)