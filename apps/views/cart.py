from fastapi import APIRouter

from starlette.requests import Request

from apps.services import cart

# 创建路由
router = APIRouter()


# 购物车列表
@router.get('/list', summary='购物车列表')
async def page_list(request: Request):
    # 调用查询用户详情服务方法
    data = await cart.page_list(request)
    # 返回结果
    return data


# 添加购物车
@router.post('/add', summary='添加购物车')
async def create(request: Request):
    # 调用查询用户详情服务方法
    data = await cart.add_cart(request)
    # 返回结果
    return data


# 删除购物车
@router.delete('/{product_id}', summary='删除购物车')
async def delete_cart(product_id, request: Request):
    # 调用添加用户服务
    result = await cart.delete_cart(product_id, request)
    # 返回结果
    return result


# 全选
@router.put('/selectAll', summary='全选')
async def select_all(request: Request):
    # 调用查询用户详情服务方法
    data = await cart.select_all(request)
    # 返回结果
    return data


# 非全选
@router.put('/unSelectAll', summary='非全选')
async def un_select_all(request: Request):
    # 调用查询用户详情服务方法
    data = await cart.un_select_all(request)
    # 返回结果
    return data


# 修改购物车数量
@router.put('/{product_id}', summary='修改购物车数量')
async def update_cart(product_id, request: Request):
    # 调用添加用户服务
    result = await cart.update_cart(product_id, request)
    # 返回结果
    return result

    return data


# 统计总数
@router.get('/sum', summary='统计总数')
async def pay(request: Request):
    # 调用查询用户详情服务方法
    data = await cart.sum_cart(request)
    # 返回结果
    return data
