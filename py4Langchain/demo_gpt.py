"""
 * @author: zkyuan
 * @date: 2025/2/21 21:28
 * @description: 调用代理的OpenAI GPT
"""
import os

import requests


def request_chatgpt_function():
    url = "https://api.aihao123.cn/luomacode-api/open-api/v1/chat/completions"  # 可以替换为任何代理的接口
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # openai官网获取key
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + OPENAI_API_KEY}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello! ZhouMin is my college roommate, how is his financial luck this year? can you tell me？"
            }
        ],
        "temperature": 0,
        "stream": False
    }
    response = requests.post(url=url, headers=header, json=data).json()
    # print(response)
    print(response)
    return response


if __name__ == "__main__":
    request_chatgpt_function()  # 利用openai正常调用
