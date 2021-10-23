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


# def register_verify(request):
#     """
#     verify is the username already exists
#     :param request:
#     :return:
#     """
