from Apps import MysqlConnector
import json
from django.shortcuts import render
from Apps.models import response


def addUserHTML(request):
    token = request.COOKIES.get('admintokne')

    return render(request, 'addUser.html')


def addUser(request):
    """
    管理员添加用户
    :param request: {'username': username, 'password': pwd, 'email': email}
    :return:
    """
    token = request.COOKIES.get('admintoken')
    result = MysqlConnector.get_one('YachtClub', 'select * from admincookies where token = %s', token)
    if result is None:
        return response({"code": 0})
    request_list = json.loads(request.body)
    username = request_list['username']
    password = request_list['password']
    email = request_list['email']
    MysqlConnector.modify('YachtClub', 'insert into userinfo (username, password, email) values(%s, %s, %s)',
                          [username, password, email])
    return response({"code": 1})


def deleteUser(request):
    """
    管理员删除用户
    :param request: {'username': username}
    :return:
    """
    token = request.COOKIES.get('admintoken')
    result = MysqlConnector.get_one('YachtClub', 'select * from admincookies where token = %s', token)
    if result is None:
        return response({"code": 0})
    request_list = json.loads(request.body)
    username = request_list['username']
    MysqlConnector.modify('YachtClub', 'delete from userinfo where username = %s', username)
    return response({"code": 1})


def updateUser(request):
    """
    管理员删除用户
    :param request: {'username': username, 'password': password, 'email': email}
    :return:
    """
    token = request.COOKIES.get('admintoken')
    result = MysqlConnector.get_one('YachtClub', 'select * from admincookies where token = %s', token)
    if result is None:
        return response({"code": 0})
    request_list = json.loads(request.body)
    username, password, email = request_list['username'], request_list['password'], request_list['email']
    MysqlConnector.modify('YachtClub', 'update userinfo set password = %s, email = %s where username = %s',
                          [password, password, username])
    return response({"code": 1})


def getAllUser(request):
    """
    管理员查看所有用户信息
    :param request:
    :return:
    """
    token = request.COOKIES.get('admintoken')
    result = MysqlConnector.get_one('YachtClub', 'select * from admincookies where token = %s', token)
    if result is None:
        return response([])
    result = MysqlConnector.get_all('YachtClub', 'select * from userinfo', [])
    return response(result)


def getUsername(request):
    """
    获取当前登陆的用户登陆状态以及用户名
    :param request:
    :return: {"username": username}
    """
    token = request.COOKIES.get('token')
    if token is None:
        return response({"username": 0})
    result = MysqlConnector.get_one('YachtClub', 'select username from cookies where token = %s', token)
    if result is None:
        return response({"username": 0})
    username = result['username']
    return response({"username": username})


def getAdminname(request):
    """
    获取当前登陆管理员登陆状态以及管理员名
    :param request:
    :return: {"adminname": adminname}
    """
    admintoken = request.COOKIES.get("admintoken")
    if admintoken is None:
        return response({"adminname": 0})
    result = MysqlConnector.get_one('YachtClub', 'select adminname from admincookies where token = %s', admintoken)
    if result is None:
        return response({"adminname": 0})
    adminname = result["adminname"]
    return response({"adminname": adminname})
