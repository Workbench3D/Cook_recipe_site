from rest_framework.serializers import ModelSerializer
from recipe.models import RecipeDish


class RecipeSerializer(ModelSerializer):
    """Сериализатор рецепта блюда"""
    class Meta:
        model = RecipeDish
        fields = ('name',
                  'description',
                  'ingredients',
                  'recipe',
                  'published',
                  'auhtor',
                  'category',
                  'image')
