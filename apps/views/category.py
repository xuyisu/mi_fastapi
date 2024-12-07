from fastapi import APIRouter

from starlette.requests import Request

from apps.services import category

# 创建路由
router = APIRouter()


# 商品列表
@router.get('/list', summary='类目列表')
async def category_list(request: Request):
    data = await category.list(request)
    # 返回结果
    return data
