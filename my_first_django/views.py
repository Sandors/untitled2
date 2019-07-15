from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	import datetime
	now = datetime.datetime.now()
	ctime = now.strftime("%Y-%m-%d %X")

	return render(request,"index.html",{"ctime":ctime})

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

	year=2006
	return  HttpResponseRedirect(reversed('news-year-archive',args=(year,)))