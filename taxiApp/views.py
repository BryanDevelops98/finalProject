from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    context = {'name': 'John'}
    return render(request, 'hello.html', context)
# Create your views here.

def add (request):
    return render (request,'mypage.html')