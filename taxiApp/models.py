from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from web_project import settings

# Create your models here.

# Add a Driver specific registration page (add user to Driver Group)


CONTACT_STATUSES = (
    (1, "recieved"),
    (2, "replied"),
    (3, "closed")
)


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(blank=False, default=1, choices=CONTACT_STATUSES)
    fullname = models.CharField(max_length=120, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=500, blank=False)
    phonenumber = models.CharField(max_length=120, null=True, blank=True)
    organization = models.CharField(max_length=120, null=True, blank=True)


class Car(models.Model):
    vin = models.CharField(max_length=120, blank=False)
    model = models.CharField(max_length=120, blank=False)
    make = models.CharField(max_length=120, blank=False)
    year = models.IntegerField(blank=False)
    color = models.CharField(max_length=16, blank=True,
                             null=False, default="#000000")


REVIEW_RATINGS = (
    (1, "Terrible"),
    (2, "Bad"),
    (3, "Ok"),
    (4, "Good"),
    (5, "Outstanding"),
)


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120, blank=False)
    content = models.TextField(max_length=500, blank=False)
    rating = models.PositiveIntegerField(
        default=3, blank=False, choices=REVIEW_RATINGS)
    rider = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)


BOOKING_STATUSES = [
    (1, "created"),
    (2, "accepted"),
    (3, "cancelled")
]

# A Rider can book any number of Bookings
# A Booking can only be associated with 1 unique Rider (one that created the Booking)
# A Booking can only be associated with 1 Driver (the driver the Rider booked)
# A Driver can be associated with any number of Bookings


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(blank=False, default=1, choices=BOOKING_STATUSES)
    pickup = models.CharField(max_length=350, blank=False, null=False)
    dropoff = models.CharField(max_length=350, blank=False, null=False)
    rider = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="rider")
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="driver")
