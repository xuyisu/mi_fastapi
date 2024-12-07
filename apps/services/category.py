from fastapi.logger import logger

from apps.models.category import Category
from config import db
from utils import R


# 商品列表
async def list(request):
    try:
        # # 实例化查询对象
        query = db.query(Category).filter(Category.delete_flag == 0)
        # 排序
        query = query.order_by(Category.id.desc())
        # 分页查询
        user_list = query.all()
        records = []
        # 遍历数据源
        if len(user_list) > 0:
            for item in user_list:
                # 对象
                data = item.to_dict()
                # 加入数组
                records.append(data)
        # 返回结果
        return R.ok(data=records)
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()