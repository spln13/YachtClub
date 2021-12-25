from django.http import JsonResponse
from Apps import MysqlConnecter
import json
import datetime
import random
import string


def lease(request):
    """
    处理租赁游艇请求, 存入记录表
    :param request:{'yachtname': yachtname}
    :return: {'code': code}
    """
    request_list = json.loads(request.body)
    yachtname = request_list['yachtname']
    token = request.COOKIES.get('token')
    to_return = {
        "code": 0
    }
    result = MysqlConnecter.get_one('YachtClub', 'select username from cookies where token = %s', token)
    if result is None:
        to_return = {
            "code": 1  # 不匹配
        }
        to_return = json.dumps(to_return)
        response = JsonResponse(to_return, safe=False)
        return response
    username = request_list['username']
    result = MysqlConnecter.get_one('YachtClub', 'select yachtid from yachtinfo where yachtname = %s', yachtname)
    if result is None:
        # 没有船了
        to_return = {
            "code": 2  # 没有船
        }
        to_return = json.dumps(to_return)
        response = JsonResponse(to_return, safe=False)
        return response
    yachtid = result['yachtid']
    time = datetime.datetime.now()
    detail = "租赁游艇"
    recordid = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    while MysqlConnecter.get_one('YachtClub', 'select * from records where recordid = %s', recordid) is not None:
        recordid = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    MysqlConnecter.modify('Yacht', 'delete from yachtinfo where yachtid = %s', yachtid)
    MysqlConnecter.modify('Yacht', 'insert into records (username, recordid, time, detail, yachtid) '
                                   'values(%s, %s, %s, %s, %s)', [username, recordid, time, detail, yachtid])
    to_return = json.dumps(to_return)
    response = JsonResponse(to_return, safe=False)
    return response
