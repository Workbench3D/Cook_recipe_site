from django.urls import path

from .views import index, recipes, RecipeDetailView

urlpatterns = [
    path('', index, name='index'),
    path('recipes', recipes, name='recipes'),
    path('recipe_dish/<int:pk>/',
         RecipeDetailView.as_view(), name='recipe_dish'),
]
