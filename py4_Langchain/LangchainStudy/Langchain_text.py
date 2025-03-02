"""
 * @author: zkyuan
 * @date: 2025/2/23 18:31
 * @description: AI大模型文本分类：
    情感分析
    话题标记
    新闻分类
    对话行为
    自然语言推理
    关系分析
    时间预测
"""
import os

from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "文本分类"
os.environ["LANGCHAIN_API_KEY"] = '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'

model = ChatTongyi(model="qwen-plus")


# class Classification(BaseModel):
#     """
#         定义一个Pydantic的数据模型，未来需要根据该类型，完成文本的分类
#     """
#     # 文本的情感倾向，预期为字符串类型
#     sentiment: str = Field(description="文本的情感")
#
#     # 文本的攻击性，预期为1到10的整数
#     aggressiveness: int = Field(
#         description="描述文本的攻击性，数字越大表示越攻击性"
#     )
#
#     # 文本使用的语言，预期为字符串类型
#     language: str = Field(description="文本使用的语言")

class Classification(BaseModel):
    """
        定义一个Pydantic的数据模型，未来需要根据该类型，完成文本的分类
    """
    # enum枚举指定取值范围
    # 文本的情感倾向，预期为字符串类型
    sentiment: str = Field(..., enum=["happy", "neutral", "sad"], description="文本的情感")

    # 文本的攻击性，预期为1到5的整数
    aggressiveness: int = Field(..., enum=[1, 2, 3, 4, 5], description="描述文本的攻击性，数字越大表示越攻击性")

    # 文本使用的语言，预期为字符串类型
    language: str = Field(..., enum=["spanish", "english", "french", "中文", "italian"], description="文本使用的语言")


# 创建一个用于提取信息的提示模板
tagging_prompt = ChatPromptTemplate.from_template(
    """
    从以下段落中提取所需信息。
    只提取'Classification'类中提到的属性。
    段落：
    {input}
    """
)

chain = tagging_prompt | model.with_structured_output(Classification)

input_text = "这个队友太坑了，做出的事情实在让我生气！"
# input_text = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"
# result: Classification = chain.invoke({'input': input_text})
# 返回的结果是Classification类型
result = chain.invoke({'input': input_text})
print(result)
