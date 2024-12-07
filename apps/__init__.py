import traceback

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.logger import logger
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from config import register_extends
from config.exception import AuthorizationException
from routers import register_router
from apps.middleware import register_cros
from utils import R


# 创建应用
def create_app() -> FastAPI:
    # # 实例化应用并鉴权
    app = FastAPI(title="FastAPI",
                  description="FastAPI",
                  version="v1",
                  )

    # 注册跨域中间件
    register_cros(app)
    # 注册路由
    register_router(app)
    # 初始化扩展
    register_extends(app)
    # 注册全局异常处理
    register_exception(app)

    # 返回应用
    return app


# 注册全局异常处理
def register_exception(app: FastAPI):
    # 登录认证异常处理执行句柄
    @app.exception_handler(AuthorizationException)
    async def unicorn_exception_handler(request: Request, exc: AuthorizationException):
        return JSONResponse(
            status_code=200,
            content=R.failed(msg=exc.msg)
        )

    # 捕获参数 验证错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        捕获请求参数 验证错误
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=R.failed(msg=exc.errors())
        )
        # return R.failed(msg=exc.errors())

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=R.failed(),
        )
        # return R.failed()
