from django.urls import path,re_path
from book import views


urlpatterns = [
    path(r'index/', views.books),
    path(r'addbook/',views.addbook),
    re_path(r'books/(\d+)/delete',views.delbook),
    re_path(r'books/(\d+)/change',views.changebook),

]

