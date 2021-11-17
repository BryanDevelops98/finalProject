from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Rider(AbstractUser):
    # Use pip package: https://github.com/stefanfoulis/django-phonenumber-field
    # phone_number = 

    def __str__(self):
        return self.username

class Review(models.Model):
    title = models.CharField(max_length=120, blank=False)
    content = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField(blank=False, default=0)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)

class Car(models.Model):
    vin = models.CharField(max_length=120, blank=False)
    model = models.CharField(max_length=120, blank=False)
    make = models.CharField(max_length=120, blank=False)
    year = models.IntegerField(max_length=120, blank=False)
    color = models.CharField(blank=True, null=True, default="#000000")

# A Driver can be associated with any number of Cars
class Driver(models.Model):
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


BOOKING_STATUSES = ("created", "cancelled")

# A Rider can book any number of Bookings
# A Booking can only be associated with 1 unique Rider (one that created the Booking)
# A Booking can only be associated with 1 Driver (the driver the Rider booked)
# A Driver can be associated with any number of Bookings
class Booking(models.Model):
    created = models.DateTimeField(blank=False, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)
    status = models.CharField(blank=False, choices=BOOKING_STATUSES)
    destination = models.CharField(max_length=350, blank=False, null=False)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL) # For now delete, changing driver or driver out/injured is a possibility
