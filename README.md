# Tornado Web应用

## 描述
基于torado框架构架的RESTful风格的api的web服务

## 项目启动说明
- 修改config.py配置
- 启动mongodb数据库，修改db.py
- 启动server.py

## Api数据返回
```
{
    'code': 0,
    'msg': 'success',
    'data': data
}
```

## 技术架构
- Python2.7+Tornado5.1+Mongodb4.2+Redis+RESTful
- motorengine 数据操作模块
- 非阻塞并发
- pycryptodome、base64、md5加密解密
- AES，CBS加密
- tornadoredis连接池的使用

## 数据库连接问题
本地连接不需要配置用户密码，不然有权限问题，线上环境一定要配置权限用户，安全考虑
mongodb如何使用权限用户登录，查看文档

## 问题
1. redis获取值问题，可以存，数据库也有，但是获取不到
原因：redis命名文件名和导入包名一致，会导致导入失败
