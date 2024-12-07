from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.env import SQLALCHEMY_MYSQL_URL

POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 2
CONNECT_TIMEOUT = 60
connect_args = {"connect_timeout": CONNECT_TIMEOUT}

# 创建一个SQLAlchemy引擎
engine = create_engine(
    SQLALCHEMY_MYSQL_URL,
    pool_size=POOL_SIZE,
    pool_recycle=POOL_RECYCLE,
    pool_timeout=POOL_TIMEOUT,
    max_overflow=MAX_OVERFLOW,
    connect_args=connect_args,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo_pool=True,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

Base = declarative_base()
