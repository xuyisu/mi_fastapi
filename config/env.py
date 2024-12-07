import os

# 应用名称
FASTAPI_NAME = os.getenv('FASTAPI_NAME', 'mi_mall')
# 应用秘钥
FASTAPI_SECRET_KEY = os.getenv('FASTAPI_SECRET_KEY', 'd67beaf46fbf4f048d2eeb26fd62ea49')
# 应用运行地址
FASTAPI_HOST = os.getenv('FASTAPI_HOST', '127.0.0.1')
# 应用运行端口
FASTAPI_PORT = os.getenv('FASTAPI_PORT', 8081)
# 应用启动文件
FASTAPI_APP = os.getenv('FASTAPI_APP', 'main.py')
# 应用环境变量
FASTAPI_ENV = os.getenv('FASTAPI_ENV', 'development')
# 是否调试模式：是-True,否-False
FASTAPI_DEBUG = (os.getenv('FASTAPI_DEBUG', 'True') == 'True')
# 是否演示模式：是-True,否-False
FASTAPI_DEMO = (os.getenv('FASTAPI_DEMO', 'True') == 'True')


# =============================================== 数据库配置 =================================================

# 数据库驱动
DB_DRIVER = os.getenv('DB_DRIVER', 'mysql')
# 数据库地址
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
# 数据库端口
DB_PORT = os.getenv('DB_PORT', 3306)
# 数据库名称
DB_DATABASE = os.getenv('DB_DATABASE', 'mi_mall')
# 数据库账号
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
# 数据库密码
DB_PASSWORD = os.getenv('DB_PASSWORD', '123456')
# 数据表前缀
DB_PREFIX = os.getenv('DB_PREFIX', '')
# 是否开启调试模式：是-True,否-False
DB_DEBUG = (os.getenv('DB_DEBUG', 'True') == 'True')
# MySQL数据库链接(当前使用的数据库)
SQLALCHEMY_MYSQL_URL = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + str(
    DB_PORT) + '/' + DB_DATABASE + '?charset=utf8mb4'



