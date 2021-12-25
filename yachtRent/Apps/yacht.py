from Apps import MysqlConnecter
import json
import random
import string
from Apps.models import response


def publish(request):
    """
    管理员发布新游艇
    :param request: {'yachtname': yachtname, 'num': num}
    :return: {'code': code}
    """
    token = request.COOKIES.get('admintoken')
    result = MysqlConnecter.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        to_return = {
            'code': 0
        }
        return response(to_return)
    request_list = json.loads(request.body)
    yachtname = request_list['yachtname']
    num = request_list['num']
    for _ in range(num):
        yachtid = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        while MysqlConnecter.get_one('YachtClub', 'select * from yachtinfo where yachtid = %s', yachtid) is not None:
            yachtid = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        MysqlConnecter.modify('YachtClub', 'insert into yachtinfo (yachtid, yachtname) value(%s, %s)',
                              [yachtid, yachtname])
    to_return = {
        'code': 1
    }
    return response(to_return)


def delete(request):
    """
    管理员删除游艇
    :param request: {'yachtid': yachtid}
    :return: {'code': code}
    """
    token = request.COOKIES.get('admintoken')
    result = MysqlConnecter.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        to_return = {
            'code': 0
        }
        return response(to_return)
    request_list = json.loads(request.body)
    yachtid = request_list['yachtid']
    MysqlConnecter.modify('Yacht', 'delete from yachtinfo where yachtid = %s', yachtid)
    to_return = {
        'code': 1
    }
    return response(to_return)


def getAllYacht(request):
    """
    返回所有游艇的信息
    :param request:
    :return:
    """
    token = request.COOKIES.get('admintoken')
    if token is None:
        to_return = {
            'code': 0
        }
        return response(to_return)
    result = MysqlConnecter.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        to_return = {
            'code': 0
        }
        return response(to_return)
    result = MysqlConnecter.get_all('YachtClub', 'select * from yachtinfo', [])
    return response(result)


def getMyRent(request):
    """
    返回我租赁游艇的所有信息
    :param
    :return:
    """
    token = request.COOKIES.get('token')
    result = MysqlConnecter.get_one('Yacht', 'select username from cookies where token = %s', token)
    if result is None:
        return response({'code': 0})
    username = result['username']
    result = MysqlConnecter.get_all('Yacht', 'select recordid, records.yachtid, yachtname, time, flag '
                                             'from records, yachtinfo where records.yachtid = yachtinfo.yachtid '
                                             'and username = %s', username)
    return response(result)
