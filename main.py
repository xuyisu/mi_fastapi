from apps import create_app
from config.env import FASTAPI_HOST, FASTAPI_PORT

app = create_app()

if __name__ == '__main__':
    import uvicorn

    # 使用uvicorn创建我们的服务
    uvicorn.run(app, host=FASTAPI_HOST, port=int(FASTAPI_PORT), reload=False)