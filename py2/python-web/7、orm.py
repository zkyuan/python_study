"""
 * @author: zkyuan
 * @date: 2025/3/23 22:53
 * @description: ORM操作对象关系映射器 ---> Tortoise框架
"""
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from account.models import Account
# pip install passlib[bcrypt] 加密工具
from passlib.context import CryptContext

app = FastAPI()

# 数据模型
class AccountForm(BaseModel):
    username: str
    password: str

# 查询用户名是否已存在，框架中模型封装的方法
async def is_username_existed(username: str):
    return await Account.get_or_none(username=username)

# 密码加密
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

@app.post("/signup")
async def signuo(account: AccountForm):

    # user = account.username
    # psw = account.password
    user = await is_username_existed(account.username)

    if user:
        # 存在
        raise HTTPException(status_code=409, detail="用户名已存在")

    hashed_password = get_password_hash(account.password)

    try:
        result = await Account.create(username=account.username, hashed_password=hashed_password)
        print(result.username)
        return Response(status_code=201, content="创建成功")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    import uvicorn

    # uvicorn.run(app, host="127.0.0.1", port=8080)
    # 加上一下参数，app要写成 文件:app 的形式
    uvicorn.run("7、orm:app", host="127.0.0.1", port=8080, reload=True)
