"""
 * @author: zkyuan
 * @date: 2025/2/23 10:52
 * @description: langchain生成数据
"""
from langchain_community.chat_models import ChatTongyi
from langchain_experimental.synthetic_data import create_data_generation_chain

model = ChatTongyi(model="qwen-plus", temperature=0.8)

# 创建链
chain = create_data_generation_chain(model)

# 生成数据
result = chain.invoke(  # 给于一些关键词， 随机生成一句话
    {
        # 字段领域
        "fields": {"颜色": ['蓝色', '黄色']},
        # 偏好
        "preferences": {"风格": "像诗歌一样"}
    }
)
print(result)
