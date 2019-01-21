from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return HttpResponse('hello word!')


def getscore(request, num):
    """
    查询学生成绩的请求
    :param request:
    :param num:
    :return:
    """
    return HttpResponse('请求学号为：{0}的学生的成绩'.format(num))


def studentlist(request, page):
    """
    带分页参数的请求
    :param request:
    :param page:
    :return:
    """
    print(page)
    return HttpResponse('第{0}页的学生列表'.format(page))


def extraParam(request,name):
    """
    设置额外参数，非前台请求，默认添加
    :param request:
    :param name:    在定义url时直接定义name的值
    :return:
    """
    return HttpResponse('我的名字是：{}'.format(name))


def geturl(request):
    """
    通过reverse()反向解析url
    :param request:
    :return:
    """
    return HttpResponse('get url: {0}'.format(reverse('geturlname')))

