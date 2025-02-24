"""
 * @author: zkyuan
 * @date: 2025/2/24 13:23
 * @description: GLM通过langchain整合sql，+执行sql语句的工具
 prompt ---> LLM ---> SQL --->  function ---> DB ---> prompt ---> LLM ---> result
"""
import os
from operator import itemgetter

from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.tools import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "zhipu"
os.environ["LANGCHAIN_API_KEY"] = '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'

model = ChatOpenAI(
    model='glm-4-plus',
    # temperature='0.6',
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url='https://open.bigmodel.cn/api/paas/v4/'
)

# sqlalchemy 初始化MySQL数据库的连接
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'langchain_db'
USERNAME = 'root'
PASSWORD = '123456'
# mysqlclient驱动URL
MYSQL_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# 创建数据库工具
db = SQLDatabase.from_uri(MYSQL_URI)

# 将数据库和模型链接
create_sql = create_sql_query_chain(llm=model, db=db)

# 对大模型生成的sql语句进行提取，并链入总链
create_sql = create_sql | (lambda x: x.replace('```sql', '').replace('```', '').replace('SQLResult:', ''))
# chain = create_sql | (lambda x: x.replace('```sql', '').replace('```', '')) | execute_sql

# sql操作提示词模版
answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question. 用中文回答最终答案
    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
)

# 链上提示词、大模型、格式化输出
answer_chain = answer_prompt | model | StrOutputParser()

# langchain内置的工具，进行数据库操作，如：执行sql
execute_sql = QuerySQLDataBaseTool(db=db)

chain = RunnablePassthrough.assign(query=create_sql).assign(result=itemgetter('query') | execute_sql) | answer_chain

resp = chain.invoke({'question': '请问：一共有多少个员工？'})
print(resp)

resp = chain.invoke({'question': '请问：哪个员工的工资最高？并且返回该员工的工资'})
print(resp)
