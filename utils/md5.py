import hashlib


# 密码MD5加密
def getPassword(password):
    encry = hashlib.md5()  # 实例化md5
    encry.update(password.encode())  # 字符串字节加密
    return encry.hexdigest()  # 字符串加密