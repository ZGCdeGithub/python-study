from django.conf.urls import include, url
from . import views as v

urlpatterns = [

    url(r'getscore/(?P<num>[0-9]+)', v.getscore),
    # url(r'student/(page-([0-9]+)/)?$', v.studentlist),
    url(r'student/(?:page-(?P<page>[0-9]+)/)?$', v.studentlist),
    # 额外参数
    url(r'extraParam/$', v.extraParam, {"name": 'zgc'}),
    # 设置url的name参数，可根据name获取请求的url
    url(r'geturl_by_name/$', v.geturl, name='geturlname'),

    # 默认首页
    # url(r'/$', v.index),
]
