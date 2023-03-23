from django.test import TestCase

from recipe.form import RecipeForm


class RecipeFormTest(TestCase):

    def test_fields_form_label(self):
        form_fields = {'name': 0,
                       'description': 1,
                       'ingredients': 2,
                       'recipe': 3,
                       'image': 4,
                       'category': 5,
                       'auhtor': 6}
        for key, value in form_fields.items():
            field = RecipeForm.Meta.fields[value]
            self.assertEqual(field, key)
