from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Recipe_dish


class NewAddRecipeList(ListView):
    """
    Контроллер-класс для представления на страртовом экране списка из трех
    последних добавленных рецептов
    """
    template_name = 'recipe/index.html'
    model = Recipe_dish
    paginate_by = 3
    ordering = '-published'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return contex


class RecipesListView(ListView):
    """Контроллер-класс для представления списка всех рецептов на сайте"""
    template_name = 'recipe/recipes.html'
    model = Recipe_dish
    paginate_by = 2
    ordering = '-published'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class RecipeDetailView(DetailView):
    """Контроллер-класс для представления деталей рецепта на странице"""
    template_name = 'recipe/recipe_dish.html'
    model = Recipe_dish

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
