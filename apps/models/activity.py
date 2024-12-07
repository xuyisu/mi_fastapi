from sqlalchemy import Column, String, Integer, BigInteger,DateTime

from apps.models.base_db import base_db
from apps.models.base_model import base_model

# 活动模型
class Activity(base_model, base_db):
    # 设置表名
    __tablename__ = "activity"
    # 活动id
    activity_id = Column(BigInteger, default=0, nullable=False, comment='活动id')
    # 活动名称
    name = Column(String(60), default='', comment='活动名称')
    # 活动状态
    status = Column(Integer, default=0, nullable=False, comment='活动状态')
    # 活动图片地址
    main_image = Column(String(100), default='', comment='活动图片地址')
    # 开始时间
    start_time = Column(DateTime, comment='开始时间')
    # 结束时间
    end_time = Column(DateTime, comment='结束时间')



def __str__(self):
        return "活动{}".format(self.id)