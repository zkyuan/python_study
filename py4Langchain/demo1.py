"""
 * @author: zkyuan
 * @date: 2025/2/20 16:17
 * @description: 用openAI的方式调用通义千问
"""
import os

from openai import OpenAI

try:
    # 配置环境
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        # api_key="sk-",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    # 调用大模型，
    completion = client.chat.completions.create(
        # 模型
        model="qwen-plus",
        # 参数
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '你是谁？'}
        ]
    )
    # 结果解析
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
