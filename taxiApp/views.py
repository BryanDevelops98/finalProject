from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import *

def index(request: HttpRequest):
    return render(request, 'taxiApp/index.html')


def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')    

    form = ContactForm()
    context = {'form':form}
    return render(request, 'taxiApp/contact.html',context)


def booking(request: HttpRequest):
    return render(request, 'taxiApp/booking.html')


def staff(request: HttpRequest):
    return render(request, 'taxiApp/staff.html')


def reviews(request: HttpRequest):
    return render(request, 'taxiApp/reviews.html')
