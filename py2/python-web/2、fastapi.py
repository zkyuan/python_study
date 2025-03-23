"""
 * @author: zkyuan
 * @date: 2025/3/23 15:31
 * @description: fastapi-demo
"""

from fastapi import FastAPI

# 实例化
app = FastAPI()


@app.post("/update")
async def update():
    return "messages:200, ok!"


@app.get("/get")
async def get():
    return "success"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)

# 在postman调用接口访问
# 接口文档  http://localhost:8080/docs
# 命令运行：uvicorn 文件名:app --reload --port=8080 --host=127.0.0.1
