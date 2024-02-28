#urls for images

# Path: backend/ecycle/images_processor/urls.py

from django.urls import path
from images_processor.views import Images
urlpatterns = [
    path('images/',Images.as_view()),
]