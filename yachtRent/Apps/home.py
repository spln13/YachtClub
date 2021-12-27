# from django.http import response
from django.shortcuts import render


def home(requests):
    """

    :param requests:
    :return: 返回index界面
    """
    return render(requests, 'index.html')
