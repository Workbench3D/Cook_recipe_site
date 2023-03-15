from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewAddRecipeList.as_view(), name='index'),
    path('recipes', views.RecipesListView.as_view(), name='recipes'),
    path('recipe_dish/<int:pk>/',
         views.RecipeDetailView.as_view(), name='recipe_dish'),
    path('create', views.CreateRecipeView.as_view(), name='create_dish'),
    # path('registration', AddNewUser.as_view(), name='registration'),
]
