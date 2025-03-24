"""
 * @author: zkyuan
 * @date: 2025/3/24 10:54
 * @description: 模型层
"""
from tortoise import fields  # 用于申明数据库字段
from tortoise.models import Model  # 用于基础数据库模型

class Account(Model):
    id = fields.IntField(primary_key=True, generated=True)
    username = fields.CharField(null=False, unique=True, max_length=32, description="用户名")
    hashed_password = fields.CharField(null=False, description="密码")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:  # 数据表的配置信息
        table_description = "Account账号信息"
        table = "account"
