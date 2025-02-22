import os

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

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
    api_key=os.getenv("OPEN_API_KEY")
)
# 解析器
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

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
for s in chain.stream({"messages": [HumanMessage(content="please talk a joy about cat!")], "language": "English", }):
    print(s,end="-")
