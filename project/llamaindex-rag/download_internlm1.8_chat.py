# 模型下载
from modelscope import snapshot_download

model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm2-chat-1_8b',
                              cache_dir='D:/AIProject/modelscope')

# model_dir = snapshot_download('Qwen/Qwen1___5-0___5B-Chat',
#                               cache_dir='D:/AI_Model')
