"""
 * @author: zkyuan
 * @date: 2025/2/22 9:55
 * @description: 聊天机器人
"""
import os

# 配置环境
# 翻墙代理的端口
api_base = '127.0.0.1:7897'

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "ChatBot"
os.environ["LANGCHAIN_API_KEY"] = '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'

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    # gpt代理配置
    base_url='https://api.aihao123.cn/luomacode-api/open-api/v1',
    api_key=os.getenv("OPENAI_API_KEY")
)
# 解析器
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# 简单调用
# chain = model | parser
from langchain_core.messages import HumanMessage
# res1 = chain.invoke([HumanMessage(content="Hi! I'm Bob")])
# print(res1)
# res2 = chain.invoke([HumanMessage(content="What's my name?")])
# print(res2)

# 传递历史对话给大模型。AIMessage参数为大模型说的话
from langchain_core.messages import AIMessage
#
# res = chain.invoke(
#     [
#         HumanMessage(content="Hi! I'm Bob"),
#         AIMessage(content="Hello Bob! How can I assist you today?"),
#         HumanMessage(content="What's my name?"),
#     ]
# )
# print(res) # Your name is Bob! How can I help you today?

# 历史消息
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory

# 创建字典存储历史消息到列表
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """历史消息存储起来"""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# 用含历史消息的chain去调用
# with_message_history = RunnableWithMessageHistory(chain, get_session_history)
# session的形式，每个session_id表示一个新对话
config = {"configurable": {"session_id": "12"}}
# 历史消息链调用，带着session请求
# res1 = with_message_history.invoke(
#     [HumanMessage(content="Hi! I'm Bob")],
#     config=config,
# )
# print(res1)
# res2 = with_message_history.invoke(
#     [HumanMessage(content="What's my name?")],
#     config=config,
# )
# print(res2)
# # 配置新对话
# config = {"configurable": {"session_id": "123"}}
# res3 = with_message_history.invoke(
#     [HumanMessage(content="What's my name?")],
#     config=config,
# )
# print(res3)

# 添加模版
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant. Answer all questions to the best of your ability.",
#         ),
#         # 参数占位符，messages的role是user
#         MessagesPlaceholder(variable_name="messages"),
#     ]
# )

# chain = prompt | model | parser

# 用含模版的链调用大模型
# rep = chain.invoke({"messages": [HumanMessage(content="hi! I'm bob")]})
# print(rep)

# with_message_history = RunnableWithMessageHistory(chain, get_session_history)
# reh1 = with_message_history.invoke([HumanMessage(content="hi!i am bob!")], config=config, )
# reh2 = with_message_history.invoke([HumanMessage(content="What's my name?")], config=config,)
# print(reh1)
# print(reh2)

# 模版加参数
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        # 参数占位符，messages的role是user
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | model | parser

# 多个参数，需要我们指定正确的键来确定哪个键才是历史消息，需要保存的
with_message_history = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="messages", )

# result = with_message_history.invoke(
#     # {"messages": [HumanMessage(content="现在美国总统是谁？")], "language": "Chinese"},
#     {"messages": [HumanMessage(content="现在美国总统是谁")], "language": "Chinese"},
#     config=config)
# print(result)


# 管理对话历史，消息修剪器 自定义修剪：https://www.langchain.com.cn/docs/how_to/trim_messages/
from langchain_core.messages import SystemMessage, trim_messages

# 参数
trimmer = trim_messages(
    max_tokens=65,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)
# 消息历史
messages = [
    SystemMessage(content="you're a good assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2 + 2 - 2 + 4 - 4 + 3 - 3"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
    HumanMessage(content="whats 2 + 2 + 2 - 2 + 4 - 4 + 3 - 3"),
    AIMessage(content="4"),
]
# 修剪
# trimmer_result = trimmer.invoke(messages)
# print(trimmer_result)

from operator import itemgetter

from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough.assign(messages=itemgetter("messages") | trimmer) | prompt | model | parser

# r1 = chain.invoke({"messages": messages + [HumanMessage(content="what's my name?")], "language": "English", })
# r2 = chain.invoke(
#     {"messages": messages + [HumanMessage(content="what math problem did i ask")], "language": "English", })
#
# print(r1)
# print(r2)

# 流式处理stream代替invoke
for s in chain.stream(
        {"messages": messages + [HumanMessage(content="please talk a joy about cat!")], "language": "English", }
):
    print(s, end=" ")
