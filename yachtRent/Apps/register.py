from django.http import JsonResponse
from django.shortcuts import render
from Apps import MysqlConnecter
import json


def register(request):
    """
    return signin.html
    :param request:
    :return:
    """
    return render(request, "signin.html")


def check_username(request):
    """
    检查用户名是否重复
    :param request: {'username': username}
    :return: {'isExist': boolean}
    """
    request_list = json.loads(request.body)
    username = request_list['username']
    result = MysqlConnecter.get_one('YachtClub', 'select * from userinfo where username = %s', [username])
    if result is None:
        to_return = {
            "isExist": '0'
        }
    else:
        to_return = {
            "isExist": '1'
        }
    print(to_return)
    to_return = json.dumps(to_return)
    response = JsonResponse(to_return, safe=False)
    return response


def storage(request):
    """x
    :param request: {'username': username, 'password': password1, 'email': email, 'ismale': ismale}
    :return:
    """
    request_list = json.loads(request.body)
    username = request_list['username']
    password = request_list['password']
    email = request_list['email']
    if request_list['ismale']:
        gender = 'm'
    else:
        gender = 'f'
    MysqlConnecter.modify('YachtClub', 'insert into userinfo (username, password, email, gender) '
                                       'values(%s, %s, %s, %s)', [username, password, email, gender])

