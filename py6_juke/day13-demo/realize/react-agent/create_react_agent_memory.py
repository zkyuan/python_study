# 首先我们初始化我们想要使用的模型。
from langchain_openai import ChatOpenAI
# 使用 gpt-4o 模型，设定温度为 0（温度控制生成内容的随机性，0 表示确定性输出）
model = ChatOpenAI(model="gpt-4o", temperature=0)
# 对于本教程，我们将使用一个自定义工具，该工具返回两个城市（纽约和旧金山）的预定义天气值
from typing import Literal
# 从 langchain_core.tools 导入 tool 装饰器
from langchain_core.tools import tool


# 定义一个工具函数 get_weather，它根据城市名称返回预定义的天气信息
@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")


# 将工具放入一个列表中
tools = [get_weather]

# 我们可以使用 LangGraph 的检查点器添加“聊天记忆”到图中，以保留交互之间的聊天上下文
from langgraph.checkpoint.memory import MemorySaver

# 初始化 MemorySaver 实例
memory = MemorySaver()

# 定义图
from langgraph.prebuilt import create_react_agent

# 使用指定的模型、工具和检查点器创建 REACT 代理
graph = create_react_agent(model, tools=tools, checkpointer=memory)


# 定义一个函数用于打印流数据
def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


# 配置参数
config = {"configurable": {"thread_id": "1"}}
# 输入参数，包含用户消息
inputs = {"messages": [("user", "What's the weather in NYC?")]}
# 打印流输出
print_stream(graph.stream(inputs, config=config, stream_mode="values"))

# 再次输入参数，包含用户消息
inputs = {"messages": [("user", "What's it known for?")]}
# 打印流输出
print_stream(graph.stream(inputs, config=config, stream_mode="values"))
