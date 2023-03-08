from django.urls import path

from .views import RecipeDetailView, RecipesListView, NewAddRecipeList

urlpatterns = [
    path('', NewAddRecipeList.as_view(), name='index'),
    path('recipes', RecipesListView.as_view(), name='recipes'),
    path('recipe_dish/<int:pk>/',
         RecipeDetailView.as_view(), name='recipe_dish'),
]
