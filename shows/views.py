from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Column,Article

def index(request):
	columns = Column.objects.all()
	return render(request,"index.html",{'columns':columns})

def column_detail(request,column_slug):
	column =Column.objects.get(slug=column_slug)
	return render(request,'shows/column.html',{'column':column})

def article_detail(request,article_slug):
	article =Article.objects.get(slug=article_slug)
	return render(request,'shows/article.html',{'article':article})