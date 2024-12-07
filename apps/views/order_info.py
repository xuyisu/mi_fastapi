from fastapi import APIRouter

from starlette.requests import Request

from apps.services import order_info

# 创建路由
router = APIRouter()


# 订单列表
@router.get('/pages', summary='订单列表')
async def page_list(request: Request):
    # 调用查询用户详情服务方法
    data = await order_info.page_list(request)
    # 返回结果
    return data


# 订单列表
@router.post('/create', summary='创建订单')
async def create(request: Request):
    # 调用查询用户详情服务方法
    data = await order_info.create_order(request)
    # 返回结果
    return data


# 订单列表
@router.post('/pay', summary='订单列表')
async def pay(request: Request):
    # 调用查询用户详情服务方法
    data = await order_info.pay(request)
    # 返回结果
    return data


@router.get('/{order_no}', summary='查询订单明细')
async def order_detail(order_no, request: Request):
    # 调用添加用户服务
    result = await order_info.order_detail(order_no, request)
    # 返回结果
    return result


@router.put('/{order_no}', summary='取消订单')
async def order_detail(order_no, request: Request):
    # 调用添加用户服务
    result = await order_info.cancel_order(order_no, request)
    # 返回结果
    return result
