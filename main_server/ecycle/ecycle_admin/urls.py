from django.contrib import admin
from django.urls import path
from .views import Pickers,Products,FillRandom

urlpatterns = [
    path('pickers',Pickers.as_view()),
    path('products',Products.as_view()),
    path('fill_random',FillRandom.as_view())
]
