from datetime import datetime
from html import escape
from fastapi.logger import logger
from sqlalchemy import and_
from sqlalchemy.exc import SQLAlchemyError

from apps.enums.yes_enum import YesEnum
from apps.constants.message import PAGE_LIMIT
from apps.forms.user_address import UserAddressForm
from apps.models.user_address import UserAddress
from werkzeug.datastructures.structures import MultiDict
from config import db
from utils import R, regular, snowflake


# 地址列表
async def pages(request):
    try:
        user_id = request.jwt_user.id
        # 页码
        page = int(request.query_params.get("current", 1))
        # 每页数
        limit = int(request.query_params.get("size", PAGE_LIMIT))
        # # 实例化查询对象
        query = db.query(UserAddress).filter(UserAddress.create_user == user_id, UserAddress.delete_flag == 0)
        # 排序
        query = query.order_by(UserAddress.id.desc())
        # 记录总数
        count = query.count()
        # 分页查询
        user_list = query.limit(limit).offset((page - 1) * limit).all()
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


# 添加地址
async def add_address(request):
    try:
        user_id = request.jwt_user.id
        # 获取请求参数
        json_data = await request.json()
        # 表单验证
        form = UserAddressForm(MultiDict(json_data))
        if not form.validate():
            # 获取错误描述
            err_msg = regular.get_err(form)
            # 返回错误信息
            return R.failed(msg=err_msg)
        # 表单数据赋值给对象
        user_address = UserAddress(**form.data)
        user_address.create_user = user_id
        user_address.update_user = user_id
        user_address.address_id = snowflake.generate_id()
        # 插入数据
        user_address.save()
        return R.ok()
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


# 获取地址详情
async def get_address_detail(address_id):
    try:
        user_address_resp = db.query(UserAddress).filter(
            and_(UserAddress.address_id == address_id, UserAddress.delete_flag == YesEnum.NO)).first()
        if not user_address_resp:
            return R.failed(msg="当前地址不存在，请重新添加")
        return R.ok(data=UserAddress.to_dict(user_address_resp))
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


# 删除地址
async def delete_address(address_id, request):
    try:
        user_id = request.jwt_user.id
        user_address_resp = db.query(UserAddress).filter(
            and_(UserAddress.address_id == address_id, UserAddress.delete_flag == YesEnum.NO)).first()
        if not user_address_resp:
            return R.failed(msg="当前地址不存在，请重新添加")
        user_address_resp.delete_flag = 1
        user_address_resp.update_user = user_id
        user_address_resp.save()
        return R.ok()
    except Exception as e:
        logger.error(e)
        raise
    finally:
        # 关闭连接
        db.close()


def get_update_data(form, multi_dict, user_id):
    return {
        "update_user": user_id,
        "update_time": datetime.now(),
        "receive_name": escape(form.receiveName.data),
        "receive_phone": escape(form.receivePhone.data),
        "province": escape(form.province.data),
        "province_code": escape(form.provinceCode.data),
        "city": escape(form.city.data),
        "city_code": escape(form.cityCode.data),
        "area": escape(form.area.data),
        "area_code": escape(form.areaCode.data),
        "street": escape(form.street.data),
        "default_flag": multi_dict.get("defaultFlag", 0),
        "postal_code": escape(form.postalCode.data),
        "address_label": multi_dict.get("addressLabel", 0)
    }


async def update_address(request, address_id):
    try:
        user_id = request.jwt_user.id
        # 获取请求参数
        json_data = await request.json()
        # 表单验证
        multi_dict = MultiDict(json_data)
        form = UserAddressForm(multi_dict)
        if not form.validate():
            # 获取错误描述
            err_msg = regular.get_err(form)
            logger.warning(f"表单验证失败: {err_msg}")
            # 返回错误信息
            return R.failed(msg=err_msg)

        # 获取更新数据
        update_data = get_update_data(form, multi_dict, user_id)

        # 先查询记录是否存在
        address = db.query(UserAddress).filter(
            and_(UserAddress.address_id == address_id, UserAddress.delete_flag == YesEnum.NO)
        ).first()

        if not address:
            logger.info(f"地址ID {address_id} 不存在")
            return R.failed(msg="当前地址不存在，请重新添加")

        # 根据主键更新地址信息
        db.query(UserAddress).filter(UserAddress.id == address.id).update(update_data, synchronize_session=False)

        db.commit()
        logger.info(f"地址ID {address_id} 更新成功")
        return R.ok()
    except (ValueError, TypeError) as e:
        logger.error(f"请求解析错误: {e}")
        return R.failed(msg="请求解析错误")
    except SQLAlchemyError as e:
        logger.error(f"数据库操作错误: {e}")
        return R.failed(msg="数据库操作错误")
    except Exception as e:
        logger.error(f"未知错误: {e}")
        raise
    finally:
        # 关闭连接
        db.close()
