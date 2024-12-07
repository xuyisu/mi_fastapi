import time
from datetime import datetime
from zoneinfo import ZoneInfo

from werkzeug.datastructures import MultiDict

from apps.constants.constants import ONE
from apps.constants.message import PAGE_LIMIT
from fastapi.logger import logger

from apps.enums.enable_status_enum import EnableStatus
from apps.enums.order_status_enum import OrderStatus
from apps.forms.order_info import OrderCreateForm, OrderPayForm
from apps.models.activity import Activity
from apps.models.cart import Cart
from apps.models.order_detail import OrderDetail
from apps.models.order_info import OrderInfo
from apps.models.order_status_record import OrderStatusRecord
from apps.models.product import Product
from apps.models.user_address import UserAddress
from config import db
from utils import R, regular


# 订单列表
async def page_list(request):
    try:
        user_id = request.jwt_user.id
        # 页码
        page = int(request.query_params.get("current", 1))
        # 每页数
        limit = int(request.query_params.get("size", PAGE_LIMIT))
        # 实例化查询对象
        query = db.query(OrderInfo).filter(OrderInfo.user_id == user_id, OrderInfo.delete_flag == 0)
        # 排序
        query = query.order_by(OrderInfo.id.desc())
        # 记录总数
        count = query.count()
        # 分页查询
        user_list = query.limit(limit).offset((page - ONE) * limit).all()
        records = []
        # 遍历数据源
        if len(user_list) > 0:
            for item in user_list:
                # 对象
                data = item.to_dict()
                # 加入数组
                records.append(data)
        result = {
            "total": count,
            "records": records,
            "current": page,
            "size": limit,
        }
        # 返回结果
        return R.ok(data=result)
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


# 创建订单
async def create_order(request):
    session = db
    try:
        # 接收请求参数
        json_data = await request.json()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = MultiDict(json_data)
        # 表单验证
        form = OrderCreateForm(dict_data)
        if not form.validate():
            # 获取错误描述
            err_msg = regular.get_err(form)
            # 返回错误信息
            return R.failed(msg=err_msg)
        address_id = form.addressId.data
        address = session.query(UserAddress).filter(UserAddress.address_id == address_id,
                                                    UserAddress.delete_flag == 0).first()
        user_id = request.jwt_user.id
        if not address:
            return R.failed("当前地址已不存在，请重新添加地址")
        # 从购物车获取商品
        cart_list = session.query(Cart).filter(Cart.user_id == user_id, Cart.delete_flag == 0,
                                               Cart.selected == ONE).all()
        if not cart_list:
            return R.failed("恭喜您的购物车已经被清空了，再加一车吧")
        # 生成订单编码
        order_no = str(int(round(time.time() * 1000)))
        total_price = 0
        with session.begin_nested():
            for cart in cart_list:
                # 查询商品是否售尽
                product = session.query(Product).filter(Product.product_id == cart.product_id, Product.delete_flag == 0,
                                                        Product.status == EnableStatus.ENABLE.value,
                                                        Product.stock > 0).first()
                if not product:
                    return R.failed(f"商品{cart.product_name}已售尽，请选择其它产品")
                # 构建订单明细信息
                order_detail, total_price = save_order_detail(session, cart, order_no, product, total_price, user_id)
                # 删除购物车信息
                delete_cart(session, cart)
                # 构建交易记录
                save_order_status_record(session, order_detail, order_no)

                # 构建订单主表信息
            save_order_info(session, address, address_id, order_no, total_price, user_id)
        session.commit()
        return R.ok(data=order_no)
    except Exception as e:
        logger.info("错误信息：\n{}", format(e))
        return R.failed(msg="操作失败")
    finally:
        # 关闭连接
        session.close()


def save_order_info(session, address, address_id, order_no, total_price, user_id):
    order_info = OrderInfo(order_no=order_no,
                           address_id=address_id,
                           province=address.province,
                           city=address.city,
                           area=address.area,
                           street=address.street,
                           postal_code=address.postal_code,
                           receive_name=address.receive_name,
                           payment=total_price,
                           payment_type=1,
                           payment_type_desc="在线支持",
                           receive_phone=address.receive_phone,
                           status=10,
                           status_desc="未付款",
                           create_user=user_id,
                           update_user=user_id,
                           user_id=user_id
                           )
    # order_info.save()
    session.add(order_info)


def save_order_status_record(session, order_detail, order_no):
    record = OrderStatusRecord(order_no=order_no,
                               order_detail_no=order_detail.order_detail_no,
                               product_id=order_detail.product_id,
                               product_name=order_detail.product_name,
                               status=order_detail.status,
                               status_desc=order_detail.status_desc)
    # record.save()
    session.add(record)


def save_order_detail(session, cart, order_no, product, total_price, user_id):
    order_detail = OrderDetail(
        order_no=order_no,
        order_detail_no=str(int(round(time.time()))),
        product_id=cart.product_id,
        product_name=cart.product_name,
        product_main_image=cart.product_main_image,
        quantity=cart.quantity,
        current_unit_price=cart.product_unit_price,
        status=OrderStatus.WAIT_PAY.value,
        status_desc="未付款",
        total_price=cart.product_total_price,
        user_id=user_id,
        create_user=user_id
    )
    activity = session.query(Activity).filter(Activity.activity_id == product.activity_id,
                                              Activity.delete_flag == 0).first()
    if activity:
        order_detail.activity_id = activity.activity_id
        order_detail.activity_name = activity.name
        order_detail.activity_main_image = activity.main_image
    # 总金额
    total_price += cart.product_total_price
    # order_detail.save()
    session.add(order_detail)
    return order_detail, total_price


def delete_cart(session, cart):
    session.query(Cart).filter(Cart.id == cart.id).update({"delete_flag": 1, "update_time": datetime.now()})
    # session.commit()
    # cart.save()
    # session.update(cart)


# 订单详情
async def order_detail(order_no, request):
    user_id = request.jwt_user.id
    order_info = db.query(OrderInfo).filter(OrderInfo.order_no == order_no, OrderInfo.delete_flag == 0,
                                            OrderInfo.user_id == user_id).first()
    if order_info:
        order_vo = order_info.to_dict()
        order_detail_list = db.query(OrderDetail).filter(OrderDetail.order_no == order_no,
                                                         OrderDetail.delete_flag == 0).all()
        if len(order_detail_list) > 0:
            for item in order_detail_list:
                order_vo["details"].append(item.to_dict())
        return R.ok(data=order_vo)
    return R.ok()


# 取消订单
async def cancel_order(order_no, request):
    try:
        user_id = request.jwt_user.id
        order_info = db.query(OrderInfo).filter(OrderInfo.order_no == order_no, OrderInfo.delete_flag == 0,
                                                OrderInfo.user_id == user_id).first()
        if order_info:
            if order_info.status != OrderStatus.WAIT_PAY.value:
                return R.failed(f"当前订单{order_info.status_desc}不允许取消")
            order_info.status = 0
            order_info.status_desc = "已取消"
            order_info.update_user = user_id
            order_info.save()
            order_detail_list = db.query(OrderDetail).filter(OrderDetail.order_no == order_no,
                                                             OrderDetail.delete_flag == 0,
                                                             OrderDetail.user_id == user_id).all()
            if len(order_detail_list) > 0:
                for item in order_detail_list:
                    item.status = 0
                    item.status_desc = "已取消"
                    item.update_user = user_id
                    item.save()
        return R.ok()
    except Exception as e:
        logger.error(e)
        return R.failed("操作失败")
    finally:
        # 关闭连接
        db.close()


# 付款
async def pay(request):
    session = db
    try:
        # 接收请求参数
        json_data = await request.json()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = MultiDict(json_data)
        user_id = request.jwt_user.id
        form = OrderPayForm(dict_data)
        if not form.validate():
            # 获取错误信息
            err_msg = regular.get_err(form)
            # 返回错误信息
            return R.failed(err_msg)
        order_no = form.orderNo.data
        order_info = session.query(OrderInfo).filter(OrderInfo.order_no == order_no, OrderInfo.delete_flag == 0,
                                                     OrderInfo.user_id == user_id,
                                                     OrderInfo.status == OrderStatus.WAIT_PAY.value).first()
        if not order_info:
            return R.failed("您没有待支付的订单")
        tz = ZoneInfo('UTC')
        order_info.payment_time = datetime.now(tz)
        order_info.status = OrderStatus.PAY_PLAN.value
        order_info.status_desc = "已付款"
        order_info.save()
        # 订单明细状态更新
        order_detail_list = session.query(OrderDetail).filter(OrderDetail.order_no == order_no,
                                                              OrderDetail.delete_flag == 0,
                                                              OrderDetail.user_id == user_id).all()
        if len(order_detail_list) > 0:
            for item in order_detail_list:
                item.status = OrderStatus.PAY_PLAN.value
                item.status_desc = "已付款"
                item.save()
                save_order_status_record(session, item, order_no)

        return R.ok()
    except Exception as e:
        logger.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    finally:
        # 关闭连接
        db.close()
