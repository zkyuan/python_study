"""
 * @author: zkyuan
 * @date: 2025/2/25 16:21
 * @description: langchain调用本地的大模型
"""
import os

from llama_index.core.llms import ChatMessage
from llama_index.llms.huggingface import HuggingFaceLLM

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "qwen本地模型"
os.environ["LANGCHAIN_API_KEY"] = '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'

model_path = "D:\AI_Model\Qwen\Qwen1___5-0___5B-Chat"

# 使用HuggingFace加载本地大模型
llm = HuggingFaceLLM(
    # 使用本地绝对路径
    model_name=model_path,
    tokenizer_name=model_path,
    model_kwargs={"trust_remote_code": True},
    tokenizer_kwargs={"trust_remote_code": True}
)

rep = llm.chat(messages=[ChatMessage(content="你擅长哪些方面的知识")])
print(rep)

from langchain_huggingface.llms import HuggingFacePipeline

"""
"text2text-generation",
    "text-generation",
    "summarization",
    "translation",
"""
task = ["text2text-generation","text-generation","summarization","translation"]
hf = HuggingFacePipeline.from_model_id(
    model_id=model_path,
    task=task[1], # 只能做text-generation
    device=0,
    pipeline_kwargs={"max_new_tokens": 1000},
)

print(hf.invoke("牛马"))
