from Apps import MysqlConnector
import json
import datetime
from Apps.models import response


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
    result = MysqlConnector.get_one('YachtClub', 'select username from cookies where token = %s', token)
    if result is None:
        to_return = {
            "code": 1  # 不匹配
        }
        return response(to_return)
    username = request_list['username']
    result = MysqlConnector.get_one('YachtClub', 'select yachtid from yachtinfo where yachtname = %s '
                                                 'and available = %s', [yachtname, 'y'])
    if result is None:
        # 没有船了
        to_return = {
            "code": 2  # 没有船
        }
        return response(to_return)
    yachtid = result['yachtid']
    time = datetime.datetime.now()
    detail = "租赁游艇"
    # recordid = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    # while MysqlConnector.get_one('YachtClub', 'select * from records where recordid = %s', recordid) is not None:
    #     recordid = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    MysqlConnector.modify('YachtClub', 'update  yachtinfo set available = %s where yachtid = %s', ['n', yachtid])
    MysqlConnector.modify('YachtClub', 'insert into records (username, recordid, time, detail, yachtid, flag) '
                                       'values(%s, %s, %s, %s, %s, %s)', [username, None, time, detail, yachtid, 'n'])
    return response(to_return)


def returnYacht(request):
    """
    用户归还游艇
    :param request: {'yachtid': "abc"}
    :return: {'code': code}
    """
    token = request.COOKIES.get('token')
    result = MysqlConnector.get_one('YachtClub', 'select username from cookies where token = %s', token)
    if result is None:
        return response({"code": 0})
    username = result['username']
    result_list = json.loads(request.body)
    yachtid = result_list['yachtid']
    MysqlConnector.modify('YachtClub', 'update records set flag = %s where yachtid = %s and username = %s '
                                       'and flag = %s', ['y', yachtid, username, 'n'])
    response({"code": 1})
