from django.urls import path
<<<<<<< HEAD
from .views import (register, login, UpdatePreferencesView)
=======
from .views import (register, login)
from .views import get_user_diet, update_user_diet
>>>>>>> 76b4c28ffa34b0a9e6587c7b00fb42070dc2bed2

urlpatterns = [
    path('register/', register, name='register'),  # API for user registration
    path('login/', login, name='register'),  # API for user registration
<<<<<<< HEAD
    path('preferences/', UpdatePreferencesView.as_view(), name='update-preferences'),
=======
    path('diet/', get_user_diet, name='get_user_diet'),  # API to get the user's diet information
    path('diet/update/', update_user_diet, name='update_user_diet'),  # API to update the user's diet information
>>>>>>> 76b4c28ffa34b0a9e6587c7b00fb42070dc2bed2
]