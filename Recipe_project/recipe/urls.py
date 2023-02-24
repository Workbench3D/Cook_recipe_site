from django.urls import path

from .views import index, recipes, recipe_dish

urlpatterns = [
    path('', index, name='index'),
    path('recipes', recipes, name='recipes'),
    path('recipe_dish/<int:dish_id>/', recipe_dish, name='recipe_dish'),
]
