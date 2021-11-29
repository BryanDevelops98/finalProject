from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return render(request, 'taxiApp/index.html')


def contact(request: HttpRequest):
    return render(request, 'taxiApp/contact.html')


def booking(request: HttpRequest):
    return render(request, 'taxiApp/booking.html')


def staff(request: HttpRequest):
    return render(request, 'taxiApp/staff.html')


def reviews(request: HttpRequest):
    return render(request, 'taxiApp/reviews.html')
