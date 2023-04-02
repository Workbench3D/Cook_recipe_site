from django.test import TestCase

from recipe.models import RecipeDish, CategoryDish

class ServicesUtilsTest(TestCase):
    number_recipe_dish = 10

    def setUp(self) -> None:
        category = CategoryDish.objects.create(name='Уникальная категория',
                                               slug='unikalnaya-kategoriya')
        for i in range(self.number_recipe_dish):
            RecipeDish.objects.create(name='Уникальный',
                                      description='',
                                      ingredients='',
                                      recipe='',
                                      published='',
                                      auhtor='Шеф',
                                      category=category,
                                      image='images/test.webp')  

    def test_unique_slugify(self):
        recipes = RecipeDish.objects.filter(name='Уникальный')
        list_slug = [i.slug for i in recipes]
        count_uniq_dishes = len(set(list_slug))
        self.assertEqual(count_uniq_dishes, self.number_recipe_dish)
