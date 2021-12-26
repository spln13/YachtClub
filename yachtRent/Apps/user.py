from Apps import MysqlConnector
import json
from Apps.models import response


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

