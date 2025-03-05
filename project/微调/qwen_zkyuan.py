import requests

api_url = "http://qwen-zkyuan-01.1665021590116887.cn-shanghai.pai-eas.aliyuncs.com/"
api_key = "N2IzN2MwZTQ1MTc5ZDg4MDIyZmZlZDM3ZjJiNzQ5OTc3YTJkYTgzZQ=="
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "prompt": "张魁元是谁",
    "max_tokens": 100
}
response = requests.post(api_url, json=data, headers=headers)
print(response.status_code)
print(response.text)
