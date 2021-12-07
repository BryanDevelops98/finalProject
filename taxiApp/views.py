from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *



def index(request: HttpRequest):
    return render(request, 'taxiApp/index.html')


def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            sub_context = {'email':form.cleaned_data['email']}
            return render(request, 'taxiApp/contact_submitted.html', sub_context)

    form = ContactForm()
    context = {'form': form}
    return render(request, 'taxiApp/contact.html', context)


def booking(request: HttpRequest):
    return render(request, 'taxiApp/booking.html')


def staff(request: HttpRequest):
    return render(request, 'taxiApp/staff.html')


def reviews(request: HttpRequest):
    reviews = Review.objects.order_by('created')
    context = { 'reviews': reviews }
    return render(request, 'taxiApp/reviews/reviews.html', context)

@login_required(login_url='login')
def add_review(request: HttpResponse):
    # create Review form 
    form = ReviewForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.instance.rider = request.user
            form.save()
            return redirect('reviews')

    context = {'form': form}
    return render(request, 'taxiApp/reviews/add_review.html', context)

@login_required(login_url='login')
def update_review(request: HttpResponse, id: str):
    review = Review.objects.get(id=id)
    form = ReviewForm(instance=review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect('reviews')

    context = {'form': form}
    return render(request, 'taxiApp/reviews/update_review.html', context)

@login_required(login_url='login')
def delete_review(request: HttpResponse, id: str):
    review = Review.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect('index')

    context = {'review': review}
    return render(request, 'taxiApp/reviews/delete_review.html', context)