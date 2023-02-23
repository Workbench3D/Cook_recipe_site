from django.urls import path

from .views import index, recipes, recipe_dish

urlpatterns = [
    path('', index),
    path('recipes', recipes),
    path('recipe_dish', recipe_dish),
]
