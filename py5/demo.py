import requests


def request_chatgpt_function():
    url = "https://api.openai.com/v1/chat/completions"  # 可以替换为任何代理的接口
    OPENAI_API_KEY = "sk-LECc8U0BcVAQWx1VE23aB8B5595f4963929d799b712382E3"  # openai官网获取key
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
                "content": "Hello!"
            }
        ],
        "temperature": 0,
        "stream": False
    }
    response = requests.post(url=url, headers=header, json=data).json()
    print(response)
    return response

if __name__ == "__main__":
    request_chatgpt_function()  # 利用openai正常调用