from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',UserCreateView.as_view()),
    path('login/', LoginView.as_view()),
    path('picker/login/', PickerLoginView.as_view()),
    path('picker/locations/', PickerLocationsViews.as_view()),
    path('user/<str:id>/', GetUserById.as_view()),
    path('notifications/',NotificationViews.as_view()),


]
