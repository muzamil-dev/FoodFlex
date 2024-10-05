from django.urls import path
from .views import (register, login)

urlpatterns = [
    path('register/', register, name='register'),  # API for user registration
    path('login/', login, name='register'),  # API for user registration
]