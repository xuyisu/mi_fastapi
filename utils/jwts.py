import datetime

import jwt

from jwt import exceptions

# JWT加密盐
JWT_SALT = "ds()udsjo@jlsdosjf)wjd_#(#)$"


# JWT加密
def create_token(payload, timeout=7200):
    # 声明类型，声明加密算法
    headers = {
        "type": "jwt",
        "alg": "HS256"
    }
    # 设置过期时间
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers)
    # 返回加密结果
    return result


# JWT解密
def parse_payload(token):
    # 自定义对象
    message = {"code": 0, "data": None, "msg": "操作成功"}
    try:
        # 进行解密
        verified_payload = jwt.decode(token, JWT_SALT, algorithms=['HS256'])
        # 返回结果
        message['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        message['code'] = -1
        message['msg'] = "token已失效"
    except jwt.DecodeError:
        message['code'] = -1
        message['msg'] = "token认证失败"
    except jwt.InvalidTokenError:
        message['code'] = -1
        message['msg'] = "非法的token"
    return message
