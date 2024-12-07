from sqlalchemy import Column, String, Integer, BigInteger,DECIMAL

from apps.models.base_db import base_db
from apps.models.base_model import base_model

# 购物车模型
class Cart(base_model, base_db):
    # 设置表名
    __tablename__ = "cart"
    # 用户id
    user_id = Column(BigInteger, default=0, nullable=True, comment='用户id')
    # 活动id
    activity_id = Column(BigInteger, default=0, nullable=True, comment='活动id')
    # 活动名称
    activity_name = Column(String(255), default='', nullable=True, comment='活动名称')
    # 商品id
    product_id = Column(BigInteger, default=0, nullable=False, comment='商品id')
    # 商品名称
    product_name = Column(String(255), default='', nullable=False, comment='商品名称')
    # 商品副标题
    product_subtitle = Column(String(255), default='', nullable=True, comment='商品简要描述')
    # 商品主图
    product_main_image = Column(String(255), default='', nullable=True, comment='商品图片地址')
    # 商品数量
    quantity = Column(Integer, default=0, nullable=False, comment='数量')
    # 商品单价
    product_unit_price = Column(DECIMAL(20, 2), default=0.00, nullable=False, comment='单价')
    # 是否已选择
    selected = Column(Integer, default=1, nullable=False, comment='是否已选择 1是 0 否')
    # 总价
    product_total_price = Column(DECIMAL(20, 2), default=0.00, nullable=False, comment='总价格')



    def __str__(self):
            return "购物车{}".format(self.id)