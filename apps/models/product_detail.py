from sqlalchemy import Column, BigInteger, JSON

from apps.models.base_db import base_db
from apps.models.base_model import base_model

# 商品明细模型
class ProductDetail(base_model, base_db):
    # 设置表名
    __tablename__ = "product_detail"
    # 商品id
    product_id = Column(BigInteger, nullable=False, comment='商品id')
    # 商品详情
    detail = Column(JSON, nullable=True, comment='商品详情')
    # 商品参数
    param = Column(JSON, nullable=True, comment='商品参数')
    # 轮播图片
    rotation = Column(JSON, nullable=True, comment='轮播图片')

    def __str__(self):
            return "商品明细{}".format(self.id)