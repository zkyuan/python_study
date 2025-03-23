"""
 * @author: zkyuan
 * @date: 2025/3/23 15:52
 * @description:
 路径操作装饰器 get post put delete update
"""

from fastapi import FastAPI

# 实例化
app = FastAPI()


@app.post("/post",
          tags=["这是post接口标题"],
          summary="接口测试语法",
          description="这是接口的详情信息",
          response_description="响应详细信息",
          deprecated=False,  # 是否废弃
          )
async def post():
    return "post"


@app.get("/get")
async def get():
    return "get"


@app.put("/put")
async def put():
    return "put"


@app.delete("/delete")
async def delete():
    return "delete"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
