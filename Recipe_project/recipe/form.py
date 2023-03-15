from django import forms
from django.forms import widgets

from .models import Recipe_dish


class RecipeForm(forms.ModelForm):
    """Форма добавления рецепта блюда"""
    class Meta:
        model = Recipe_dish
        fields = ('name', 'description', 'ingredients',
                  'recipe', 'image', 'category', 'auhtor')
        text_input = widgets.TextInput(attrs={'class': 'form-control'})
        text_area = widgets.Textarea(
                attrs={'class': 'form-control', 'rows': 6})
        file_input = widgets.FileInput(
                attrs={'class': 'form-control', 'type': 'file'})
        select = widgets.Select(
                attrs={'class': 'form-select'})
        widgets = {'name': text_input,
                   'description': text_area,
                   'ingredients': text_area,
                   'recipe': text_area,
                   'image': file_input,
                   'category': select,
                   'auhtor': text_input}
