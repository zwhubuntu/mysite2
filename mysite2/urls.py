"""mysite2 URL Configuration

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
from Test import views
from django.views.generic.base import RedirectView
#from Test import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Test/$', 'Test.views.login'),
    url(r'^Test/login/$', 'Test.views.login'),
    url(r'^Test/regist/$', 'Test.views.regist'),
    url(r'^Test/index/$', 'Test.views.index'),
    #url(r'^Test/index/$', 'Test.views.showusers'),
    #url(r'^Test/logout/$', 'Test.views.logout'),
    url(r'^Test/logout/$', RedirectView.as_view(url='/Test/login/'), name='Test.views.logout'),
    url(r'^$', 'Test.views.login'),
]
