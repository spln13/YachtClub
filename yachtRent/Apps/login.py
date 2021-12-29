from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from Apps import MysqlConnector
import json
from Apps import cookie
from Apps.models import response


def login(request):
    """
    return static login html
    :param request:
    :return: login html
    """
    return render(request, 'login.html')


def loginVerify(request):
    """
    :param request: {'username': username, 'password': password}
    :return: {'code': code}
    {'code': 0} -> success
    {'code': 1} -> password error
    {'code': 2} -> user doesn't exist
    """
    request_list = json.loads(request.body)
    username = request_list['username']
    password = request_list['password']
    result = MysqlConnector.get_one('YachtClub', 'select password from userinfo where username = %s', [username])
    if result is None:
        return response({"code": 2})
    pwd = result['password']
    if password != pwd:
        return response({"code": 1})
    to_return = json.dumps({"code": 0})
    response1 = JsonResponse(to_return, safe=False)
    token = cookie.generateCookie()
    response1.set_cookie('token', token, 3600 * 24 * 14)
    cookie.storageCookieInfo(username, token)
    return response1


def adminLogin(request):
    """
    return a static html for admin logging
    :param request:
    :return:
    """
    return render(request, 'adminLogin.html')


def adminVerify(request):
    """
    验证管理员的登陆信息
    :param request: {'adminname': adminname, 'adminpwd': adminpwd}
    :return: {"code": code}
    {'code': 0} -> success
    {'code': 1} -> password error
    {'code': 2} -> user doesn't exist
    """
    request_list = json.loads(request.body)
    adminname, adminpwd = request_list['adminname'], request_list['adminpwd']
    result = MysqlConnector.get_one('YachtClub', 'select adminpwd from admininfo where adminname = %s', [adminname])
    if result is None:
        return response({"code": 2})
    password = result['adminpwd']
    if adminpwd != password:
        return response({"code": 1})
    admin_token = cookie.generateCookie()
    MysqlConnector.modify('YachtClub', 'insert into admincookies (adminname, token) values (%s, %s)',
                          [adminname, admin_token])
    to_return = json.dumps({"code": 0})
    response1 = JsonResponse(to_return, safe=False)
    response1.set_cookie('admintoken', admin_token, 3600 * 24 * 14)
    return response1


def userLogout(request):
    """
    用户请求退出登陆
    :param request:
    :return: {'code': code}
    """
    token = request.COOKIES.get('token')
    if token is None:
        return response({"code": 0})
    MysqlConnector.modify('YachtClub', 'delete from cookies where token = %s', token)
    response1 = HttpResponse("<script>location.href='/home/';</script>")
    response1.delete_cookie('token')
    return response1


def adminLogout(request):
    """
    管理员请求退出登陆
    :param request:
    :return: {"code": code}
    """
    token = request.COOKIES.get('admintoken')
    if token is None:
        return response({"code": 0})
    MysqlConnector.modify('YachtClub', 'delete from admincookies where token = %s', token)
    response1 = HttpResponse("<script>location.href='/home/';</script>")
    response1.delete_cookie('admintoken')
    return response1
