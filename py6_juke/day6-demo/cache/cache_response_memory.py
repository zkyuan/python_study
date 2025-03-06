import time
import os

# pip install -qU langchain-openai
from langchain_openai import ChatOpenAI
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache

# 创建LLM实例
llm = ChatOpenAI(model="gpt-4")
# 相同的问题调缓存比调大模型更快
set_llm_cache(InMemoryCache())

def measure_invoke_time(llm, prompt):
    # 记录开始时间
    start_wall_time = time.time()
    start_cpu_times = os.times()

    # 调用LLM
    response = llm.invoke(prompt)

    # 记录结束时间
    end_wall_time = time.time()
    end_cpu_times = os.times()

    # 计算经过的时间
    wall_time = end_wall_time - start_wall_time
    user_time = end_cpu_times.user - start_cpu_times.user
    sys_time = end_cpu_times.system - start_cpu_times.system
    total_cpu_time = user_time + sys_time

    return response, wall_time, user_time, sys_time, total_cpu_time

# 第一次调用
response1, wall_time1, user_time1, sys_time1, total_cpu_time1 = measure_invoke_time(llm, "给我讲个笑话")
print("First call response:", response1)
print(f"First call CPU times: user {user_time1 * 1000:.0f} ms, sys: {sys_time1 * 1000:.0f} ms, total: {total_cpu_time1 * 1000:.0f} ms")
print(f"First call Wall time: {wall_time1 * 1000:.0f} ms")

# 第二次调用
response2, wall_time2, user_time2, sys_time2, total_cpu_time2 = measure_invoke_time(llm, "给我讲个笑话")

print("Second call response:", response2)
print(f"Second call CPU times: user {user_time2 * 1000:.0f} ms, sys: {sys_time2 * 1000:.0f} ms, total: {total_cpu_time2 * 1000:.0f} ms")
print(f"Second call Wall time: {wall_time2 * 1000:.0f} ms")

"""
First call response: content='当然可以！这是一个经典的笑话：\n\n有一天，小明问爸爸：“爸爸，‘成功’的秘诀是什么？”\n\n爸爸想了想，回答道：“成功的秘诀就是四个字——‘不要说’。”\n\n小明好奇地问：“为什么呢？”\n\n爸爸微微一笑：“因为说出来就不灵了！”\n\n希望这个笑话能让你开心！' additional_kwargs={'refusal': None} response_metadata={'token_usage': None, 'model_name': None, 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-be7eae9a-fe64-44f4-9c66-7aeee3c3467d-0'
First call CPU times: user 16 ms, sys: 0 ms, total: 16 ms
First call Wall time: 2433 ms
Second call response: content='当然可以！这是一个经典的笑话：\n\n有一天，小明问爸爸：“爸爸，‘成功’的秘诀是什么？”\n\n爸爸想了想，回答道：“成功的秘诀就是四个字——‘不要说’。”\n\n小明好奇地问：“为什么呢？”\n\n爸爸微微一笑：“因为说出来就不灵了！”\n\n希望这个笑话能让你开心！' additional_kwargs={'refusal': None} response_metadata={'token_usage': None, 'model_name': None, 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-be7eae9a-fe64-44f4-9c66-7aeee3c3467d-0'
Second call CPU times: user 0 ms, sys: 0 ms, total: 0 ms
Second call Wall time: 0 ms
"""