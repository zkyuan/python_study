"""
 * @author: zkyuan
 * @date: 2025/2/22 13:40
 * @description: 向量存储与检索器，创建向量空间失败,代理的gpt在使用OpenAIEmbeddings和bind_tools等时会有问题
 向量存储+检索器让私有数据源参与大模型的回答
"""
import os

from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import RunnableLambda

api_base = '127.0.0.1:7897'

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "VectorBase"
os.environ["LANGCHAIN_API_KEY"] = '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'

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4",
    # gpt代理配置
    base_url='https://api.aihao123.cn/luomacode-api/open-api/v1',
    api_key=os.getenv("OPENAI_API_KEY")
    # api_key=os.getenv("DASHSCOPE_API_KEY"),
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
llm = ChatTongyi(model="qwen-plus")

# 解析器
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# 准备数据
from langchain_core.documents import Document

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
    # Document(
    #     page_content="狗是伟大的伴侣，以其忠诚和友好而闻名。",
    #     metadata={"source": "哺乳动物宠物文档"},
    # ),
    # Document(
    #     page_content="猫是独立的宠物，通常喜欢自己的空间。",
    #     metadata={"source": "哺乳动物宠物文档"},
    # ),
    # Document(
    #     page_content="金鱼是初学者的流行宠物，需要相对简单的护理。",
    #     metadata={"source": "鱼类宠物文档"},
    # ),
    # Document(
    #     page_content="鹦鹉是聪明的鸟类，能够模仿人类的语言。",
    #     metadata={"source": "鸟类宠物文档"},
    # ),
    # Document(
    #     page_content="兔子是社交动物，需要足够的空间跳跃。",
    #     metadata={"source": "哺乳动物宠物文档"},
    # ),
]
from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings

embedding = DashScopeEmbeddings()
# embeddings = OpenAIEmbeddings()
# 创建向量数据空间
vectorstore = Chroma.from_documents(documents=documents, embedding=embedding)

print(vectorstore.similarity_search_with_score("cat"))

embedding1 = DashScopeEmbeddings().embed_query("cat")

print(vectorstore.similarity_search_by_vector(embedding1))

# 创建检索器
# retriever = RunnableLambda(vectorstore.similarity_search).bind(k=1)  # bind(k=1) 选第一个
#
# retriever.batch(["cat", "shark"])

# 向量存储实现了一个 as_retriever 方法，该方法将生成一个检索器
retriever = vectorstore.as_retriever(
    search_type="similarity",  # 相似度
    search_kwargs={"k": 1},  # 选第一个
)

print(retriever.batch(["cat", "shark"]))

# 检索器可以轻松地纳入更复杂的应用程序，例如检索增强生成（RAG）应用程序，这些应用程序将给定问题与检索到的上下文结合成 LLM 的提示。
# 自定义数据源参与大模型的回答

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

message = """
Answer this question using the provided context only.

{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([("human", message)])

# 检索器入链
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

response = rag_chain.invoke("tell me about cats")

print(response.content)
