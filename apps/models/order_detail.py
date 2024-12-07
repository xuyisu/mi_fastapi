from sqlalchemy import Column, String, Integer, BigInteger, DECIMAL, DateTime

from apps.models.base_db import base_db
from apps.models.base_model import base_model


# 订单明细模型
class OrderDetail(base_model, base_db):
    # 设置表名
    __tablename__ = "order_detail"
    # 订单编号
    order_no = Column(String(60), default='', nullable=False, comment='订单编号')
    # 订单明细编号
    order_detail_no = Column(String(60), default='', nullable=False, comment='订单明细编号')
    # 活动id
    activity_id = Column(BigInteger, default=0, nullable=True, comment='活动id')
    # 活动名称
    activity_name = Column(String(50), default='', nullable=True, comment='活动名称')
    # 活动图片地址
    activity_main_image = Column(String(100), default='', nullable=True, comment='活动图片地址')
    # 商品id
    product_id = Column(BigInteger, default=0, nullable=False, comment='商品id')
    # 商品名称
    product_name = Column(String(50), default='', nullable=False, comment='商品名称')
    # 商品图片地址
    product_main_image = Column(String(100), default='', nullable=False, comment='商品图片地址')
    # 单价
    current_unit_price = Column(DECIMAL(20, 2), default=0.00, nullable=True, comment='单价')
    # 数量
    quantity = Column(Integer, default=0, nullable=True, comment='数量')
    # 总价
    total_price = Column(DECIMAL(20, 2), default=0.00, nullable=True, comment='总价')
    # 购买人id
    user_id = Column(BigInteger, default=0, nullable=False, comment='购买人id')
    # 订单状态
    status = Column(Integer, default=0, nullable=False, comment='订单状态')
    # 状态描述
    status_desc = Column(String(20), default='', nullable=True, comment='状态描述')
    # 取消时间
    cancel_time = Column(DateTime, nullable=True, comment='取消时间')
    # 取消原因
    cancel_reason = Column(Integer, default=0, nullable=True, comment='取消原因')
    # 发货时间
    send_time = Column(DateTime, nullable=True, comment='发货时间')
    # 签收时间
    receive_time = Column(DateTime, nullable=True, comment='签收时间')

    def __str__(self):
        return "订单明细{}".format(self.id)

    def __init__(self, create_time=None, update_time=None, create_user=0, update_user=0,
                 delete_flag=0, order_no='', order_detail_no='', product_id=0, product_name='', product_main_image=''
                 , quantity=0, current_unit_price=0, status_desc='', total_price=0, user_id=0, status=0,
                 ):
        self.order_no = order_no,
        self.order_detail_no = order_detail_no,
        self.product_id = product_id,
        self.product_name = product_name,
        self.product_main_image = product_main_image,
        self.quantity = quantity,
        self.current_unit_price = current_unit_price,
        self.status = status,
        self.status_desc = status_desc,
        self.total_price = total_price,
        self.user_id = user_id,
        self.create_user = user_id

    def to_dict(self):
        return {
            "orderNo": self.order_no,
            "orderDetailNo": self.order_detail_no,
            "productId": self.product_id,
            "productName": self.product_name,
            "productMainImage": self.product_main_image,
            "quantity": self.quantity,
            "currentUnitPrice": self.current_unit_price,
            "status": self.status,
            "statusDesc": self.status_desc,
        }