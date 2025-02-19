"""
 * @author: zkyuan
 * @date: 2025/2/19 11:50
 * @description:
"""
import random

# user-Agent池，防止反爬

UAlist = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
]

print(random.choice(UAlist))

# 可能出现异常
from fake_useragent import UserAgent

# 随机生成user-agent
print(UserAgent().random)

