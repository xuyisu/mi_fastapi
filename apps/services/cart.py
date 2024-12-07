import json
from datetime import datetime

from fastapi import APIRouter
from werkzeug.datastructures import MultiDict

from apps.constants.constants import ONE
from apps.enums.enable_status_enum import EnableStatus
from apps.forms.cart import CartAddForm
from apps.models.activity import Activity
from apps.models.cart import Cart
from apps.models.product import Product
from config import db
from utils import R
from fastapi.logger import logger

# 创建路由
router = APIRouter()


# 购物车列表
async def page_list(request):
    user_id = request.jwt_user.id
    # # 实例化查询对象
    query = db.query(Cart).filter(Cart.create_user == user_id, Cart.delete_flag == 0)
    # 排序
    query = query.order_by(Cart.id.desc())
    # 分页查询
    cart_list = query.all()
    # 实例化结果
    records = []
    # 遍历数据源
    if len(cart_list) > 0:
        for item in cart_list:
            # 对象
            data = item.to_dict()
            # 加入数组
            records.append(data)
    # 返回结果
    return R.ok(data=records)


# 添加购物车
async def add_cart(request):
    try:
        # 接收请求参数
        json_data = await request.json()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 表单验证
        user_id = request.jwt_user.id
        form = CartAddForm(MultiDict(json_data))
        if form.validate():
            # 获取数据
            product_id = form.productId.data.strip()
            product = db.query(Product).filter(Product.product_id == product_id,
                                               Product.status == EnableStatus.ENABLE.value).first()
            if not product:
                return R.failed("当前商品已下架或删除")
            # 查询当前商品是否已存在购物车
            cart_exist = db.query(Cart).filter(Cart.delete_flag == 0, Cart.user_id == user_id,
                                               Cart.product_id == product_id).first()
            if not cart_exist:
                cart_create = Cart()
                cart_create.product_id = product_id
                cart_create.activity_id = product.activity_id
                cart_create.create_user = user_id
                cart_create.user_id = user_id
                cart_create.product_subtitle = product.sub_title
                cart_create.product_unit_price = product.price
                cart_create.product_main_image = product.main_image
                cart_create.product_name = product.name
                cart_create.quantity = ONE
                cart_create.product_total_price = cart_create.product_unit_price * cart_create.quantity
                activity = db.query(Activity).filter(Activity.activity_id == product.activity_id).first()
                if activity:
                    cart_create.activity_name = activity.name
                cart_create.save()
            else:
                cart_exist.update_time = None
                cart_exist.update_user = user_id
                cart_exist.quantity = cart_exist.quantity + ONE
                cart_exist.product_total_price = cart_exist.product_unit_price * cart_exist.quantity
                cart_exist.save()
        return await sum_cart(request)
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


# 改变购物车数量
async def update_cart(product_id, request):
    try:
        # 接收请求参数
        json_data = await request.json()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        dict_data = MultiDict(json_data)
        user_id = request.jwt_user.id
        product = db.query(Product).filter(Product.product_id == product_id,
                                           Product.status == EnableStatus.ENABLE.value).first()
        if not product:
            return R.failed("当前商品已下架或删除")
        cart_exist = db.query(Cart).filter(Cart.delete_flag == 0, Cart.user_id == user_id,
                                           Cart.product_id == product_id).first()
        if not cart_exist:
            return R.failed("购物车已不存在该商品")
        type = dict_data["type"]
        cart_exist.update_time = None
        if 1 == type:
            cart_exist.quantity = cart_exist.quantity + ONE
        else:
            if cart_exist.quantity <= ONE:
                return R.failed("购物车商品数量不足")
            else:
                cart_exist.quantity = cart_exist.quantity - ONE
        cart_exist.product_total_price = cart_exist.product_unit_price * cart_exist.quantity
        cart_exist.update_user = user_id
        cart_exist.save()
        return R.ok()
    except Exception as e:
        logger.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    finally:
        # 关闭连接
        db.close()


# 删除购物车商品
async def delete_cart(product_id, request):
    try:
        user_id = request.jwt_user.id
        cart_list = db.query(Cart).filter(Cart.delete_flag == 0, Cart.user_id == user_id,
                                          Cart.product_id == product_id).all()
        if len(cart_list) > 0:
            for item in cart_list:
                # 对象
                item.delete_flag = True
                item.update_user = user_id
                item.update_time = datetime.now()
                # 加入数组
                item.save()
        return R.ok()
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


# 全选
async def select_all(request):
    try:
        user_id = request.jwt_user.id
        cart_list = db.query(Cart).filter(Cart.delete_flag == 0, Cart.user_id == user_id, Cart.selected == 0).all()
        if len(cart_list) > 0:
            for item in cart_list:
                # 对象
                item.is_select = True
                item.update_user = user_id
                item.update_time = datetime.now()
                # 加入数组
                item.save()
        return R.ok()
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


# 取消全选
async def un_select_all(request):
    try:
        user_id = request.jwt_user.id
        cart_list = db.query(Cart).filter(Cart.delete_flag == 0, Cart.user_id == user_id, Cart.selected == ONE).all()
        if len(cart_list) > 0:
            for item in cart_list:
                # 对象
                item.is_select = False
                item.update_user = user_id
                item.update_time = datetime.now()
                # 加入数组
                item.save()
        return R.ok()
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


# 获取购物车数量
async def sum_cart(request):
    try:
        user_id = request.jwt_user.id
        count = db.query(Cart).filter(Cart.delete_flag == 0, Cart.user_id == user_id).count()
        return R.ok(data=count)
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()
