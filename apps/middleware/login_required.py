from starlette.requests import Request

from config.exception import AuthorizationException
from utils import R
from utils.jwts import parse_payload


# 登录验证中间件
async def login_required(request: Request):
    # 自定义忽略URL数组
    ignoreURL = ['/category/list', '/user/register', '/user/login', '/user/logout', '/product/pages',
                 '/product/:productId']
    # 请求地址
    requestURL = request.url.path
    if requestURL not in ignoreURL and request.method != "OPTIONS":
        # 从请求头中获取token值
        access_token = request.headers['Authorization']
        # 字符串替换
        access_token = access_token.replace('Bearer ', "")
        # JWT解密
        result = parse_payload(access_token)
        # 结果标识
        code = result['code']
        if code != 0:
            raise AuthorizationException(code=401, msg="登录过期")
        request.jwt_user = result['data']
        return True
