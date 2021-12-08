from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .templatetags.user_extras import user_in_driver_group


def index(request: HttpRequest):
    return render(request, 'taxiApp/index.html')


def contact(request: HttpRequest):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            sub_context = {'email': form.cleaned_data['email']}
            return render(request, 'taxiApp/contacts/contact_submitted.html', sub_context)

    form = ContactForm()
    context = {'form': form}
    return render(request, 'taxiApp/contacts/contact.html', context)


@login_required(login_url='login')
def booking(request: HttpRequest):
    if user_in_driver_group(request.user):
        return redirect('index')

    bookings = Booking.objects.filter(rider_id=request.user.id).order_by('-created')
    form = BookingForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.rider = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Ride booked, enjoy your upcoming trip!')
            return redirect('booking')

    context = {'bookings': bookings, 'form': form}
    return render(request, 'taxiApp/bookings/booking.html', context)


@login_required(login_url='login')
def driver_bookings(request: HttpRequest):
    bookings = Booking.objects.filter(driver_id=request.user.id).order_by('-created')
    context = {'bookings': bookings}
    return render(request, 'taxiApp/bookings/driver_bookings.html', context)


# This route will be used by Drivers to accept a booking request (check if the user is a Driver)
# If user isn't Driver, route to access level page with error

@login_required(login_url='login')
def accept_booking(request: HttpRequest, id: str):
    if user_in_driver_group(request.user):
        booking = Booking.objects.get(id=id)
        if booking.status != 2:
            booking.status = 2 # accepted status
            booking.save()
        return redirect('driver_bookings')
    else:
        messages.add_message(request, messages.ERROR, "Unauthorized to access this resource")
        return redirect('error')


# This route will be used for deleting a booking (check whether the user is a driver or not)
@login_required(login_url='login')
def delete_booking(request: HttpRequest, id: str):
    booking = Booking.objects.get(id=id)
    booking.delete()

    if user_in_driver_group(request.user):
        return redirect('driver_bookings')
    else:
        return redirect('booking')


# This route will be used for cancelling a booking (check whether the user is a driver or not)
@login_required(login_url='login')
def cancel_booking(request: HttpRequest, id: str):
    booking = Booking.objects.get(id=id)

    if request.method == 'POST':
        if booking.status != 3:
            booking.status = 3  # cancel status
            booking.save()

        if user_in_driver_group(request.user):
            return redirect('driver_bookings')
        else:
            return redirect('booking')

    context = {'booking': booking}
    return render(request, 'taxiApp/bookings/cancel_booking.html', context)


def error(request: HttpRequest):
    return render(request, 'taxiApp/errors/error.html')


def staff(request: HttpRequest):
    return render(request, 'taxiApp/staff.html')


def reviews(request: HttpRequest):
    reviews = Review.objects.order_by('-created')
    context = {'reviews': reviews}
    return render(request, 'taxiApp/reviews/reviews.html', context)


@login_required(login_url='login')
def add_review(request: HttpRequest):
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
def update_review(request: HttpRequest, id: str):
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
def delete_review(request: HttpRequest, id: str):
    review = Review.objects.get(id=id)

    if request.method == 'POST':
        review.delete()
        return redirect("reviews")


    context = {'review': review}
    return render(request, 'taxiApp/reviews/delete_review.html', context)
