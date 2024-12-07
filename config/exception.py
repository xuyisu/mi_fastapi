# 登录认证异常处理类
class AuthorizationException(Exception):
    def __init__(self, code: int, msg: str):
        self.msg = msg
        self.code = code
