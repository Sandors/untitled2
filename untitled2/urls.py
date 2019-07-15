from django.contrib import admin
from django.urls import path,re_path,include

from my_first_django import views

urlpatterns = [

    re_path(r'^blog/', include('templates.urls'))

]

