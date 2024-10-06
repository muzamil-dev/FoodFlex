from django.urls import path
from .views import AddItemView, DeleteItemView

urlpatterns = [
    path('add/', AddItemView.as_view(), name='add-item'),  # Endpoint to add an item
    path('delete/<str:item_id>/', DeleteItemView.as_view(), name='delete-item'),  # Endpoint to delete an item
]
