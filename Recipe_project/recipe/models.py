from django.db import models


class CategoryDish(models.Model):
    """Модель категории блюд"""
    name = models.CharField(max_length=20, primary_key=True,
                            verbose_name='Категория блюда')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'category_dish'
        verbose_name_plural = 'Категории блюд'
        verbose_name = 'Категория блюда'
        ordering = ['name']


class RecipeDish(models.Model):
    """Модель рецептов блюд"""
    name = models.CharField(max_length=50, verbose_name='Название блюда')
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Короткое описание блюда')
    ingredients = models.TextField(null=True, blank=True,
                                   verbose_name='Список ингредиентов')
    recipe = models.TextField(null=True, blank=True,
                              verbose_name='Рецепт приготовления')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Дата публикации')
    auhtor = models.CharField(max_length=50, verbose_name='Автор')
    category = models.ForeignKey(CategoryDish, null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория блюда')
    image = models.ImageField(upload_to='images',
                              verbose_name='Изображение блюда')

    def __str__(self) -> str:
        return self.name

    class Meta():
        db_table = 'recipe_dish'
        verbose_name_plural = 'Рецепты блюд'
        verbose_name = 'Рецепт блюда'
        ordering = ['published']
