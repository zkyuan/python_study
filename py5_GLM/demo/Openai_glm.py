from openai import OpenAI
import os
# 使用OpenAI的API

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "zhipu"
os.environ["LANGCHAIN_API_KEY"] = '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'

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