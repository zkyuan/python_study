"""
 * @author: zkyuan
 * @date: 2025/3/20 21:46
 * @description: openllm调用自己部署的大模型
"""
from langchain.chains.llm import LLMChain
from langchain_community.chat_models import ChatOllama
from langchain_community.llms import OpenLLM
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(
    model="deepseek-r1:70b",
    base_url="http://175.6.13.6:11434",#
    temperature=0,
    # other params...
)

template = "你能告诉我下面这个问题吗？{question}"

prompt = PromptTemplate.from_template(template)

llm_chain = LLMChain(prompt=prompt, llm=llm)

invoke = llm_chain.invoke(input={"question":"deepseek是什么"})

print(invoke)

