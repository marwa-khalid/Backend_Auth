from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BrandManager
from .models import PRManager
from django.db import models

class BrandManagerRegistrationForm(UserCreationForm):
    email = models.CharField(max_length=255, unique=True)

    class Meta:
        model = BrandManager
        fields = ['email', 'password1', 'password2', 'picture']

class PRManagerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = PRManager
        fields = ['email', 'password', 'confirm_password', 'image']
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        
        return cleaned_data


class PRLoginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class AdminLoginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
