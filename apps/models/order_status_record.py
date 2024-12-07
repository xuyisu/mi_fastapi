from sqlalchemy import Column, String, Integer, BigInteger, DateTime

from apps.models.base_db import base_db
from datetime import datetime

from config.sqlalchemy import Base


# 鼎泰状态记录模型
class OrderStatusRecord(Base, base_db):
    # 设置表名
    __tablename__ = "order_status_record"
    # 主键
    id = Column(BigInteger, autoincrement=True, primary_key=True, comment='主键')
    # 创建时间
    create_time = Column(DateTime, default=lambda: datetime.utcnow(), nullable=False, comment='创建时间')
    # 订单编号
    order_no = Column(String(60), default='', nullable=False, comment='订单编号')
    # 订单明细编号
    order_detail_no = Column(String(60), default='', nullable=False, comment='订单明细编号')
    # 商品id
    product_id = Column(BigInteger, default=0, nullable=False, comment='商品id')
    # 商品名称
    product_name = Column(String(60), default='', nullable=True, comment='商品名称')
    # 订单状态
    status = Column(Integer, default=0, nullable=False, comment='订单状态')
    # 状态描述
    status_desc = Column(String(60), default='', nullable=True, comment='状态描述')

    def __str__(self):
        return "订单状态记录{}".format(self.id)

    def __init__(self, create_time=None, update_time=None, create_user=0, update_user=0,
                 delete_flag=0, order_no='', order_detail_no='', product_id=0, product_name='',
                 status=0, status_desc=''):
        self.order_no = order_no,
        self.order_detail_no = order_detail_no,
        self.product_id = product_id,
        self.product_name = product_name,
        self.status = status,
        self.status_desc = status_desc
