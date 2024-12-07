from wtforms import StringField, Form
from wtforms.validators import DataRequired


# 添加购物车表单验证
class CartAddForm(Form):
    # 商品id
    productId = StringField(
        label='商品id',
        validators=[
            DataRequired(message='商品id不能为空')
        ]
    )
