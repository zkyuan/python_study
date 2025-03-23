"""
 * @author: zkyuan
 * @date: 2025/3/23 15:52
 * @description:
 请求 --> controller --> model、pydantic --> service --> DB
"""

from fastapi import FastAPI

# 导入APIRouter的实例
from app1.router1 import app1
from app2.router2 import app2

# 实例化
app = FastAPI()

# 添加封装的路由
app.include_router(app1, prefix="/api1", tags=["一号封装接口"])
app.include_router(app2, prefix="/api2", tags=["二号封装接口"])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
