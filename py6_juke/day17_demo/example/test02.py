#中文文言文生成
from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

tokenizer = BertTokenizer.from_pretrained("uer/gpt2-chinese-ancient")
model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-ancient")
text_generator = TextGenerationPipeline(model, tokenizer ,device=0)
print(text_generator("于是者", max_length=100, do_sample=True))
# print(tokenizer)
