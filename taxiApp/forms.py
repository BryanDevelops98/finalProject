from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control"
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control"
            }),
            'phonenumber': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'organization': forms.TextInput(attrs={
                'class': "form-control"
            }),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Title of Review"
            }),
            'content': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Content of Review"
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Leave a Rating"
            }),
        }

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('pickup', 'destination', 'driver')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Title of Review"
            }),
            'content': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Content of Review"
            }),
            'rating': forms.NumberInput(attrs={
                'class': "form-control",
                'placeholder': "Leave a Rating"
            }),
        }
