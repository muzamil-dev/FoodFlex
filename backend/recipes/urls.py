from django.urls import path
from .views import RecipeCreateView, RecipeListView, RecipeDetailView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),  # Fixed line
    path('create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<str:recipe_id>/', RecipeDetailView.as_view(), name='recipe-detail'),
]
