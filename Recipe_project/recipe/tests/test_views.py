from django.test import TestCase
from django.urls import reverse

from recipe.models import RecipeDish, CategoryDish


class NewAddRecipeListTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        number_recipe_dish = 4
        category = CategoryDish.objects.create(name='Главный экран',
                                               slug='main-dish')
        for i in range(number_recipe_dish):
            RecipeDish.objects.create(name=f'Главный экран {i}',
                                      slug=f'main-dish-{i}',
                                      description='',
                                      ingredients='',
                                      recipe='',
                                      published='',
                                      auhtor='Шеф',
                                      category=category,
                                      image='images/test.webp')

    def test_index_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_index_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_index_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertTemplateUsed(resp, 'recipe/index.html')

    def test_index_view_queryset_is_three(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.context['object_list'].count(), 3)

    def test_index_view_ordering_is_last_published(self):
        resp = self.client.get(reverse('index'))
        queryset_to_dict = resp.context['object_list'].values()
        last_name = queryset_to_dict[0]['name']
        self.assertEquals(last_name, 'Главный экран 3')


class RecipesListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        number_recipe_dish = 3
        category = CategoryDish.objects.create(name='Все рецепты',
                                               slug='all-recipe')
        for i in range(number_recipe_dish):
            RecipeDish.objects.create(name=f'Все рецепты {i}',
                                      slug=f'all-recipe-{i}',
                                      description='',
                                      ingredients='',
                                      recipe='',
                                      published='',
                                      auhtor='Шеф',
                                      category=category,
                                      image='images/test.webp')

    def test_recipes_view_url_exists_at_desired_location(self):
        resp = self.client.get('/recipes')
        self.assertEqual(resp.status_code, 200)

    def test_recipes_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('recipes'))
        self.assertEqual(resp.status_code, 200)

    def test_recipes_view_uses_correct_template(self):
        resp = self.client.get(reverse('recipes'))
        self.assertTemplateUsed(resp, 'recipe/recipes.html')

    def test_recipes_view_pagination_is_two(self):
        resp = self.client.get(reverse('recipes'))
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(resp.context['object_list'].count() == 2)

    def test_recipes_view_lists_all_recipes(self):
        resp = self.client.get(reverse('recipes')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(resp.context['object_list'].count() == 1)

    def test_recipes_view_ordering_is_last_published(self):
        resp = self.client.get(reverse('recipes'))
        queryset_to_dict = resp.context['object_list'].values()
        last_name = queryset_to_dict[0]['name']
        self.assertEquals(last_name, 'Все рецепты 2')


class RecipeDetailViewTest(TestCase):

    def setUp(self) -> None:
        self.category = CategoryDish.objects.create(name='Рецепт',
                                                    slug='recipe')
        self.recipe_dish = RecipeDish.objects.create(name='Рецепт блюда',
                                                     slug='recipe-dish',
                                                     description='',
                                                     ingredients='',
                                                     recipe='',
                                                     published='',
                                                     auhtor='Шеф',
                                                     category=self.category,
                                                     image='images/test.webp')

    def test_recipe_dish_view_url_accessible_by_name(self):
        resp = self.client.get(
            reverse('recipe_dish',
                    kwargs={'recipe_dish_slug': self.recipe_dish.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_recipe_dish_view_uses_correct_template(self):
        resp = self.client.get(
            reverse('recipe_dish',
                    kwargs={'recipe_dish_slug': self.recipe_dish.slug}))
        self.assertTemplateUsed(resp, 'recipe/recipe_dish.html')
