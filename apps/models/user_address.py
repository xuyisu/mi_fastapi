from sqlalchemy import Column, String, Integer, BigInteger

from apps.models.base_db import base_db
from apps.models.base_model import base_model


# 用户地址模型
class UserAddress(base_model, base_db):
    # 设置表名
    __tablename__ = "user_address"
    # 地址id
    address_id = Column(BigInteger, default=0, nullable=False, comment='地址id')
    # 默认标志
    default_flag = Column(Integer, default=0, nullable=True, comment='默认标志')
    # 收货人
    receive_name = Column(String(60), default='', nullable=False, comment='收货人')
    # 联系号码
    receive_phone = Column(String(20), default='', nullable=False, comment='联系号码')
    # 省份
    province = Column(String(20), default='', nullable=False, comment='省份')
    # 省份编码
    province_code = Column(String(10), default='', nullable=False, comment='省份编码')
    # 城市
    city = Column(String(20), default='', nullable=False, comment='城市')
    # 城市编码
    city_code = Column(String(10), default='', nullable=False, comment='城市编码')
    # 区
    area = Column(String(20), default='', nullable=False, comment='区')
    # 区编码
    area_code = Column(String(10), default='', nullable=False, comment='区编码')
    # 详细地址
    street = Column(String(100), default='', nullable=True, comment='详细地址')
    # 邮编
    postal_code = Column(String(10), default='', nullable=True, comment='邮编')
    # 用户id
    address_label = Column(Integer, default=0, nullable=True, comment='地址标签')

    def __str__(self):
        return "用户地址{}".format(self.id)

    def __init__(self, create_time=None, update_time=None, create_user=0, update_user=0,
                 delete_flag=0, addressId=None, defaultFlag=0, receiveName='',
                 receivePhone='', province='', provinceCode='', city='', cityCode='', area='',
                 areaCode='', street='', postalCode='', addressLabel=0):
        self.id = None
        self.create_time = create_time
        self.update_time = update_time
        self.create_user = create_user
        self.update_user = update_user
        self.delete_flag = delete_flag
        self.address_id = addressId
        self.default_flag = defaultFlag
        self.receive_name = receiveName
        self.receive_phone = receivePhone
        self.province = province
        self.province_code = provinceCode
        self.city = city
        self.city_code = cityCode
        self.area = area
        self.area_code = areaCode
        self.street = street
        self.postal_code = postalCode
        self.address_label = addressLabel




    def to_dict(self):
        # 使用字典推导式来生成字典
        return {
            'id': self.id,
            'addressId': self.address_id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            'createUser': self.create_user,
            'updateUser': self.update_user,
            'deleteFlag': self.delete_flag,
            'defaultFlag': self.default_flag,
            'receiveName': self.receive_name,
            'receivePhone': self.receive_phone,
            'province': self.province,
            'provinceCode': self.province_code,
            'city': self.city,
            'cityCode': self.city_code,
            'area': self.area,
            'areaCode': self.area_code,
            'street': self.street,
            'postalCode': self.postal_code,
            'addressLabel': self.address_label,
        }
