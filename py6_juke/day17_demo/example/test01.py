#中文歌词生成模型
from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

tokenizer = BertTokenizer.from_pretrained("uer/gpt2-chinese-lyric")
model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-lyric")
text_generator = TextGenerationPipeline(model, tokenizer)
# print(tokenizer)
#do_sample是否进行随机采样。为True时，每次生成的结果都不一样;为False时，每次生成的结果都是相同的。
print(text_generator("在下雨的天，你走在前面", max_length=100, do_sample=True))
