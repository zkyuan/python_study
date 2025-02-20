"""
 * @author: zkyuan
 * @date: 2025/2/20 16:17
 * @description: 用openAI的方式调用通义千问
"""
from openai import OpenAI
from langchain_community.chat_models import ChatTongyi

try:
    # 配置环境
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        # api_key=os.getenv("DASHSCOPE_API_KEY"),
        api_key="sk-955a716c2390445388d3fc4e33d14e1e",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    # 调用，可以先准备参数
    completion = client.chat.completions.create(
        model="qwen_turbo",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '你是谁？'}
            ]
    )
    # 大模型输出的结果completion
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")


