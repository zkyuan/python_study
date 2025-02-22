"""
 * @author: zkyuan
 * @date: 2025/2/22 16:02
 * @description: Agent代理，执行操作
"""
import os

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage

api_base = '127.0.0.1:7897'

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "Agent"
os.environ["LANGCHAIN_API_KEY"] = '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'
os.environ["TAVILY_API_KEY"] = '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'

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4",
    # gpt代理配置
    base_url='https://api.aihao123.cn/luomacode-api/open-api/v1',
    api_key=os.getenv("OPENAI_API_KEY")
)

# 没用代理的情况
# result = chain.invoke([HumanMessage(content="广州天气怎么样？")])
# print(result)

# Langchain内置的工具Tavily搜索
search = TavilySearchResults(max_results=2)  # max_results最大返回结果数量
# print(search.invoke("现在是2025年2月，美国总统是谁？"))
print("++++++++++++++")

# 创建工具
tools = [search]
#模型绑定工具
model_with_tools = model.bind_tools(tools)
# 调用大模型
response = model_with_tools.invoke([HumanMessage(content="美国总统是谁？")])
print(response)
print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")

response2 = model_with_tools.invoke([HumanMessage(content="北京天气怎么样？")])
print(response2)
print(f"ContentString: {response2.content}")
print(f"ToolCalls: {response2.tool_calls}")