from fastapi import APIRouter

from apps.views import user, product, user_address, category, order_info, cart

# 创建路由
routes = APIRouter()
# 用户管理
routes.include_router(user.router, prefix="/user", tags=["用户管理"])
routes.include_router(user_address.router, prefix="/address", tags=["用户地址管理"])
routes.include_router(product.router, prefix="/product", tags=["商品管理"])
routes.include_router(category.router, prefix="/category", tags=["类目管理"])
routes.include_router(order_info.router, prefix="/order", tags=["订单管理"])
routes.include_router(cart.router, prefix="/cart", tags=["购物车管理"])
