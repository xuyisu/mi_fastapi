from enum import Enum


class OrderStatus(Enum):
    # 待支付
    WAIT_PAY = 10
    # 已支付
    PAY_PLAN = 20
