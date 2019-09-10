from django.shortcuts import render,HttpResponse,redirect

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
		return redirect('/books/')
	return render(request,'addbook.html')

def changebook(request,id):
	book_obj=Book.objects.filter(id=id).first()
	if request.method == "POST":
		title=request.POST.get('title')
		price=request.POST.get('price')
		publish=request.POST.get('publish')
		date=request.POST.get('date')
		Book.objects.filter(id=id).update(title=title,price=price,publish=publish,pub_date=date)

		return redirect('/books/')

	return render(request,'changebook.html',{"book_obj":book_obj})

def books(request):
	book_list=Book.objects.all()
	return render(request,'books.html',locals())


def delbook(request,id):

	Book.objects.filter(id=id).delete()

	return redirect('/books/')