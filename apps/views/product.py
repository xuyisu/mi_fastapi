from fastapi import APIRouter

from starlette.requests import Request

from apps.services import product

# 创建路由
router = APIRouter()


# 商品列表
@router.get('/pages', summary='商品列表')
async def page_list(request: Request):
    # 调用查询用户详情服务方法
    data = await product.page_list(request)
    # 返回结果
    return data


# 查询商品列表
@router.get('/{productId}', summary='查询商品列表')
async def get_product_detail(productId):
    # 调用添加用户服务
    result = await product.get_product_detail(productId)
    # 返回结果
    return result
