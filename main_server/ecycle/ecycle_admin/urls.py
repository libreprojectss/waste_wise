from django.contrib import admin
from django.urls import path
from .views import Pickers,Products

urlpatterns = [
    path('pickers',Pickers.as_view()),
    path('products',Products.as_view())
]
