from django.contrib import admin
from django.urls import path,re_path,include

from book import views
from django.conf.urls import url

urlpatterns = [

    # path(r'index/',views.index),
    path(r'addbook/',views.addbook),
    path(r'books/',views.books),
    re_path(r'books/(\d+)/delete',views.delbook),
    re_path(r'books/(\d+)/change',views.changebook),

]

