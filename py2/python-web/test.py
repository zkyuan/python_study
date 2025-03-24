from contextlib import asynccontextmanager

from fastapi import FastAPI
from database.tortoise import register_mysql0

app = FastAPI()

@asynccontextmanager
async def tai_init(app: FastAPI):
    async with register_mysql0(app):
        yield print("mysql生命周期")

    print('tai关闭了')