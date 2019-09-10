from django.contrib import admin
from django.urls import path,re_path,include

from book import views
from django.conf.urls import url

urlpatterns = [

    # path(r'index/',views.index),
    path(r'addbook/',views.addbook),

]

