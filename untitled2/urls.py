from django.contrib import admin
from django.urls import path,re_path,include

from my_first_django import views
from django.conf.urls import url


urlpatterns = [

    # re_path(r'^blog/', include('templates.urls')),
    re_path(r'^archives/([0-9]{4}/$)',views.year_archive,name='news-year-archive'),
    re_path(r'time/',views.current_datetime),
    re_path(r'index/',views.index),
    re_path(r'moban/',views.moban),
    re_path(r'moban1/',views.moban1),
    re_path(r'moban2/',views.moban2),


]

