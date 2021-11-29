from django import forms
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