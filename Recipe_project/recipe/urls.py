from django.urls import path

from .views import index, RecipeDetailView, RecipesListView

urlpatterns = [
    path('', index, name='index'),
    path('recipes', RecipesListView.as_view(), name='recipes'),
    path('recipe_dish/<int:pk>/',
         RecipeDetailView.as_view(), name='recipe_dish'),
]
