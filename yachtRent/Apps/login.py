from django.http import JsonResponse
from django.shortcuts import render
from Apps import MysqlConnector
import json
from Apps import cookie


def login(request):
    """
    return static login html
    :param request:
    :return: login html
    """
    return render(request, 'login.html')


def login_verify(request):
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
    # TODO: 验证
    result = MysqlConnector.get_one('YachtClub', 'select password from userinfo where username = %s', [username])
    is_success = False
    if result is None:
        to_return = {
            'code': 2
        }
    else:
        pwd = result['password']
        if password == pwd:
            to_return = {
                'code': 0
            }
            is_success = True
        else:
            to_return = {
                'code': 1
            }
    print(to_return)
    to_return = json.dumps(to_return)
    response = JsonResponse(to_return, safe=False)
    if is_success:
        token = cookie.generateCookie()
        cookie.storageCookieInfo(username, token)
        print(token)
    return response
