from django.contrib import admin
from django.urls import path,re_path,include

from my_first_django import views
from django.conf import urls


urlpatterns = [

    # re_path(r'^blog/', include('templates.urls')),
    re_path(r'^archives/([0-9]{4}/$)',views.year_archive,name='news-year-archive'),
    ######
######

]

