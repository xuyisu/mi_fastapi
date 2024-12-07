
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware



# 注册跨域中间件
def register_cros(app: FastAPI):
    # 允许发出跨域请求的源列表
    origins = [
        "http://localhost:8080",
        # 以下添加实际时使用自定义前端访问域名
    ]
    # 配置中间件
    app.add_middleware(ProxyHeadersMiddleware)
    app.add_middleware(
        CORSMiddleware,
        # 允许访问的源
        allow_origins=origins,
        # 支持 cookie
        allow_credentials=True,
        # 允许使用的请求方法
        allow_methods=['OPTIONS', 'GET', 'POST', 'DELETE', 'PUT'],
        # 允许携带的 Headers
        allow_headers=["*"],
        # 设置浏览器缓存 CORS 响应的最长时间(以秒为单位)，默认600
        max_age=3600
    )



