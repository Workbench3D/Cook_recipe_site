from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('recipes/', views.RecipesList.as_view()),
    path('recipe_dish/<slug:recipe_dish_slug>/',
         views.RecipeDetailList.as_view()),
    path('category/<slug:category_dish_slug>/',
         views.CategoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)