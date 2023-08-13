from django.db.models import Model, CharField, SlugField, TextField
from django.db.models import DateTimeField, ForeignKey, ImageField, PROTECT
from django.urls import reverse
from recipe.services.utils import unique_slugify


class CategoryDish(Model):
    """Модель категории блюд"""
    name = CharField(max_length=20, primary_key=True,
                            verbose_name='Категория блюда')
    slug = SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name='URL категории блюда')

    def get_absolute_url(self):
        return reverse('category_dish',
                       kwargs={'category_dish_slug': self.slug})

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'category_dish'
        verbose_name_plural = 'Категории блюд'
        verbose_name = 'Категория блюда'
        ordering = ['name']


class RecipeDish(Model):
    """Модель рецептов блюд"""
    name = CharField(max_length=50, verbose_name='Название блюда')
    slug = SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name='URL название блюда')
    description = TextField(null=True, blank=True,
                                   verbose_name='Короткое описание блюда')
    ingredients = TextField(null=True, blank=True,
                                   verbose_name='Список ингредиентов')
    recipe = TextField(null=True, blank=True,
                              verbose_name='Рецепт приготовления')
    published = DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Дата публикации')
    auhtor = CharField(max_length=50, verbose_name='Автор')
    category = ForeignKey(CategoryDish, null=True,
                                 on_delete=PROTECT,
                                 verbose_name='Категория блюда')
    image = ImageField(upload_to='images',
                              verbose_name='Изображение блюда')

    def get_absolute_url(self):
        return reverse('recipe_dish', kwargs={'recipe_dish_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    class Meta():
        db_table = 'recipe_dish'
        verbose_name_plural = 'Рецепты блюд'
        verbose_name = 'Рецепт блюда'
        ordering = ['published']
