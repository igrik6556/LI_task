# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('comments.urls', namespace='comments')),
]

handler404 = 'comments.views.custom_404'
