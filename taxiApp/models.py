from django.db import models
from web_project import settings
from django.utils import timezone
import datetime

# Create your models here.

CONTACT_STATUSES = (
    (1, "received"),
    (2, "replied"),
    (3, "closed")
)


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(blank=False, default=1, choices=CONTACT_STATUSES)
    fullname = models.CharField(max_length=120, blank=False, verbose_name='Full Name')
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=500, blank=False)
    phonenumber = models.CharField(max_length=120, null=True, blank=True, verbose_name='Phone Number')
    organization = models.CharField(max_length=120, null=True, blank=True)


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
    rating = models.PositiveIntegerField(default=3, blank=False, choices=REVIEW_RATINGS)
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


BOOKING_STATUSES = [
    (1, "created"),
    (2, "accepted"),
    (3, "cancelled")
]


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    depart_date = models.DateField(default=timezone.now, blank=False, verbose_name='Depart Date')
    depart_time = models.TimeField(default=datetime.time(8, 00), blank=False, verbose_name='Depart Time')
    status = models.PositiveIntegerField(blank=False, default=1, choices=BOOKING_STATUSES)
    pickup = models.CharField(max_length=350, blank=False, null=False, verbose_name='Pick Up')
    dropoff = models.CharField(max_length=350, blank=False, null=False, verbose_name='Drop Off')
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rider")
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="driver")
