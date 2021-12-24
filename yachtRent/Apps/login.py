from django.http import JsonResponse
from django.shortcuts import render
from Apps import MysqlConnecter
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
    result = MysqlConnecter.get_one('YachtClub', 'select password from userinfo where username = %s', [username])
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
        else:
            to_return = {
                'code': 1
            }

    to_return = json.dumps(to_return)
    response = JsonResponse(to_return, safe=False)
    warrant = cookie.generateCookie()
    response.set_cookie('warrant', warrant, max_age=3253600000)

    return response
