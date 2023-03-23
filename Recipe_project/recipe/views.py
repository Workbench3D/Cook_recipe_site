from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from django.db import connection

from .models import RecipeDish
from .form import RecipeForm


class NewAddRecipeList(ListView):
    """
    Контроллер-класс для представления на страртовом экране списка из трех
    последних добавленных рецептов
    """
    template_name = 'recipe/index.html'
    model = RecipeDish
    ordering = '-published'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        return contex

    def get_queryset(self):
        """
        Изменяем запрос в БД для того чтобы выводить только последние 3
        добавленных рецепта
        """
        context = super().get_queryset()[:3]
        connection.queries
        return context


class RecipesListView(ListView):
    """Контроллер-класс для представления списка всех рецептов на сайте"""
    template_name = 'recipe/recipes.html'
    model = RecipeDish
    paginate_by = 2
    ordering = '-published'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class RecipeDetailView(DetailView):
    """Контроллер-класс для представления деталей рецепта на странице"""
    template_name = 'recipe/recipe_dish.html'
    model = RecipeDish

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


# class AddNewUser(FormView):
#     """Форма для добавления нового пользователя"""
#     template_name = 'recipe/registration.html'
#     form_class = User

#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

#     def get_form(self, form_class):
#         return super().get_form(form_class)

#     def get_success_url(self):
#         return super().get_success_url()

class CreateRecipeView(CreateView):
    """Форма для добавления нового блюда"""
    template_name = 'recipe/create.html'
    form_class = RecipeForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
