#中文对联
from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline

tokenizer = BertTokenizer.from_pretrained("uer/gpt2-chinese-couplet")
model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-couplet")
text_generator = TextGenerationPipeline(model, tokenizer)
print(text_generator("[CLS]十口心思，思乡思国思社稷 -", max_length=28, do_sample=True))
