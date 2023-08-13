from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db import connection

from .models import RecipeDish, CategoryDish
from .form import RecipeForm


class IndexView(ListView):
    """
    Контроллер-класс для представления страртового экрана
    """
    template_name = 'recipe/index.html'
    model = RecipeDish
    ordering = '-published'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryDish.objects.all()
        return context

    def get_queryset(self):
        """
        Изменяем запрос в БД для того чтобы выводить только последние 3
        добавленных рецепта
        """
        query = super().get_queryset()[:3]
        connection.queries
        return query


class RecipesListView(ListView):
    """Контроллер-класс для представления списка всех рецептов на сайте"""
    template_name = 'recipe/recipes.html'
    model = RecipeDish
    paginate_by = 2
    ordering = '-published'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CategoryListView(ListView):
    """
    Контроллер-класс для представления списка блюд по категориям на сайте
    использует слаг модели
    """
    template_name = 'recipe/category_dish.html'
    model = RecipeDish
    paginate_by = 2
    ordering = '-published'
    slug_field = 'slug'
    slug_url_kwarg = 'category_dish_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryDish.objects.get(
            slug=self.kwargs['category_dish_slug'])
        return context

    def get_queryset(self):
        category_name = CategoryDish.objects.get(
            slug=self.kwargs['category_dish_slug'])
        query = RecipeDish.objects.filter(
            category=category_name)
        return query


class RecipeDetailView(DetailView):
    """Контроллер-класс для представления деталей рецепта на странице"""
    template_name = 'recipe/recipe_dish.html'
    model = RecipeDish
    slug_field = 'slug'
    slug_url_kwarg = 'recipe_dish_slug'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CreateRecipeView(CreateView):
    """Форма для добавления нового блюда"""
    template_name = 'recipe/create.html'
    form_class = RecipeForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
