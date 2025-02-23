"""
 * @author: zkyuan
 * @date: 2025/2/23 21:15
 * @description: 智普GLM大模型
"""
import os

from zhipuai import ZhipuAI

model = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))



result = model.chat.completions.create(
    model="glm-4-plus",
    messages=[{'role': "user", 'content': '用C语言写一个冒泡排序的函数', }]
)

print(result)

