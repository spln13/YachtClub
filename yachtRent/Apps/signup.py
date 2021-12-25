from django.http import JsonResponse
from django.shortcuts import render
from Apps import MysqlConnecter
import json


def register(request):
    """
    return signin.html
    :param request: None
    :return: signin.html
    """
    return render(request, "signup.html")


def check_username(request):
    """
    check whether username is unique
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
    """
    :param request: {'username': username, 'password': password, 'email': email, 'ismale': ismale}
    :return: {'code': code}
    """
    request_list = json.loads(request.body)
    username = request_list['username']
    password = request_list['password']
    email = request_list['email']
    if request_list['ismale']:
        gender = 'm'
    else:
        gender = 'f'
    print(request_list)
    to_return = {
        "code": 1
    }
    try:
        MysqlConnecter.modify('YachtClub', 'insert into userinfo (username, password, email) '
                                           'values(%s, %s, %s)', [username, password, email])
    except:
        to_return = {
            "code": 0
        }
    try:
        MysqlConnecter.modify('YachtClub', 'insert into userdetial (username, gender) '
                                       'value(%s, %s)', [username, gender])
    except:
        to_return = {
            "code": 0
        }
    to_return = json.dumps(to_return)
    response = JsonResponse(to_return, safe=False)
    return response
