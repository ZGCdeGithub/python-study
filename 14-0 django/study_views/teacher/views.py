from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json

# Create your views here.


def index(r):
    return HttpResponse('这是首页视图')


def excp_404(request):
    """
    使用Http404响应一个404异常
    :param request:
    :return:
    """
    raise Http404()
    # 抛出异常后，下面的代码不会再执行
    return HttpResponse('抱歉，页面找不到了')


def mine(request):
    """
    使用HttpResponseRedirect重定向地址
    :param request:
    :return:
    """
    return HttpResponseRedirect(reverse('index'))


def get_request(request):
    # print(request)
    data = {
        "path": request.path,
        "method": request.method,
        "encoding": request.encoding,
        "GET": request.GET,
        'POST': request.POST,
        'FILES': request.FILES,
        'COOKIES': request.COOKIES,
        # "SESSION": dict(request.session),
    }
    return HttpResponse(json.dumps(data))


def post_request(request):
    if request.POST:
        data = {
            "path": request.path,
            "method": request.method,
            "encoding": request.encoding,
            "GET": request.GET,
            'POST': request.POST,
            'FILES': request.FILES,
            'COOKIES': request.COOKIES,
            # "SESSION": dict(request.session),
        }
        print(request.POST.getlist('hobby'))
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('form.html')




