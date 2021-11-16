from django.urls import path
from . import views

urlpatterns = [
path('', views.hello, name="hello"),
path('index/', views.index, name="index"),
path('contact/',views.contact,name="contact"),
path('book/',views.booking,name="booking"),
path('staff/',views.staff,name="staff"),
]