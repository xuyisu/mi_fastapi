from sqlalchemy import Column, String, Integer, BigInteger, DECIMAL, DateTime

from apps.models.base_db import base_db
from apps.models.base_model import base_model


# 订单模型
class OrderInfo(base_model, base_db):
    # 设置表名
    __tablename__ = "order_info"
    # 订单编号
    order_no = Column(String(60), default='', nullable=False, comment='订单编号')
    # 支付金额
    payment = Column(DECIMAL(20, 2), default=0.00, nullable=True, comment='支付金额')
    # 支付类型
    payment_type = Column(Integer, default=0, nullable=True, comment='支付类型')
    # 支付类型描述
    payment_type_desc = Column(String(20), default='', nullable=True, comment='支付类型描述')
    # 邮费
    postage = Column(DECIMAL(20, 2), default=0.00, nullable=True, comment='邮费')
    # 订单状态
    status = Column(Integer, default=0, nullable=False, comment='订单状态')
    # 状态描述
    status_desc = Column(String(20), default='', nullable=False, comment='状态描述')
    # 支付时间
    payment_time = Column(DateTime, nullable=True, comment='支付时间')
    # 地址id
    address_id = Column(BigInteger, default=0, nullable=True, comment='地址id')
    # 收货人
    receive_name = Column(String(50), default='', nullable=True, comment='收货人')
    # 联系号码
    receive_phone = Column(String(20), default='', nullable=True, comment='联系号码')
    # 省份
    province = Column(String(20), default='', nullable=True, comment='省份')
    # 城市
    city = Column(String(20), default='', nullable=True, comment='城市')
    # 区
    area = Column(String(20), default='', nullable=True, comment='区')
    # 详细地址
    street = Column(String(50), default='', nullable=True, comment='详细地址')
    # 邮编
    postal_code = Column(String(255), default='', nullable=True, comment='邮编')
    # 用户id
    user_id = Column(BigInteger, default=0, nullable=False, comment='购买人id')

    def __str__(self):
        return "订单{}".format(self.id)

    def __init__(self, create_time=None, update_time=None, create_user=0, update_user=0,
                 delete_flag=0, order_no='', address_id=0, province='', city='', area='', street='', postal_code='',
                 receive_name='', payment=0, payment_type=0, payment_type_desc='', receive_phone='',
                 status=0, status_desc='', user_id=0):
        self.order_no = order_no,
        self.address_id = address_id,
        self.province = province,
        self.city = city,
        self.area = area,
        self.street = street,
        self.postal_code = postal_code,
        self.receive_name = receive_name,
        self.payment = payment,
        self.payment_type = payment_type,
        self.payment_type_desc = payment_type_desc,
        self.receive_phone = receive_phone,
        self.status = status,
        self.status_desc = status_desc,
        self.create_user = user_id,
        self.update_user = user_id,
        self.user_id = user_id

    def to_dict(self):
        return {
            "id": self.id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            "orderNo": self.order_no,
            "addressId": self.address_id,
            "province": self.province,
            "city": self.city,
            "area": self.area,
            "street": self.street,
            "postalCode": self.postal_code,
            "receiveName": self.receive_name,
            "payment": self.payment,
            "paymentType": self.payment_type,
            "paymentTypeDesc": self.payment_type_desc,
            "receivePhone": self.receive_phone,
            "status": self.status,
            "statusDesc": self.status_desc,
            "userId": self.user_id,
            "details": []
        }

