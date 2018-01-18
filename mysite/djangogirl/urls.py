#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'djangogirl'
urlpatterns = [
	# url(r'^post/\d+/$', views.post_list, name='post_list')
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='post_edit'),
]
