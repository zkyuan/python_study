"""
 * @author: zkyuan
 * @date: 2025/2/22 16:02
 * @description: Agent代理，执行操作
"""
import os

from langchain_community.chat_models import ChatTongyi

# api_base = '127.0.0.1:7897'

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "Agent"
os.environ["LANGCHAIN_API_KEY"] = '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'
os.environ["TAVILY_API_KEY"] = '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'
# os.environ["TAVILY_API_KEY"] = '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'

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4",
    # gpt代理配置
    base_url='https://api.aihao123.cn/luomacode-api/open-api/v1',
    # api_key=os.getenv("OPENAI_API_KEY")
)

llm = ChatTongyi(model="qwen-plus")

# 定义工具
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults(max_results=2)
# search_results = search.invoke("what is the weather in SF")
# print(search_results)
# 创建工具
tools = [search]
print(tools)
# 绑定工具
# model_with_tools = model.bind_tools(tools)

bind_tools = llm.bind_tools(tools)

from langchain_core.messages import HumanMessage

# response = bind_tools.invoke([HumanMessage(content="What's the weather in BeiJing?")])

# print(f"ContentString: {response.content}")
# print(f"ToolCalls: {response.tool_calls}")

# response = model_with_tools.invoke([HumanMessage(content="Hi!")])
#
# print(f"ContentString: {response.content}")
# print(f"ToolCalls: {response.tool_calls}")
#
# response2 = model_with_tools.invoke([HumanMessage(content="What's the weather in SF?")])
#
# print(f"ContentString: {response2.content}")
# print(f"ToolCalls: {response2.tool_calls}")

# 创建代理
from langgraph.prebuilt import create_react_agent

agent_executor = create_react_agent(llm, tools)

response = agent_executor.invoke({"messages": [HumanMessage(content="hi!")]})

print(response["messages"])


# response = agent_executor.invoke(
#     {"messages": [HumanMessage(content="今天北京天气怎么样")]}
# )
# print(response["messages"])

# 流式响应
for s in agent_executor.stream(
        {"messages": [HumanMessage(content="今天北京天气怎么样")]}
):
    print(s)

# 添加内存
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
agent = create_react_agent(llm, tools, checkpointer=memory)

# thread_id决定会话编号，换不同的id开启新的对话框
config = {"configurable": {"thread_id": "001"}}

for s in agent.stream(
        {"messages": [HumanMessage(content="现在是2025年2月，美国总统是谁？")]},
        config=config,
):
    print(s)
