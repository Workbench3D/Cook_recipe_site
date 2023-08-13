from django.urls import path, include

from .views import IndexView, RecipesListView, CategoryListView
from .views import RecipeDetailView, CreateRecipeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes', RecipesListView.as_view(), name='recipes'),
    path('category/<slug:category_dish_slug>/',
         CategoryListView.as_view(), name='category_dish'),
    path('recipe_dish/<slug:recipe_dish_slug>/',
         RecipeDetailView.as_view(), name='recipe_dish'),
    path('create', CreateRecipeView.as_view(), name='create_dish'),
]
