from Apps import MysqlConnector
import json
import random
import string
from Apps.models import response
from django.shortcuts import render, redirect


def adminYachtHTML(request):
    token = request.COOKIES.get('admintoken')
    if token is None:
        return redirect('/adminLogin/')
    result = MysqlConnector.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        return redirect('/adminLogin/')
    return render(request, 'adminYacht.html')


def addYachtHTML(request):
    token = request.COOKIES.get('admintoken')
    if token is None:
        return redirect('/adminLogin/')
    result = MysqlConnector.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        return redirect('/adminLogin/')
    return render(request, 'addYacht.html')


def publish(request):
    """
    管理员发布新游艇
    :param request: {'yachtname': yachtname, 'num': num}
    :return: {'code': code}
    """
    token = request.COOKIES.get('admintoken')
    result = MysqlConnector.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        to_return = {
            'code': 0
        }
        return response(to_return)
    request_list = json.loads(request.body)
    yachtname = request_list['yachtname']
    num = int(request_list['num'])
    for _ in range(num):
        yachtid = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        while MysqlConnector.get_one('YachtClub', 'select * from yachtinfo where yachtid = %s', yachtid) is not None:
            yachtid = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        MysqlConnector.modify('YachtClub', 'insert into yachtinfo (yachtid, yachtname, available) value(%s, %s, %s)',
                              [yachtid, yachtname, 'y'])
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
    result = MysqlConnector.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        to_return = {
            'code': 0
        }
        return response(to_return)
    request_list = json.loads(request.body)
    yachtid = request_list['yachtid']
    MysqlConnector.modify('YachtClub', 'delete from yachtinfo where yachtid = %s', yachtid)
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
        to_return = []
        return response(to_return)
    result = MysqlConnector.get_one('YachtClub', 'select adminname from admincookies where token = %s', token)
    if result is None:
        to_return = []
        return response(to_return)
    result = MysqlConnector.get_all('YachtClub', 'select * from yachtinfo', [])
    return response(result)


def getMyRentRecords(request):
    """
    返回我租赁游艇的所有信息
    :param
    :return:
    """
    token = request.COOKIES.get('token')
    result = MysqlConnector.get_one('YachtClub', 'select username from cookies where token = %s', token)
    if result is None:
        return response([])
    username = result['username']
    result = MysqlConnector.get_all('YachtClub', 'select recordid, records.yachtid, yachtname, time, flag '
                                                 'from records, yachtinfo where records.yachtid = yachtinfo.yachtid '
                                                 'and username = %s', username)
    for i in range(len(result)):
        result[i]['time'] = result[i]['time'].strftime("%Y-%m-%d %H:%M:%S")
    return response(result)
