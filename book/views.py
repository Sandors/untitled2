from django.shortcuts import render

# Create your views here.
# from book.models import Book_test
from django.shortcuts import HttpResponse
from book.models import Book

def index(request):
	# book_obj = Book(title="python葵花宝典", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
	# book_obj.save()
	book_obj = Book.objects.create(title="python葵花宝典",  price=100, publish="苹果出版社", pub_date="2012-12-12")
	print(book_obj.title,book_obj.publish,book_obj.price)
	return HttpResponse(book_obj.title)






