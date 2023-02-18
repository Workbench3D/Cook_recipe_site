from django.db import models


class Category_dish(models.Model):
    """Модель категории блюд"""
    name = models.CharField(max_length=20, primary_key=True,
                            verbose_name='Название')

    class Meta:
        db_table = 'category_dish'
        verbose_name_plural = 'Категории блюд'
        verbose_name = 'Категория блюда'
        ordering = ['name']


class Recipe_dish(models.Model):
    """Модель рецептов блюд"""
    name = models.CharField(max_length=50)
    ingredients = models.TextField(null=True, blank=True)
    recipe = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    auhtor = models.CharField(max_length=50)
    category = models.ForeignKey(Category_dish, null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория блюда')
    image = models.ImageField(upload_to='images')

    class Meta():
        db_table = 'recipe_dish'
        verbose_name_plural = 'Рецепты блюд'
        verbose_name = 'Рецепт блюда'
        ordering = ['published']
