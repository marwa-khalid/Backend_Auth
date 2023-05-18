from django.urls import path
from .views import register

app_name = 'authentication'

urlpatterns = [
    path('', register, name='register'),
]
