from django.shortcuts import render

from .models import Recipe_dish


def index(request):
    list_dish = Recipe_dish.objects.order_by('-published')
    return render(request, 'recipe/index.html',
                  {'list_dish': list_dish[:3]})


def recipes(request):
    list_dish = Recipe_dish.objects.order_by('-published')
    context = {'list_dish': list_dish}
    return render(request, 'recipe/recipes.html', context)


def recipe_dish(request):
    list_dish = Recipe_dish.objects.order_by('-published')
    context = {'list_dish': list_dish[0]}
    return render(request, 'recipe/recipe_dish.html', context)
