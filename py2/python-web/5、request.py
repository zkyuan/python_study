"""
 * @author: zkyuan
 * @date: 2025/3/23 15:52
 * @description:request
"""
import os
from typing import List

from fastapi import FastAPI, Form, File, UploadFile, Request
from pydantic import BaseModel, Field, validator

# 实例化
app = FastAPI()


@app.post("/post",
          tags=["这是post接口标题"],
          summary="接口测试语法",
          description="这是接口的详情信息",
          response_description="响应详细信息",
          deprecated=False,  # 是否废弃
          )
async def post(request: Request):  # 请求体 前端json格式参数--->Data类型
    print(f"url:{request.url}")
    print(f"客户端ip:{request.client.host}")
    print(f"客户端代理:{request.headers.get("user-agent")}")
    print(f"cookies:{request.cookies}")
    # 以及其他属性
    return Messages(code=200, msg="success", data={"out": "UploadFile文件上传成功"})


# 请求返回的消息码
class Messages(BaseModel):
    code: int
    msg: str
    data: dict



if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app, host="127.0.0.1", port=8080)
    # 加上一下参数，app要写成 文件:app 的形式
    uvicorn.run("5、request:app", host="127.0.0.1", port=8080, reload=True)
