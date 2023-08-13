from django.contrib.admin import ModelAdmin, site
from .models import RecipeDish, CategoryDish


class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class RecipeDishAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


site.register(RecipeDish, RecipeDishAdmin)
site.register(CategoryDish, CategoryAdmin)
