from sqlalchemy import Column, String, Integer
from datetime import datetime
from apps.models.base_db import base_db
from apps.models.base_model import base_model
import json

# 用户模型
class User(base_model, base_db):
    # 设置表名
    __tablename__ = "user"
    # 启用状态
    status = Column(Integer, nullable=False, comment="启用状态 1 启用 0 禁用")
    # 用户名
    user_name = Column(String(50), default='', nullable=False, comment='用户名')
    # 邮箱'
    email = Column(String(50), default='', nullable=False, comment='邮箱')
    # 手机号
    phone = Column(String(20), unique=True, default='', nullable=False, comment='手机号')
    # 密码
    password = Column(String(100), default='', nullable=False, comment='密码')

    def __init__(self, id=None, create_time=None, update_time=None, create_user=0, update_user=0,
                 delete_flag=0, status=1, userName='', email='', phone='', password=''):
        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.create_user = create_user
        self.update_user = update_user
        self.delete_flag = delete_flag
        self.status = status
        self.user_name = userName
        self.email = email
        self.phone = phone
        self.password = password

    def to_json(self):
        # 将日期时间对象转换为字符串
        data = {
            'id': self.id,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'create_user': self.create_user,
            'update_user': self.update_user,
            'delete_flag': self.delete_flag,
            'status': self.status,
            'user_name': self.user_name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password
        }
        return json.dumps(data, default=str)  # 使用default=str来处理可能的非标准类型，但这里其实不需要

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        # 将字符串转换回日期时间对象（如果需要的话）
        create_time = datetime.fromisoformat(data['create_time']) if data['create_time'] else None
        update_time = datetime.fromisoformat(data['update_time']) if data['update_time'] else None

        return User(
            id=data['id'],
            create_time=create_time,
            update_time=update_time,
            create_user=data['create_user'],
            update_user=data['update_user'],
            delete_flag=data['delete_flag'],
            status=data['status'],
            user_name=data['user_name'],
            email=data['email'],
            phone=data['phone'],
            password=data['password']
        )

    def __str__(self):
        return "用户{}".format(self.id)