# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from comments import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^comment_add/$', views.add_comment, name='comment_add'),
    url(r'^comment_reply/(?P<pk>\d+)$', views.add_comment, name='comment_reply'),
    url(r'^login/$', auth_views.login,
        {
            'template_name': 'auth_u/login_page.html'
        },
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {
            'next_page': 'comments:main'
        },
        name='logout'),
]