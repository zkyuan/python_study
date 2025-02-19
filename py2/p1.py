"""
 * @author: zkyuan
 * @date: 2025/2/19 10:30
 * @description: 网络爬虫
"""
# 1、网络请求

# https://www.baidu.com  url：统一资源占位符

# 请求过程：客户端 指向web浏览器向服务器发送请求

"""
    请求网址：request url
    请求方法：request methods
    请求头：request header
    请求体：request body
"""
# 请求响应 F12

# 2、网络爬虫的基本流程
"""
    确认目标：目标url：
    发送请求：发送网络请求，获取特定的服务端给你的响应
    提取数据：从响应中提取特定的数据  jsonpath/xpath/re
    保存数据：本地（html、json、txt)、数据库
    
    获取到的响应中，有可能会提取到还需要继续发送请求的url，可以继续拿着解析到的url继续发送请求
"""

# robots协议  约定俗成的规范

# 3、网络通信

# request请求的使用
# 安装模块：pip install requests

import requests

# 找到目标url（在headers里）
url = 'https://www.baidu.com'

# 发送请求
requests_get = requests.get(url)

print(requests_get)  # <Response [200]> 200成功

requests_get.encoding = 'utf-8'
print(requests_get.text)  # 乱码

print(requests_get.content.decode())  # 解码

# 找一张图片
url1 = 'https://image.baidu.com/favicon.ico'

getResp = requests.get(url1)

print(getResp.content)  # 不乱码

with open("baiduImg.png", "wb") as p:
    p.write(getResp.content)

# 其他属性
"""
    response.text：str类型；requests模块自动根据http头部对响应的编码作出有根据的推测
    response.content：bytes类型，通过decode()解码
    response.encoding：指定text的编码格式
    response.url
    response.
    response.
    response.
    response.
    response.
"""
# 用户代理 user-Agent

# 构建请求头,模拟浏览器发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    # 'Cookie' : ''
}
# 带上user-agent发送请求
# headers参数接收字典形式的请求头，
response = requests.get(url, headers=headers)

print(response.request.headers)
print(response.content.decode())
