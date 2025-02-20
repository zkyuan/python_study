"""
 * @author: zkyuan
 * @date: 2025/2/20 16:22
 * @description: Langchain整合通义千问
"""
from typing import Optional

from langchain_community.chat_models import ChatTongyi
from pydantic import BaseModel

# LangChain 聊天模型的命名约定是在其类名前加上 “Chat” 前缀（例如，ChatOllama、ChatAnthropic、ChatOpenAI 等）。旧版也有不带chat的
# 1、模型
model = ChatTongyi(
    model="qwen-turbo",
    # 其他参数...
)
# 2、prompt
messages = [
    ("system", "你是一名专业的翻译家，可以将用户的中文翻译为英文。"),
    ("human", "我喜欢编程。"),
]

# 3、同步调用
response = model.invoke(messages)

# 4、结果解析
# print(response) # content='I like programming.' additional_kwargs={} response_metadata={'model_name': 'qwen-turbo', 'finish_reason': 'stop', 'request_id': '23f11a73-7032-9702-b672-0276d29f9536', 'token_usage': {'input_tokens': 30, 'output_tokens': 4, 'prompt_tokens_details': {'cached_tokens': 0}, 'total_tokens': 34}} id='run-05aa636a-368c-47bf-b3db-e75814bd2255-0'
# print(response.content)

# 响应元数据
# response.response_metadata


# 5、流式响应的调用方式
# for chunk in model.stream(messages):
#     # chunk:content='I' additional_kwargs={} response_metadata={} id='run-7eebd0cd-a98f-41d2-9062-a19863343fd2'
#     print(chunk.content)

# 6、该类可以将工具（使用 Pydantic 模型定义）绑定到聊天模型
# class GetWeather(BaseModel):
#     location: str
#
#
# chat_with_tools = model.bind_tools([GetWeather])
# ai_msg = chat_with_tools.invoke("今天哪个城市更热，哪个城市更大：洛杉矶还是纽约？")
# print(ai_msg.content)

# 7、该类可以返回结构化输出，通过定义 Pydantic 模型来指定期望的输出格式
class Joke(BaseModel):
    setup: str
    punchline: str
    rating: Optional[int]


# 按自定义结果输出结果
structured_chat = model.with_structured_output(Joke)
joke_response = structured_chat.invoke("给我讲一个关于猫的笑话")
print(joke_response)  # setup='为什么猫咪不喜欢在线上购物？' punchline='因为它们害怕结账时爪子会被卡住！' rating=4
