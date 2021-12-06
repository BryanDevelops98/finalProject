from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

# Merge the Driver and Rider into a User class
# Add Role of Driver if the User is a Driver?
# Add property: IsDriver to indicate if the user is a Driver
# Add foreign key to Car?
# Add phonenumber property for Driver (can be null, can be empty for regular User)

# Make sure to use only properties for regular or driver in registration form
# Update regular login/register pages to be User
# Create Driver login/register page

class Rider(AbstractUser):
    def __str__(self):
        return self.username


class Contact(models.Model):
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
    color = models.CharField(max_length=16, blank=True, null=True, default="#000000")
    # Add foreign key to User for Driver (Driver can have multiple Cars?)

# A Driver can be associated with any number of Cars


# Remove this class, will be merged into User class
class Driver(models.Model):
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


REVIEW_RATINGS = (
    (1, "Terrible"),
    (2, "Bad"),
    (3, "Ok"),
    (4, "Good"),
    (5, "Outstanding"), 
)

class Review(models.Model):
    title = models.CharField(max_length=120, blank=False)
    content = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField(blank=False, default=3, choices=REVIEW_RATINGS)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)


BOOKING_STATUSES = [
    ("created", "created"),
    ("accepted", "accepted"),
    ("cancelled", "cancelled")
]

# A Rider can book any number of Bookings
# A Booking can only be associated with 1 unique Rider (one that created the Booking)
# A Booking can only be associated with 1 Driver (the driver the Rider booked)
# A Driver can be associated with any number of Bookings


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)
    status = models.CharField(max_length=85, blank=False, choices=BOOKING_STATUSES)
    pickup = models.CharField(max_length=350, blank=False, null=True)
    destination = models.CharField(max_length=350, blank=False, null=True)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
