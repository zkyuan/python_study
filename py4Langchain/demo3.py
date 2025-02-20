"""
 * @author: zkyuan
 * @date: 2025/2/20 18:14
 * @description:
"""
import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_community.tools import DuckDuckGoSearchResults


# 加载 .env 文件
load_dotenv()

# 从环境变量中获取 API 配置
api_base = os.getenv("proxy")
api_key = os.getenv("DASHSCOPE_API_KEY")

print(api_base)
print(api_key)
# 初始化 DuckDuckGo 搜索工具
duckduckgo_tool = DuckDuckGoSearchResults()

# 初始化 ChatTongyi 模型
llm = ChatTongyi(
    model="qwen-plus",
    temperature=0,
    api_key=api_key,
    api_base=api_base,
    max_tokens=512,
)

# 用户查询
user_query = ("白玉京是谁?")

# 使用 DuckDuckGo 搜索工具进行查询
search_results = duckduckgo_tool.run(user_query)
print(search_results)


# 处理搜索结果，提取相关信息
if search_results and 'RelatedTopics' in search_results:
    # 提取前几个结果的标题和链接
    context = "\n".join(
        [f"{topic['Text']}: {topic['FirstURL']}" for topic in search_results['RelatedTopics'] if 'Text' in topic and 'FirstURL' in topic]
    )
else:
    context = "没有找到相关结果。"

# 将搜索结果作为上下文传递给 ChatTongyi 模型
final_query = [
    {"role": "system", "content": "你是一个智能助手。"},
    {"role": "user", "content": f"根据以下信息回答问题：\n{context}\n\n问题：{user_query}"}
]

# 使用 invoke 方法生成响应
response = llm.invoke(final_query)

# 打印最终响应
print(response)
