"""
 * @author: zkyuan
 * @date: 2025/2/21 20:06
 * @description:langchain+代理gpt
"""
import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# 翻墙代理
api_base = '127.0.0.1:7897'

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    # gpt代理配置
    base_url='https://api.aihao123.cn/luomacode-api/open-api/v1',
    api_key=os.getenv("OPEN_API_KEY")
)

messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="hi!"),
]

print(model.invoke(messages))
