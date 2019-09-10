from django.shortcuts import render

# Create your views here.
# from book.models import Book_test
from django.shortcuts import HttpResponse
from book.models import Book

def addbook(request):
	if request.method == "POST":
		title=request.POST.get('title')
		price=request.POST.get('price')
		publish=request.POST.get('publish')
		date=request.POST.get('date')
		book_obj=Book.objects.create(title=title,price=price,publish=publish,pub_date=date)
		return HttpResponse("ok")
	return render(request,'addbook.html')





