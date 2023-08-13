from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RecipesList, RecipeDetailList, CategoryList

urlpatterns = [
    path('recipes/', RecipesList.as_view()),
    path('recipe_dish/<slug:recipe_dish_slug>/',
         RecipeDetailList.as_view()),
    path('category/<slug:category_dish_slug>/',
         CategoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)