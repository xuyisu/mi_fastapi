
from wtforms import StringField, Form
from wtforms.validators import DataRequired, Length, ValidationError

from apps.models.user import User

from config import db


# 用户表单验证
class UserRegisterForm(Form):

    # 手机号
    phone = StringField(
        label='手机号',
        validators=[
            DataRequired(message='手机号不能为空'),
            Length(max=30, message='手机号长度不得超过30个字符')
        ]
    )
    # 邮箱
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired(message='邮箱不能为空'),
            Length(max=30, message='邮箱长度不得超过30个字符')
        ]
    )

    # 登录账号
    userName = StringField(
        label='登录账号',
        validators=[
            DataRequired(message='登录账号不能为空'),
            Length(max=30, message='登录账号长度不得超过30个字符')
        ]
    )
    # 登录密码
    password = StringField(
        label='登录密码',
        validators=[
            Length(min=6, max=30, message='登录密码长度不得超过30个字符')
        ]
    )




# 用户登录表单
class UserLoginForm(Form):
    # 登录账号
    userName = StringField(
        label='登录账号',
        validators=[
            DataRequired(message='登录账号不能为空'),
            Length(max=30, message='登录账号长度不得超过30个字符')
        ]
    )
    # 登录密码
    password = StringField(
        label='登录密码',
        validators=[
            Length(min=6, max=255, message='登录密码长度不得超过255个字符')
        ]
    )
