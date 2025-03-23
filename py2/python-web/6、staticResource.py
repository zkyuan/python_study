"""
 * @author: zkyuan
 * @date: 2025/3/23 15:52
 * @description: 暴露静态资源给外部访问
"""
import os
from typing import List

from fastapi import FastAPI, Form, File, UploadFile, Request
from pydantic import BaseModel, Field, validator
from fastapi.staticfiles import StaticFiles

# 实例化
app = FastAPI()

# 暴露静态资源给外部访问
# directory与项目目录下的statics文件夹名保持一致
app.mount("/xxx", StaticFiles(directory="statics"))

if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app, host="127.0.0.1", port=8080)
    # 加上一下参数，app要写成 文件:app 的形式
    uvicorn.run("6、staticResource:app", host="127.0.0.1", port=8080, reload=True)
