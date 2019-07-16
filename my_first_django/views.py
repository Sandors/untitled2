from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import datetime

# Create your views here.

def index(request):
	import datetime
	S = "hello world"
	L = [111,222,333]
	dic = {"name":"yuan","age":18}
	date = datetime.date(1993,4,5)
	class Person(object):
		def __init__(self,name):
			self.name=name
	person_yuan = Person("yuan")
	person_egon = Person("egon")
	person_alex = Person("alex")

	persion_list = [person_yuan,person_egon,person_alex]
	value = "<a href="">点击</a>"

	return render(request,'index.html',{"S":S,"L":L,"dic":dic,"date":date,"persion_list":persion_list,"value":value})


def special_case_2003(request):
	import datetime
	now = datetime.datetime.now()
	ctime = now.strftime("%Y-%m-%d %X")

	return render(request,"index.html",{"ctime":ctime})

def year_archive(requset,year):
	import datetime

	now = datetime.datetime.now()
	ctime = now.strftime("%Y-%m-%d %X")

	return render(requset,"index.html",{"ctime":ctime})


def month_archive(requset,year,month):
	import datetime

	now = datetime.datetime.now()
	ctime = now.strftime("%Y-%m-%d %X")

	return render(requset,"index.html",{"ctime":ctime})


def article_detail(requset,year,month,day):
	import datetime

	now = datetime.datetime.now()
	ctime = now.strftime("%Y-%m-%d %X")

	return render(requset,"index.html",{"ctime":ctime})

def redirect_to_year(request):

	year = 2006
	return  HttpResponseRedirect(reverse('news-year-archive',args=(year,)))


def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def moban(request):

    import datetime
    now=datetime.datetime.now()
    ctime=now.strftime("%Y-%m-%d %X")

    return render(request,"base.html",{"ctime":ctime})


def moban1(request):

    import datetime
    now=datetime.datetime.now()
    ctime=now.strftime("%Y-%m-%d %X")

    return render(request,"jicheng1.html",{"ctime":ctime})

def moban2(request):

    import datetime
    now=datetime.datetime.now()
    ctime=now.strftime("%Y-%m-%d %X")

    return render(request,"jicheng2.html",{"ctime":ctime})
