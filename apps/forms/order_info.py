from wtforms import StringField, Form
from wtforms.validators import DataRequired


# 订单表单验证
class OrderCreateForm(Form):
    # 地址id
    addressId = StringField(
        label='地址id',
        validators=[
            DataRequired(message='地址id不能为空')
        ]
    )


class OrderPayForm(Form):
    # 订单编号
    orderNo = StringField(
        label='订单编号',
        validators=[
            DataRequired(message='订单编号不能为空')
        ]
    )
