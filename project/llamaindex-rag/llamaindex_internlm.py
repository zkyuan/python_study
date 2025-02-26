from llama_index.core.llms import ChatMessage
from llama_index.llms.huggingface import HuggingFaceLLM

#  使用 HuggingFace 加载本地大模型
llm = HuggingFaceLLM(
    # 给定的是本地模型的路径
    model_name="D:\AI_Model\Qwen\Qwen1___5-0___5B-Chat",
    tokenizer_name="D:\AI_Model\Qwen\Qwen1___5-0___5B-Chat",
    model_kwargs={"trust_remote_code": True},
    tokenizer_kwargs={"trust_remote_code": True}
)

rsp = llm.chat(messages=[ChatMessage(content="xtuner是什么？")])
print(rsp)
