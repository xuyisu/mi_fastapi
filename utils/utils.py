
from starlette.requests import Request
import uuid

from utils.jwts import parse_payload


# 获取用户ID
def uid(request: Request):
    # 从请求头中获取token值
    access_token = request.headers.get("Authorization", "")
    if access_token:
        # 字符串替换
        access_token = access_token.replace('Bearer ', "")
        # JWT解密
        result = parse_payload(access_token)
        # 结果标识
        code = result['code']
        if code != 0:
            return 0
        # 用户ID
        userId = int(result['data']['userId'])
        # 返回结果
        return userId
    else:
        return 0


# 判断变量类型的函数
def typeof(value):
    type = None
    if isinstance(value, int):
        type = "int"
    elif isinstance(value, str):
        type = "str"
    elif isinstance(value, float):
        type = "float"
    elif isinstance(value, list):
        type = "list"
    elif isinstance(value, tuple):
        type = "tuple"
    elif isinstance(value, dict):
        type = "dict"
    elif isinstance(value, set):
        type = "set"
    return type


# 返回变量类型
def getType(value):
    arr = {"int": "整数", "float": "浮点", "str": "字符串", "list": "列表", "tuple": "元组", "dict": "字典", "set": "集合"}
    vartype = typeof(value)
    if not (vartype in arr):
        return "未知类型"
    return arr[vartype]

# 生成随机字符串
def randomId():
     return str(uuid.uuid4())

