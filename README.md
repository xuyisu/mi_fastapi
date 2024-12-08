# python fastapi仿小米商城后端服务
## 介绍

模拟小米官网的后端服务

项目运行环境

| python       | 3.11+  |
|--------------|--------|
| fastapi       | 0.97.0 |
| uvicorn   | 0.22.0 |
| PyMySQL | 1.1.1+ |
| mysql        | 5.7+   |
| jwt        | 1.3.1  |



## 后端运行先配置数据库（mysql 和redis）

[代码地址Gitee](https://gitee.com/gitxys/mi_fastapi)

[代码地址GitHub](https://github.com/xuyisu/mi_fastapi)

**数据库配置修改**

```
#修改env.py 文件

```



点击启动类启用服务

```
app = create_app()

if __name__ == '__main__':
    import uvicorn

    # 使用uvicorn创建我们的服务
    uvicorn.run(app, host=FASTAPI_HOST, port=int(FASTAPI_PORT), reload=False)
```
## 后端启动
安装依赖包
```
pip install -r requirements.txt
```
启动服务
```
uvicorn main:app --reload
```



## 其他语言后端地址

| 名称                       | Gitee                                      | Github                                      |
| -------------------------- | ------------------------------------------ | ------------------------------------------- |
| mi_springboot (Java)       | https://gitee.com/gitxys/mi_springboot     | https://github.com/xuyisu/mi_springboot     |
| mi-beego (Golang)          | https://gitee.com/gitxys/mi-beego          | https://github.com/xuyisu/mi-beego          |
| mi-gin (Golang)            | https://gitee.com/gitxys/mi-gin            | https://github.com/xuyisu/mi-gin            |
| mi_django (Python)         | https://gitee.com/gitxys/mi_django         | https://github.com/xuyisu/mi_django         |
| mi_fastapi (Python)        | https://gitee.com/gitxys/mi_fastapi        | https://github.com/xuyisu/mi_fastapi        |
| mi_koa_nodejs (nodejs)     | https://gitee.com/gitxys/mi_koa_nodejs     | https://github.com/xuyisu/mi_koa_nodejs     |
| mi_express_nodejs (nodejs) | https://gitee.com/gitxys/mi_express_nodejs | https://github.com/xuyisu/mi_express_nodejs |
| mi_egg_nodejs (nodejs)     | https://gitee.com/gitxys/mi_egg_nodejs     | https://github.com/xuyisu/mi_egg_nodejs     |
|                            |                                            |                                             |



## 前端启动

项目地址https://gitee.com/gitxys/mi_vue

[代码地址Gitee](https://gitee.com/gitxys/mi_vue)

[代码地址GitHub](https://github.com/xuyisu/mi_vue)

控制台先安装依赖包

```
npm install 
```

然后运行下面代码即可启动

```
npm run serve
```

## 页面介绍

浏览器输入http://localhost:8080 将看到一下页面

![](images/index.png)

登录:**用户名/密码**  admin/123456

![image-20211219223115929](images/login.png)

购物车

![image-20211219223220837](images/cart.png)

订单确认

![image-20211219223323684](images/order-confirm.png)

订单结算(彩蛋！！！！   这里的结算做了特殊处理)

![image-20211219223406482](images/pay.png)

订单列表

![image-20211219223507791](images/order.png)





亲，留个star 吧
