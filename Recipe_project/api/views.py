from rest_framework.generics import ListAPIView
from .serializers import RecipeSerializer
from recipe.models import RecipeDish, CategoryDish


class RecipesList(ListAPIView):
    """
    Контроллер-класс передающий представления всего списка рецептов блюд
    """
    queryset = RecipeDish.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailList(ListAPIView):
    """
    Контроллер-класс передающий представления рецепта блюда
    """
    serializer_class = RecipeSerializer

    def get_queryset(self):
        recipe_dish_slug = self.kwargs['recipe_dish_slug']
        return RecipeDish.objects.filter(slug=recipe_dish_slug)


class CategoryList(ListAPIView):
    """
    Контроллер-класс передающий представления всего списка рецептов блюд,
    определенной категории блюда
    """
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category_dish_slug = self.kwargs['category_dish_slug']
        category_name = CategoryDish.objects.get(slug=category_dish_slug)
        return RecipeDish.objects.filter(category=category_name)
