#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#author:uncle sandor
from django.contrib import admin
from django.urls import path,re_path,include
from my_first_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    re_path(r'^articles/2003/$', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),  # 有名分组 名字作为视图函数参数必须保持一致
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+)/$', views.article_detail),

]