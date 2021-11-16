from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    context = {'name': 'John'}
    return render(request, 'base.html', context)
# Create your views here.

def index (request):
    return render (request,'index.html')

def contact(request):
    return render (request, 'contact.html' )

def booking(request):
    return render (request, 'booking.html' )

def staff(request):
    return render (request, 'staff.html' )