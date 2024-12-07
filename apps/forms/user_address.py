from wtforms import StringField, Form
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length



# 用户表单验证
class UserAddressForm(Form):
    # 收货人
    receiveName = StringField(
        label='收货人',
        validators=[
            DataRequired(message='收货人不能为空'),
            Length(max=60, message='收货人不能为空不得超过60个字符')
        ]
    )
    # 联系号码
    receivePhone = StringField(
        label='联系号码',
        validators=[
            DataRequired(message='联系号码不能为空'),
            Length(max=20, message='联系号码长度不得超过20个字符')
        ]
    )

    # 省份
    province = StringField(
        label='省份',
        validators=[
            DataRequired(message='省份不能为空'),
            Length(max=20, message='省份长度不得超过20个字符')
        ]
    )
    # 省份编码
    provinceCode = StringField(
        label='省份编码',
        validators=[
            DataRequired(message='省份编码不能为空'),
            Length(max=20, message='省份编码长度不得超过20个字符')
        ]
    )

    # 城市
    city = StringField(
        label='城市',
        validators=[
            DataRequired(message='城市不能为空'),
            Length(max=20, message='城市长度不得超过20个字符')
        ]
    )
    # 城市编码
    cityCode = StringField(
        label='城市编码',
        validators=[
            DataRequired(message='城市编码不能为空'),
            Length(max=20, message='城市编码长度不得超过20个字符')
        ]
    )
    # 区
    area = StringField(
        label='区',
        validators=[
            DataRequired(message='区不能为空'),
            Length(max=20, message='区长度不得超过20个字符')
        ]
    )
    # 区编码
    areaCode = StringField(
        label='区编码',
        validators=[
            DataRequired(message='区编码不能为空'),
            Length(max=20, message='区编码长度不得超过20个字符')
        ]
    )

    # 详细地址
    street = StringField(
        label='详细地址',
        validators=[
            DataRequired(message='详细地址不能为空'),
            Length(max=100, message='详细地址长度不得超过100个字符')
        ]
    )

    # 默认标志
    # defaultFlag = IntegerField(
    #     label='默认标志',
    #     validators=[
    #         DataRequired(message='默认标志不能为空'),
    #         Length(min=0, max=1, message='默认标志输入0和1')
    #     ]
    # )

    # 邮编
    postalCode = StringField(
        label='详细地址',
        validators=[
            DataRequired(message='邮编不能为空'),
            Length(max=10, message='邮编长度不得超过10个字符')
        ]
    )

    # 地址标签
    # addressLabel = IntegerField(
    #     label='地址标签',
    #     validators=[
    #         DataRequired(message='地址标签不能为空'),
    #         Length(min=0, max=127, message='地址标签输入0和1')
    #     ]
    # )
