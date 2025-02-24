"""
 * @author: zkyuan
 * @date: 2025/2/24 11:23
 * @description: GLM通过langchain整合sql
 prompt ---> LLM ---> SQL --->  function ---> DB ---> prompt ---> LLM ---> result
"""
import os

from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from zhipuai import ZhipuAI

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

db = SQLDatabase.from_uri(MYSQL_URI)
# 可以执行sql语句
# result = db.run('select * from employee;')
# print(result)

# 创建sql工具
chain = create_sql_query_chain(llm=model, db=db)

# chain.get_prompts()[0].pretty_print()  # 这是一个提示工程，能打印一个关于sql的prompt模版
"""
You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURDATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

Only use the following tables:
{table_info}

Question: {input}
"""

# 根据question得到sql语句，str型
sqlResult = chain.invoke({'question': '请问共有几个数据表，每个表中各有多少条数据'})
print(sqlResult)
"""
# SELECT 'employee' AS table_name, COUNT(*) AS row_count FROM employee
# UNION ALL
# SELECT 'student' AS table_name, COUNT(*) AS row_count FROM student;
# 
# SQLResult:
"""
# 提取出sql语句
sql = sqlResult.replace('```sql', '').replace('```', '').replace('SQLResult:','')
print('提取之后的SQL：' + sql)
print("--------------------")
# 若是提了两个问题，或者要执行两条sql语句才能查出结果，这里直接run会出线程问题
print(db.run(sql))


