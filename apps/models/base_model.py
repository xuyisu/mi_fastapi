
from datetime import datetime

from sqlalchemy import Column, Integer, DATETIME, DateTime, Numeric, Date

from config.sqlalchemy import Base


# 对象转字典
def to_dict(self):
    # return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    # 等价于
    res = {}
    for c in self.__table__.columns:
        res[c.name] = getattr(self, c.name)


Base.to_dict = to_dict


# 基类模型
class base_model(Base):
    # 定义为抽象类
    __abstract__ = True
    # 默认字段
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    create_user = Column(Integer, default=0, comment="创建人")
    create_time = Column(DATETIME, default=datetime.now, comment="创建时间")
    update_user = Column(Integer, default=0, comment="更新人")
    update_time = Column(DATETIME, default=datetime.now, comment="更新时间")
    delete_flag = Column(Integer, default=0, comment="删除标识：0-未删除 1-已删除")

    # 自定义将返回实例对象转化为json
    def to_json(self):
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item

    # 对象转字典
    def to_dict(self):
        res = {}
        for col in self.__table__.columns:
            if isinstance(col.type, DateTime):  # 判断类型是否为DateTime
                if not getattr(self, col.name):  # 判断实例中该字段是否有值
                    value = ""
                else:  # 进行格式转换
                    value = getattr(self, col.name).strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(col.type, Date):  # 判断类型是否为Date
                if not getattr(self, col.name):  # 判断实例中该字段是否有值
                    value = ""
                else:  # 进行格式转换
                    value = getattr(self, col.name).strftime("%Y-%m-%d")
            elif isinstance(col.type, Numeric):  # 判断类型是否为Numeric
                value = float(getattr(self, col.name))  # 进行格式转换
            else:  # 剩余的直接取值
                value = getattr(self, col.name)
            res[col.name] = value
        return res