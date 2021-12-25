# 接口文档
### 0.用户登陆 - **post** `/api/login/verify`
开发者: 李楠</br>
接口说明: 验证登陆信息，登陆成功后生成令牌(token)</br>
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
### 1. 检查用户名 - **POST** `api/register/check_username`
开发者: 李楠</br>
接口说明: 检查用户名是否重复</br>
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
### 2. 储存用户信息 - **POST** `api/register/storage`
开发者: 李楠</br>
接口说明: 将用户的信息储存</br>
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
### 3. 租赁游艇请求 - **POST** `api/lease`
开发者: 李楠</br>
接口说明: 发出租赁游艇请求</br>
请求参数:
```json
{
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
 - token不存在
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
### 4. 发布新游艇 - **POST** `api/yacht/publish`
开发者: 李楠</br>
接口说明: 管理员发布新游艇</br>
请求参数:
```json
{
  "yachtname": "TATIANA",
  "num": 3
}
```
响应信息:
 - 操作成功
```json
{
  "code": 1
}
```
 - 操作失败
```json
{
  "code": 0
}
```
### 5. 获取所有游艇信息 - **GET** `api/yacht/query`
开发者: 李楠</br>
接口说明: 返回所有游艇信息</br>
请求参数: `null`</br>
响应信息:
 - 操作失败
```json
[]
```
 - 查询成功
```json
[
  {"yachtid": "abc1234", "yachtname": "TATIANA"},
  {"yachtid": "abc1235", "yachtname": "CLARITY"}
]
```