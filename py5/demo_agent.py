"""
 * @author: zkyuan
 * @date: 2025/2/21 15:59
 * @description: agent例子
"""
from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import ChatOpenAI

load_dotenv()

# 定义llm
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",
)

# 谷歌工具包
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 创建Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # 这里有不同的类型
    verbose=True,  # 是否打印日志
)

print(agent.run("请问现任的中国主席是谁？他的年龄的平方是多少? 请用中文告诉我这两个问题的答案"))
