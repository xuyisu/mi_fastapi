from sqlalchemy import and_
from werkzeug.datastructures.structures import MultiDict
from apps.forms.user import UserRegisterForm, UserLoginForm
from apps.models.user import User
from config import db
from utils import R, regular, md5, jwts
from utils.utils import uid


# 注册用户
async def register(request):
    # 获取请求参数
    json_data = await request.json()
    # 表单验证
    form = UserRegisterForm(MultiDict(json_data))
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 密码存在是MD5加密
    password = form.password.data
    if password:
        form.password.data = md5.getPassword(password)

    # 表单数据赋值给对象
    user = User(**form.data)
    user.create_user = uid(request)
    # 插入数据
    user.save()
    # 返回结果
    return R.ok(msg="添加成功")


# 登录
async def login(request):
    # 获取请求参数
    json_data = await request.json()
    # 表单验证
    form = UserLoginForm(MultiDict(json_data))
    if not form.validate():
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)
    # 根据ID查询用户
    user_name = form.userName.data
    user = db.query(User).filter(and_(User.status == 1, User.user_name == user_name)).first()
    if not user:
        return R.failed("用户名或密码错误")
    if user.password != md5.getPassword(form.password.data):
        return R.failed("用户名或密码错误")
    payload = {"userName": user.user_name, "id": user.id, "email": user.email, "phone": user.phone}
    # jwt 方式
    key = jwts.create_token(payload)
    # key = utils.randomId()
    # 写入redis 用户id
    # await request.app.state.redis.set(key, user.to_json(), expire=60 * 60 * 24)
    user.password = None
    result = {"Authorization": key, "userInfo": user}
    return R.ok(data=result)


# 获取用户信息
async def getUser(request):
    return R.ok(data=request.jwt_user)


# 退出
async def logout(request):
    return R.ok()
