from sqlalchemy import Column, String, Integer, BigInteger, DECIMAL

from apps.models.base_db import base_db
from apps.models.base_model import base_model

# 商品信息
class Product(base_model, base_db):
    # 设置表名
    __tablename__ = "product"
    # 商品id
    product_id = Column(BigInteger, default=0, nullable=True, comment='商品id')
    # 品类id
    category_id = Column(BigInteger, default=0, nullable=True, comment='品类id')
    # 商品名称
    name = Column(String(60), default='', nullable=True, comment='商品名称')
    # 简要描述
    sub_title = Column(String(100), default='', nullable=True, comment='简要描述')
    # 商品图片地址
    main_image = Column(String(100), default='', nullable=True, comment='商品图片地址')
    # 子图片列表
    sub_images = Column(String(100), default='', nullable=True, comment='子图片列表')
    # 活动id
    activity_id = Column(BigInteger, nullable=True, comment='活动id')
    # 商品状态
    status = Column(Integer, default=1, nullable=False, comment='商品状态')
    # 商品单价
    price = Column(DECIMAL(20, 2), default=0.00, nullable=False, comment='商品单价')
    # 库存数
    stock = Column(Integer, default=0, nullable=False, comment='库存数')

    def __str__(self):
            return "商品{}".format(self.id)