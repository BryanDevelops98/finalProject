from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('error/', views.error, name="error"),
    
    path('contact/', views.contact, name="contact"),

    path('book/', views.booking, name="booking"),
    path('bookings/driver/', views.driver_bookings, name="driver_bookings"),
    path('bookings/accept/<str:id>/', views.accept_booking, name="accept_booking"),
    path('bookings/cancel/<str:id>/', views.cancel_booking, name="cancel_booking"),
    path('bookings/delete/<str:id>/', views.delete_booking, name="delete_booking"),

    path('staff/', views.staff, name="staff"),

    path('reviews/', views.reviews, name="reviews"),
    path('reviews/add/', views.add_review, name="add_review"),
    path('reviews/update/<str:id>/', views.update_review, name="update_review"),
    path('reviews/delete/<str:id>/', views.delete_review, name="delete_review"),
]
