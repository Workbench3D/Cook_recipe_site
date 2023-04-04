from rest_framework import generics
from . import serializers
from recipe.models import RecipeDish, CategoryDish


class RecipesList(generics.ListAPIView):
    """
    Контроллер-класс передающий представления всего списка рецептов блюд
    """
    queryset = RecipeDish.objects.all()
    serializer_class = serializers.RecipeSerializer


class RecipeDetailList(generics.ListAPIView):
    """
    Контроллер-класс передающий представления рецепта блюда
    """
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        recipe_dish_slug = self.kwargs['recipe_dish_slug']
        return RecipeDish.objects.filter(slug=recipe_dish_slug)


class CategoryList(generics.ListAPIView):
    """
    Контроллер-класс передающий представления всего списка рецептов блюд,
    определенной категории блюда
    """
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        category_dish_slug = self.kwargs['category_dish_slug']
        category_name = CategoryDish.objects.get(slug=category_dish_slug)
        return RecipeDish.objects.filter(category=category_name)
