from fastapi import FastAPI, Depends

from apps.middleware.login_required import login_required
from routers.routes import routes


# 注册路由
def register_router(app: FastAPI):
    # 路由集合
    app.include_router(
        # 版本
        routes,
        # 依赖
        dependencies=[Depends(login_required)],
    )
