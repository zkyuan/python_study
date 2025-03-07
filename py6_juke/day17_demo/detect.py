import torch
from transformers import AutoTokenizer
from transformers import TextGenerationPipeline
from transformers import AutoModelForCausalLM, GPT2Model

#加载编码器
# tokenizer = AutoTokenizer.from_pretrained('uer/gpt2-chinese-cluecorpussmall')
#
# model = AutoModelForCausalLM.from_pretrained(
#     'uer/gpt2-chinese-cluecorpussmall')

#将模型地址指向本地模型
tokenizer = AutoTokenizer.from_pretrained(r'C:\Users\Mr.Zhang\.cache\huggingface\hub\models--uer--gpt2-chinese-cluecorpussmall\snapshots\c2c0249d8a2731f269414cc3b22dff021f8e07a3')

# Auto 通用的接口
model = AutoModelForCausalLM.from_pretrained(
    r'C:\Users\Mr.Zhang\.cache\huggingface\hub\models--uer--gpt2-chinese-cluecorpussmall\snapshots\c2c0249d8a2731f269414cc3b22dff021f8e07a3')
#加载我们自己训练的模型权重
model.load_state_dict(torch.load("net.pt"))
print(model)

pipline = TextGenerationPipeline(model, tokenizer)

print(pipline('天高', max_length=24))