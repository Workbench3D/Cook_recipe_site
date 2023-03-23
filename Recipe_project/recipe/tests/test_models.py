from django.test import TestCase

from recipe.models import RecipeDish, CategoryDish


class RecipeDishModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        RecipeDish.objects.create(name='Блюдо',
                                  description='',
                                  ingredients='',
                                  recipe='',
                                  published='',
                                  auhtor='Шеф',
                                  category=CategoryDish.objects.create(
                                       name='Блюдо'),
                                  image='images/test.webp')

    def test_model_label(self):
        model_label = {'name': 'Название блюда',
                       'description': 'Короткое описание блюда',
                       'ingredients': 'Список ингредиентов',
                       'recipe': 'Рецепт приготовления',
                       'published': 'Дата публикации',
                       'auhtor': 'Автор',
                       'category': 'Категория блюда'}
        recipe_dish = RecipeDish.objects.get(id=1)
        for key, value in model_label.items():
            field_label = recipe_dish._meta.get_field(key).verbose_name
            self.assertEquals(field_label, value)


class CategoryDishModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        CategoryDish.objects.create(name='Категория')

    def test_name_label(self):
        recipe_dish = CategoryDish.objects.get(name='Категория')
        field_label = recipe_dish._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Категория блюда')
