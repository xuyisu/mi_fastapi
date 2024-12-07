from config import db


# 模型基类方法
class base_db:
    # 定义为抽象类
    __abstract__ = True

    # 添加一条数据，对象方法
    def save(self):
        # 插入记录ID
        rowId = 0
        try:
            db.add(self)
            db.commit()
            rowId = self.id
        except:
            # 事务回滚
            db.rollback()
            raise
        finally:
            # 关闭连接
            db.close()
            # 返回插入ID
            return rowId

    # 添加多条数据，静态方法
    @staticmethod
    def save_all(*args):
        try:
            db.add_all(args)
            db.commit()
        except:
            db.rollback()
            db.close()
        finally:
            db.close()

    # 删除数据
    def delete(self):
        try:
            db.delete(self)
            db.commit()
            return True
        except:
            db.rollback()
            db.close()
            return False
        finally:
            db.close()