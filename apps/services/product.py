from fastapi.logger import logger
from apps.constants.message import PAGE_LIMIT
from apps.models.product import Product
from config import db
from utils import R


# 商品列表
async def page_list(request):
    try:
        # 页码
        page = int(request.query_params.get("current", 1))
        # 每页数
        limit = int(request.query_params.get("size", PAGE_LIMIT))
        category_id = request.query_params.get("categoryId")
        # # 实例化查询对象
        query = db.query(Product).filter(Product.category_id == category_id, Product.delete_flag == 0)
        # 排序
        query = query.order_by(Product.id.desc())
        # 记录总数
        count = query.count()
        # 分页查询
        user_list = query.limit(limit).offset((page - 1) * limit).all()
        records = []
        # 遍历数据源
        if len(user_list) > 0:
            for item in user_list:
                # 对象
                data = item.to_dict()
                # 加入数组
                records.append(data)
        result = {
            "total": count,
            "records": records,
            "current": page,
            "size": limit,
        }
        # 返回结果
        return R.ok(data=result)
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


async def get_product_detail(product_id):
    try:
        product_resp = db.query(Product).filter(Product.product_id == product_id, Product.delete_flag == 0).first()
        if not product_resp:
            return R.failed(msg="该商品已下架或删除")
        return R.ok(data=Product.to_dict(product_resp))
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()
