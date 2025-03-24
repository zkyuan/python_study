from datetime import datetime, timezone, timedelta

import jwt
from fastapi import FastAPI, Depends, requests, Body, Path, Query
from fastapi.security import OAuth2PasswordBearer
from requests import Request

# 命令行输入 openssl rand -hex 32 生成密钥
SECRET_KEY = "c0f46cf953adbd6f29cf9d9a83604ccddbf25ef4425b9b65fd723db08122c578"
algorithm = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    encoded_jwt = jwt.encode(
        to_encode,  # 通过token传输的内容
        SECRET_KEY,  # JWT签名密钥
        algorithm=algorithm,  # JWT算法
    )

    return encoded_jwt


# 获取token，解码。 从/login请求的请求体的Authorization获取字段token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# 解码
def get_user_token(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[algorithm],  # 解密算法
    )
    return payload


def get_extra_param(data: str = Query()):
    payload = {

    }
    return dict


def verify_token(token):
    pass


app = FastAPI()


@app.get("/send_token")
async def send_token():
    data = {"username": "zky"}
    token = create_token(data)
    print(token)
    return token


# 获取token
@app.get("/get_token")
async def get_token(data=Depends(get_user_token)):
    return data

# 填写 Authorization = Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InpreSIsImV4cCI6MTc0Mjc5ODMxNH0.BtmfXKBvkx43feWstic1udePFLf8rFMXvUdOXdte9tI


# 没跑通
# @app.post("/use_token/{path_param}")
# async def use_token(
#     data=Depends(get_user_token),
#     path_param: str = Path(...),
#     query_param: str = Query(...),
#     extra_params: str = Body(...),
#     extra_param=Depends(get_extra_param)
# ):
#     return {
#         "data": data,
#         "path_param": path_param,
#         "query_param": query_param,
#         "extra_params": extra_params,
#         "extra_param": extra_param
#     }



if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app, host="127.0.0.1", port=8080)
    # 加上一下参数，app要写成 文件:app 的形式
    uvicorn.run("test:app", host="127.0.0.1", port=8080, reload=True)
