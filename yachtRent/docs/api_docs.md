# 接口文档
### 用户登陆 - **post** `/api/login/verify`
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
### 检查用户名 - **POST** `api/register/check_username`
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
  "is_exist": 1
}
```

 - 用户名不存在
```json
{
  "is_exist": 0
}
```
### 储存用户信息 - **POST** `api/register/storage`
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
### 租赁游艇请求 - **POST** `api/lease/lease`
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

### 归还游艇 - **POST** `api/lease/returnyacht`
开发者: 李楠</br>
接口说明: 用户归还游艇</br>
请求参数:
```json
{
  "yachtid": "abc"
}
```
响应信息:
 - 操作失败
```json
{
  "code": 0
}
```
 - 操作成功
```json
{
  "code": 1
}
```


### 发布新游艇 - **POST** `api/yacht/publish`
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
### 获取所有游艇信息 - **GET** `api/yacht/query`
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
### 删除游艇信息 - **POST** `api/yacht/delete`
开发者: 李楠</br>
接口说明: 删除指定游艇</br>
请求参数:
```json
{
  "yachtid": "abc123"
}
```
响应信息:
 - 操作失败
```json
{
  "code": 0
}
```
 - 操作成功
```json
{
  "code": 1
}
```
### 获取个人租赁信息 - **GET** `api/yacht/getmyrentrecords`
开发者: 李楠</br>
接口说明: 返回当前用户的租赁信息</br>
请求参数: `null`</br>
响应信息:
 - 操作失败

```json
[]
```
 - 查询成功
```json
[
  {"recordid": "1","yachtid": "12312", "yachtname": "TATIANA", "time": "2019-2-10", "flag": "n"},
  {"recordid": "2","yachtid": "12312", "yachtname": "TATIANA", "time": "2019-2-10", "flag": "y"}
]
```
### 管理员获取所有记录 - **GET** `api/yacht/getAllRecords`
开发者: 李楠</br>
接口说明: 返回所有用户的租赁信息</br>
请求参数: `null` </br>
响应信息:
```json
[
  {"recordid": "1","yachtid": "12312", "username": "spln", "yachtname": "TATIANA", "time": "2019-2-10", "flag": "n"},
  {"recordid": "2","yachtid": "12313", "username": "spln13", "yachtname": "TATIANA", "time": "2019-2-10", "flag": "n"}
]
```

### 管理员新增加用户 - **POST** `api/user/adduser`
开发者: 李楠</br>
接口说明: 管理员添加新用户
请求参数:
```json
{
  "username": "spln",
  "password": "123",
  "email": "spln13@qq.com"
}
```
响应信息:
 - 操作失败
```json
{
  "code": 0
}
```
 - 操作成功
```json
{
  "code": 1
}
```
### 删除用户 - **POST** `api/user/deleteuser`
开发者: 李楠</br>
接口说明: 管理员删除用户</br>
请求参数:
```json
{
  "username": "spln"
}
```
响应信息:
 - 操作失败
```json
{
  "code": 0
}
```
 - 操作成功
```json
{
  "code": 1
}
```
### 获取所有用户信息 - **GET** `api/user/getalluser`
开发者: 李楠</br>
接口说明: 管理员获取所有用户信息</br>
请求参数: `null`</br>
响应参数:
 - 操作失败
```json
[]
```
 - 操作成功
```json
[
  {"username": "spln13", "password": "123", "email": "spln13@qq.com"}
]
```
### 更新用户信息 - **GET** `api/user/updateuserinfo`
开发者: 李楠</br>
接口说明: 管理员更改用户信息</br>
请求参数: `null`</br>
响应信息:
 - 操作失败
```json
{
  "code": 0
}
```
 - 操作成功
```json
{
  "code": 1
}
```

### 管理员登陆验证 - **POST** `api/login/adminverify`
开发者: 李楠</br>
接口说明: 验证登陆信息，登陆成功后生成令牌(token)</br>
请求参数:
```json
{
  "adminname": "spln",
  "adminpwd": "123"
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
- 管理员不存在
```json
{
  "code": 2
}
```
### 用户请求退出登陆 - **DELETE** `api/login/userlogout`
接口说明: 用户请求退出登陆, 删除token</br>
请求参数: `null`</br>
响应信息:
 - 操作失败
```json
{
  "code": 0
}
```
 - 操作成功
```json
{
  "code": 1
}
```
### 管理员请求退出登陆 - **DELETE** `api/login/adminlogout`
接口说明: 管理员请求退出登陆, 删除token</br>
请求参数: `null`</br>
响应信息:
 - 操作失败
```json
{
  "code": 0
}
```
 - 操作成功
```json
{
  "code": 1
}
```
### 获取用户登陆状态 - **GET** `api/user/getusername`
接口说明: 获取当前登陆的用户登陆状态以及用户名</br>
请求参数: `null`</br>
响应信息: 
 - 无登陆状态
```json
{
  "username": 0
}
```
 - 登陆状态
```json
{
  "username": "spln"
}
```
### 获取管理员登陆状态 - **GET** `api/user/getadminname`
接口说明: 获取当前登陆的管理员登陆状态以及管理员名</br>
请求参数: `null`</br>
响应信息: 
 - 无登陆状态
```json
{
  "adminname": 0
}
```
 - 登陆状态
```json
{
  "adminname": "spln"
}
```
