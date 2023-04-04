from rest_framework import serializers
from recipe.models import RecipeDish


class RecipeSerializer(serializers.ModelSerializer):
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
