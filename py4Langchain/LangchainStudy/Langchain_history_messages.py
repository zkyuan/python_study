"""
 * @author: zkyuan
 * @date: 2025/2/22 12:31
 * @description: 保存历史消息的格式
"""
import os

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

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

chain = model | parser

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """历史消息存储起来"""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# 用含历史消息的chain去调用
with_message_history = RunnableWithMessageHistory(chain, get_session_history)
# session的形式，每个session_id表示一个新对话
config = {"configurable": {"session_id": "12"}}
# 历史消息链调用，带着session请求
res1 = with_message_history.invoke(
    [HumanMessage(content="Hi! I'm Bob")],
    config=config,
)
print(res1)
res2 = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)
print(res2)
# 配置新对话
config = {"configurable": {"session_id": "123"}}
res3 = with_message_history.invoke(
    [HumanMessage(content="What's my name?")],
    config=config,
)
print(res3)
print("---------")
print(store)
"""BaseChatMessageHistory存储的历史消息格式，可以用trim_messages进行修剪：https://www.langchain.com.cn/docs/how_to/trim_messages/
{
	'12': InMemoryChatMessageHistory(
        messages = [
            HumanMessage(
                content = "Hi! I'm Bob", 
                additional_kwargs = {},
                response_metadata = {}
            ), 
            AIMessage(
                content = 'Hi Bob! How can I assist you today?',
                additional_kwargs = {}, 
                response_metadata = {}
            ), 
            HumanMessage(
                content = "What's my name?",
                additional_kwargs = {},
                response_metadata = {}
            ), 
            AIMessage(
                content = 'Your name is Bob! How can I help you today, Bob?', 
                additional_kwargs = {}, 
                response_metadata = {}
            )
        ]
    ),
	'123': InMemoryChatMessageHistory(
        messages = [
            HumanMessage(
                content = "What's my name?",
                additional_kwargs = {}, 
                response_metadata = {}
            ), 
            AIMessage(
                content = "I'm sorry, but I don't have access to personal information about users unless you share it with me. How can I assist you today?", 
                additional_kwargs = {}, 
                response_metadata = {}
            )
        ]
    )
}
"""