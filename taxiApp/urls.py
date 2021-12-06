from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('book/', views.booking, name="booking"),
    path('staff/', views.staff, name="staff"),
    path('reviews/', views.reviews, name="reviews"),
    path('reviews/add/', views.add_review, name="add_review"),
]
