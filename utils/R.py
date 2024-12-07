"""
    返回结果
    code 类型码 200-成功 500失败
    data 数据
    msg 提示信息
    kwargs 其他参数
"""


# 返回成功
def ok(data=None, msg="操作成功", code=200, **kwargs):
    result = {"code": code, "data": data, "msg": msg}
    if kwargs:
        result.update(kwargs)
    return result


# 返回失败
def failed(msg="操作成功", code=500, **kwargs):
    result = {"code": code, "data": None, "msg": msg}
    if kwargs:
        result.update(kwargs)
    return result
