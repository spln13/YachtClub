from django.http import JsonResponse
from Apps import MysqlConnecter
import json
import datetime
import random
import string


def lease(request):
    """
    处理租赁游艇请求, 存入记录表
    :param request:{'username': username, 'yachtname': yachtname}
    :return: {'code': code}
    """
    request_list = json.loads(request.body)
    username_get, yachtname = request_list['username'], request_list['yachtname']
    token = request.COOKIES.get('token')
    to_return = {
        "code": 0
    }
    result = MysqlConnecter.get_one('YachtClub', 'select username from cookies where token = %s', token)
    username = result['username']
    if username != username_get:
        to_return = {
            "code": 1  # 不匹配
        }
        to_return = json.dumps(to_return)
        response = JsonResponse(to_return, safe=False)
        return response
    result = MysqlConnecter.get_one('YachtClub', 'select yachtid, price from yachtinfo where yachtname = %s', yachtname)
    if result is None:
        # 没有船了
        to_return = {
            "code": 2  # 没有船
        }
        to_return = json.dumps(to_return)
        response = JsonResponse(to_return, safe=False)
        return response
    yachtid = result['yachtid']
    price = result['price']
    result = MysqlConnecter.get_one('YachtClub', 'select balance from userdetail where username = %s', username)
    balance = result['balance']
    if balance < price:
        # 钱不够了
        to_return = {
            "code": 3  # 没钱了
        }
        to_return = json.dumps(to_return)
        response = JsonResponse(to_return, safe=False)
        return response
    balance -= price
    time = datetime.datetime.now()
    detail = "租赁游艇"
    recordid = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    while MysqlConnecter.get_one('YachtClub', 'select * from records where recordid = %s', recordid) is not None:
        recordid = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    MysqlConnecter.modify('Yacht', 'update userdetail set balance = %s where username = %s', [balance, username])
    MysqlConnecter.modify('Yacht', 'delete from yachtinfo where yachtid = %s', yachtid)
    MysqlConnecter.modify('Yacht', 'insert into records (username, recordid, price, time, detail, yachtid) '
                                   'values(%s, %s, %s, %s, %s, %s)', [username, recordid, price, time, detail, yachtid])
    to_return = json.dumps(to_return)
    response = JsonResponse(to_return, safe=False)
    return response
