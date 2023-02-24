from django.shortcuts import render
from django.core.paginator import Paginator

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


def recipe_dish(request, dish_id):
    recipe_dish = Recipe_dish.objects.get(id=dish_id)
    context = {'recipe_dish': recipe_dish}
    return render(request, 'recipe/recipe_dish.html', context)
