from django.urls import path
from .views import UserViewID,NewUser,AddItemAmazon,EditItemAmazon

urlpatterns=[
    path('newuser/', NewUser.as_view()),
    path('user/<int:pk>/', UserViewID.as_view()),
    path('AddItemAmazon/',AddItemAmazon.as_view()),
    path('EditItemAmazon/<int:pk>/', EditItemAmazon.as_view()),
]