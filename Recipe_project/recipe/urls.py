from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recipes', views.RecipesListView.as_view(), name='recipes'),
    path('category/<slug:category_dish_slug>/',
         views.CategoryListView.as_view(), name='category_dish'),
    path('recipe_dish/<slug:recipe_dish_slug>/',
         views.RecipeDetailView.as_view(), name='recipe_dish'),
    path('create', views.CreateRecipeView.as_view(), name='create_dish'),
    path('api/', include('api.urls')),
    # path('registration', AddNewUser.as_view(), name='registration'),
]
