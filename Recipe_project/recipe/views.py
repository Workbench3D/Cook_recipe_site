from django.shortcuts import render

from .models import Recipe_dish


def index(request):
    list_dish = Recipe_dish.objects.order_by('-published')
    return render(request, 'recipe/index.html',
                  {'list_dish': list_dish})
