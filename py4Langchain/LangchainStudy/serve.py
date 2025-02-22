import os

from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes

# 配置环境
# 翻墙代理的端口
api_base = '127.0.0.1:7897'

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "Langchain"
os.environ["LANGCHAIN_API_KEY"] = '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'

# 1、创建提示词模版Create prompt template
"""
翻译模版的两个参数
    1：language翻译的目标语言
    2：text要翻译的内容
"""
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2、创建大模型Create model
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    # gpt代理配置
    base_url='https://api.aihao123.cn/luomacode-api/open-api/v1',
    api_key=os.getenv("OPEN_API_KEY")
)

# 3、创建解析器Create parser
parser = StrOutputParser()

# 4、创建链接器Create chain
chain = prompt_template | model | parser

# 5、定义服务App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# 6、添加路由访问地址Adding chain route,
"""
post请求，地址：localhost:8000/chain/invoke
请求参数：
    {
        "input":
        {
            "language":"English",
            "text":"你好，我的名字是zky"
        }
    }
"""
add_routes(
    app,
    chain,
    path="/chain",
)

# 服务入口函数
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

"""python代码调用方式
    client = RemoteRunnable('localhost:8000/chain/')
    print(client.invoke({'language': 'italian', 'text': '你好！'}))
"""