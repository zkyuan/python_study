from openai import OpenAI
import os
# 使用OpenAI的API

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url='https://open.bigmodel.cn/api/paas/v4/'
)

# response = client.chat.completions.create(
#     model='glm-4-0520',
#     messages=[
#         {'role': "user", 'content': '北京天气怎么样？'}
#     ],
#     stream=True
# )


# print(response)

# print(response.choices[0].message.content)

for e in client.chat.completions.create(
        model='glm-4-0520',
        messages=[
            {'role': "user", 'content': '北京天气怎么样？'}
        ],
        # 流式输出
        stream=True
):
    print(e.choices[0].delta.content)