"""
 * @author: zkyuan
 * @date: 2025/3/24 9:17
 * @description: tortoise-orm
"""
# pip install fastapi[all]
# pip install tortoise-orm[aiomysql]

from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise.contrib.fastapi import RegisterTortoise
from tortoise import connection, connections

MYSQL_HOST = ""  # 数据库主机ip
MYSQL_PORT = ""  # 数据库端口
MYSQL_USER = ""  # 数据库用户名
MYSQL_PASSWORD = ""  # 数据库密码
MYSQL_DATABASE = ""  # 数据库名

# 数据库模型类，封装数据库表实体
TORTOISE_MODELS = ['account.models']

# Tortoise ORM 的mysql连接配置
TORTOISE_CONFIG = {
    'connections': {
        # 字典格式
        'default': {
            'engine': 'tortoise.backends.mysql',  # 要连接的数据库类型
            'credentials': {  # 登录凭证
                'host': MYSQL_HOST,
                'port': MYSQL_PORT,
                'user': MYSQL_USER,
                'password': MYSQL_PASSWORD,
                'database': MYSQL_DATABASE,
            }
        },
        # url连接形式
        # 'second': 'mysql://user:password@MYSQL_HOST:MYSQL_PORT/MYSQL_DATABASE',
    },

    'apps': {
        'tai_models': {  # tai_models是当前数据库前缀，在数据模型的类中使用到
            'models': TORTOISE_MODELS,  # 加载的模型
            'default_connection': 'default',  # 需要使用哪个连接配置
        },
        # 'tai_models2': {
        #     'models': TORTOISE_MODELS_2,
        #     'default_connection': 'second',
        # },

    },
    'use_tz': False,  # 不使用默认时区
    'timezone': 'Asia/Shanghai',  # 设置时区
}

@asynccontextmanager
async def register_mysql0(app: FastAPI):
    try:
        async with RegisterTortoise(
                app,
                config=TORTOISE_CONFIG,
                generate_schemas=True # 建立连接时，根据数据模型来表示数据表
        ):
            yield print("mysql连接成功")
            await connections.close_all()
            print("mysql数据库连接已关闭")
    except Exception as e:
        print(e)