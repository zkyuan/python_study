"""
 * @author: zkyuan
 * @date: 2025/2/20 12:47
 * @description: 调用通义千问
"""
import dashscope
from dashscope import Generation
from dashscope.api_entities.dashscope_response import Role

# 1、如果环境变量配置无效请启用以下代码
# dashscope.api_key = 'YOUR_DASHSCOPE_API_KEY'
# os.environ["dashscope_api_key"] = 'YOUR_DASHSCOPE_API_KEY'

# 2、使用通义千问API进行Token切分 Tokenization
response = dashscope.Tokenization.call(model='qwen-turbo', messages=[{'role': 'user', 'content': '你好？'}])
print(response)
# {"status_code": 200, "request_id": "6d53e094-e8bc-9d88-a84a-6085c9425ad8", "code": "", "message": "", "output": {"token_ids": [108386, 11319], "tokens": ["你好", "？"]}, "usage": {"input_tokens": 2}}


# 3、调用通义千问回答问题 Generation
# 准备msg参数
messages = [{'role': 'user', 'content': '如何做西红柿鸡蛋汤？'}]
response = dashscope.Generation.call(dashscope.Generation.Models.qwen_turbo, messages=messages, result_format='message')
# print(response)
# {"status_code": 200, "request_id": "537d7681-8aa2-9f15-a17d-1b8492ad901f", "code": "", "message": "", "output": {"text": null, "finish_reason": null, "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "材料：鸡蛋2个，西红柿1个。\n\n做法：\n\n1. 鸡蛋打入碗中搅拌均匀备用；\n\n2. 西红柿洗净切块备用；\n\n3. 热锅凉油，油热后放入搅拌好的鸡蛋液，用筷子快速划散成小块，凝固即可盛出备用；\n\n4. 锅内再加少量底油，放入西红柿翻炒出汁，倒入炒好的鸡蛋，加入适量盐、糖调味翻匀即可。"}}]}, "usage": {"input_tokens": 12, "output_tokens": 106, "total_tokens": 118}}

print(response.output.choices[0]["message"]["content"])

print("------------------------")

# 连续对话，将上面的结果拿下来，再传给大模型
messages.append({'role': response.output.choices[0]['message']['role'],
                 'content': response.output.choices[0]['message']['content']})
messages.append({'role': Role.USER, 'content': '不放糖可以吗？'})
response = Generation.call(Generation.Models.qwen_turbo, messages=messages, result_format='message')
print(response.output.choices[0]['message']['content'])

# 4、通过prompt提示词对话，更简单
response = dashscope.Generation.call(model=dashscope.Generation.Models.qwen_turbo, prompt='如何做西红柿鸡蛋汤？')
print(response.output['text'])

# 5、流式输出，一边生成一边输出结果
# 两个参数 stream=True,incremental_output=True ，for循环输出
messages = [{'role': 'user', 'content': '如何做西红柿鸡蛋汤？'}]
responses = Generation.call(Generation.Models.qwen_turbo, messages=messages, result_format='message', stream=True,
                            incremental_output=True)
for response in responses:
    print(response.output.choices[0]['message']['content'], end='')

# 6、控制台循环对话
msg = []
while True:
    msgs = input('user:')
    # 停止条件
    if msgs == 'z':
        break
    # 将输入信息加入历史对话
    msg.append({'role': Role.USER, 'content': msgs})
    # 获得模型输出结果
    response = Generation.call(Generation.Models.qwen_turbo, messages=msg, result_format='message')
    print('system:' + response.output.choices[0]['message']['content'])
    # 将输出信息加入历史对话
    msg.append({'role': response.output.choices[0]['message']['role'],
                     'content': response.output.choices[0]['message']['content']})
