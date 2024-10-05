from django.urls import path
from .views import (register, login, UpdatePreferencesView, GetUserPreferencesView, AddFavoriteRecipeView)
from .views import get_user_diet, update_user_diet


urlpatterns = [
    path('register/', register, name='register'),  # API for user registration
    path('login/', login, name='login'),  # API for user registration
    path('preferences/', UpdatePreferencesView.as_view(), name='update-preferences'),
    path('preferences/<str:user_id>/', GetUserPreferencesView.as_view(), name='get-user-preferences'),
    path('diet/', get_user_diet, name='get_user_diet'),  # API to get the user's diet information
    path('diet/update/', update_user_diet, name='update_user_diet'),  # API to update the user's diet information
    path('add_favorite_recipe/', AddFavoriteRecipeView.as_view(), name='add-favorite-recipe'),
]