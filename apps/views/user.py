from fastapi import APIRouter

from starlette.requests import Request

from apps.services import user

# 创建路由
router = APIRouter()



# 查询用户详情
@router.post('/login', summary='用户注册')
async def login(request: Request):
    # 调用查询用户详情服务方法
    data = await user.login(request)
    # 返回结果
    return data


# 添加用户
@router.post('/register', summary='注册用户')
async def register(request: Request):
    # 调用添加用户服务
    result = await user.register(request)
    # 返回结果
    return result


# 更新用户
@router.get('/getUser', summary='获取用户信息')
async def get_user(request: Request):
    # 调用更新用户服务方法
    result = await user.getUser(request)
    # 返回结果
    return result


@router.post('/logout', summary='登出')
async def logout(request: Request):
    # 调用查询用户详情服务方法
    data = await user.logout(request)
    # 返回结果
    return data
