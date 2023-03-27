from django.contrib import admin
from .models import RecipeDish, CategoryDish


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class RecipeDishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(RecipeDish, RecipeDishAdmin)
admin.site.register(CategoryDish, CategoryAdmin)
