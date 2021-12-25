# 接口文档
### 0.用户登陆 - **post** `/api/login/verify`
开发者: 李楠\
接口说明: 验证登陆信息，登陆成功后生成令牌(token)\
请求参数:
```json
{
  "username": "spln",
  "password": "123"
}
```

响应信息: 

 - 登陆成功
```json
{
  "code": 0
}
```
- 密码错误
```json
{
  "code": 1
}
```
- 用户不存在
```json
{
  "code": 2
}
```
### 1. 检查用户名 - **GET** `api/register/check_username`
开发者: 李楠\
接口说明: 检查用户名是否重复\
请求参数:

```json
{
  "username": "spln"
}
```
响应信息:
 - 用户名已存在
```json
{
  "is_exist": "1"
}
```

 - 用户名不存在
```json
{
  "is_exist": "0"
}
```
### 2. 储存用户信息 - POST `api/register/storage`
开发者: 李楠\
接口说明: 将用户的信息储存\
请求参数:

```json
{
  "username": "spln",
  "password": "123",
  "email": "qwe@123.com",
  "ismale": 1
}
```
响应信息: 
 - 存储成功
```json
{
  "code": 1
}
```
 - 存储失败
```json
{
  "code": 0
}
```
### 3. 租赁游艇请求 - POST `api/lease`
开发者: 李楠\
接口说明：发出租赁游艇请求\
请求参数:
```json
{
  "username": "spln",
  "yachtname": "abc"
}
```
响应信息:
 - 租赁成功
```json
{
  "code": 0
}
```
 - 用户不匹配
```json
{
  "code": 1
}
```
 - 无剩余船数
```json
{
  "code": 2
}
```
 - 用户余额不足
```json
{
  "code": 3
}
```