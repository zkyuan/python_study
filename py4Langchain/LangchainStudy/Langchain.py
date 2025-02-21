"""
 * @author: zkyuan
 * @date: 2025/2/21 20:06
 * @description:langchain+代理gpt+
"""
import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# 翻墙代理的端口
api_base = '127.0.0.1:7897'

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "Langchain"
os.environ["LANGCHAIN_API_KEY"] = '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'

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

# 结果
# print(model.invoke(messages))

# 输出解析器,只输出content的结果而没有多余信息
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
# 将结果传给解析器
# result = model.invoke(messages)
# print(parser.invoke(result))

# 将模型与输出解析器链式连接，每次都会调用此解析器
# chain = model | parser
# print(chain.invoke(messages))

# 提示词模版
from langchain_core.prompts import ChatPromptTemplate

# 创建提示词模版
prompt_template = ChatPromptTemplate.from_messages(
    [("system", "Translate the following into {language}:"), ("user", "{text}")]
)
# 给提示词模版传参，它得到的结果就是特殊类型 ChatPromptValue(messages=[SystemMessage(content='Translate the following into italian:'), HumanMessage(content='hi')])
msg = prompt_template.invoke({"language": 'Chinese', "text": "hello!"})

"""
消息占位符
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder("msgs")
    ])
    prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})
这样就可以生成多条msgs时，只需要一条system消息
"""
"""
一种不显式使用 MessagesPlaceholder 类来实现相同功能的替代方法是：
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        ("placeholder", "{msgs}") # <-- This is the changed part
    ])
"""

# 将它转为messages格式
to_messages = msg.to_messages()
# print(chain.invoke(to_messages))

# 可以将大模型、解析器、提示词模版链接起来，
chain = prompt_template | model | parser
print(chain.invoke({"language": 'Chinese', "text": "hello!my name is zky"}))

# LangServe服务

