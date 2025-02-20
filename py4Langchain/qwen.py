"""
 * @author: zkyuan
 * @date: 2025/2/20 12:47
 * @description: 调用通义千问
"""
import dashscope

# 如果环境变量配置无效请启用以下代码
# dashscope.api_key = 'YOUR_DASHSCOPE_API_KEY'

# respose获得的为
response = dashscope.Tokenization.call(model='qwen-turbo', messages=[{'role': 'user', 'content': '你好？'}])
print(response)

# {"status_code": 200, "request_id": "6d53e094-e8bc-9d88-a84a-6085c9425ad8", "code": "", "message": "", "output": {"token_ids": [108386, 11319], "tokens": ["你好", "？"]}, "usage": {"input_tokens": 2}}


messages = [{'role': 'user', 'content': '如何做西红柿鸡蛋汤？'}]

response = dashscope.Generation.call(dashscope.Generation.Models.qwen_turbo,messages=messages,result_format='message')
# print(response)
# {"status_code": 200, "request_id": "537d7681-8aa2-9f15-a17d-1b8492ad901f", "code": "", "message": "", "output": {"text": null, "finish_reason": null, "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "材料：鸡蛋2个，西红柿1个。\n\n做法：\n\n1. 鸡蛋打入碗中搅拌均匀备用；\n\n2. 西红柿洗净切块备用；\n\n3. 热锅凉油，油热后放入搅拌好的鸡蛋液，用筷子快速划散成小块，凝固即可盛出备用；\n\n4. 锅内再加少量底油，放入西红柿翻炒出汁，倒入炒好的鸡蛋，加入适量盐、糖调味翻匀即可。"}}]}, "usage": {"input_tokens": 12, "output_tokens": 106, "total_tokens": 118}}

print(response.output.choices[0]["message"]["content"])

