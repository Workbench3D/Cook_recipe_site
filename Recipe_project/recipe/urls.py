from django.urls import path

from .views import index, recipes

urlpatterns = [
    path('', index),
    path('recipes', recipes)
]
