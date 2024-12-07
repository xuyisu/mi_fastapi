from sqlalchemy import Column, String, Integer, BigInteger

from apps.models.base_db import base_db
from apps.models.base_model import base_model

# 类目模型
class Category(base_model, base_db):
    # 设置表名
    __tablename__ = "category"
    # 父id
    parent_id = Column(BigInteger, default=0, nullable=True, comment='父id')
    # 名称
    name = Column(String(100), default='', nullable=True, comment='名称')
    # 启用禁用状态 1启用 0禁用
    status = Column(Integer, default=0, nullable=True, comment='启用禁用状态 1启用 0禁用')
    # 排序
    sort_order = Column(Integer, default=0, nullable=True, comment='排序')



def __str__(self):
        return "类目{}".format(self.id)