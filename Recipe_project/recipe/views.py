from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

from .models import Recipe_dish


def index(request):
    list_dish = Recipe_dish.objects.order_by('-published')
    return render(request, 'recipe/index.html',
                  {'list_dish': list_dish[:3]})


def recipes(request):
    list_dish = Recipe_dish.objects.order_by('-published')
    paginator = Paginator(list_dish, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'list_dish': page.object_list, 'page': page,
               'range': range(1, page.paginator.num_pages+1)}
    return render(request, 'recipe/recipes.html', context)


class RecipeDetailView(DetailView):
    """Контроллер-класс для представления деталей рецепта на странице"""
    model = Recipe_dish

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
