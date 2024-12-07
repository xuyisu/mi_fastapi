from fastapi import APIRouter

from starlette.requests import Request

from apps.services import user_address

# 创建路由
router = APIRouter()


# 查询用户详情
@router.get('/pages', summary='地址列表')
async def pages(request: Request):
    # 调用查询用户详情服务方法
    data = await user_address.pages(request)
    # 返回结果
    return data


@router.post('/add', summary='添加地址')
async def add(request: Request):
    # 调用查询用户详情服务方法
    data = await user_address.add_address(request)
    # 返回结果
    return data


@router.get('/{addressId}', summary='地址查询')
async def get_address_detail(addressId):
    # 调用查询用户详情服务方法
    data = await user_address.get_address_detail(addressId)
    # 返回结果
    return data


@router.delete('/{addressId}', summary='地址删除')
async def delete(addressId, request: Request):
    # 调用查询用户详情服务方法
    data = await user_address.delete_address(addressId, request)
    # 返回结果
    return data


@router.put('/{addressId}', summary='地址更新')
async def update_address(request: Request, addressId):
    # 调用查询用户详情服务方法
    data = await user_address.update_address(request, addressId)
    # 返回结果
    return data
