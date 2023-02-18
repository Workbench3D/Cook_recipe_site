from django.contrib import admin
from .models import Recipe_dish, Category_dish

admin.site.register(Recipe_dish)
admin.site.register(Category_dish)
