"""study_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as t_v

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', t_v.index, name="index"),
    url(r'^excp_404/$', t_v.excp_404),
    url(r'mine/$', t_v.mine, name='mine'),
    url(r'get_r/$', t_v.get_request, name='get'),
    url(r'post_r/$', t_v.post_request, name='post'),
]
