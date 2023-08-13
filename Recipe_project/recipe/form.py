from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, FileInput, Select

from .models import RecipeDish


class RecipeForm(ModelForm):
    """Форма добавления рецепта блюда"""
    class Meta:
        model = RecipeDish
        fields = ('name',
                  'description',
                  'ingredients',
                  'recipe',
                  'image',
                  'category',
                  'auhtor')
        text_input = TextInput(attrs={'class': 'form-control'})
        text_area = Textarea(attrs={'class': 'form-control', 'rows': 6})
        file_input = FileInput(attrs={'class': 'form-control', 'type': 'file'})
        select = Select(attrs={'class': 'form-select'})
        widgets = {'name': text_input,
                   'description': text_area,
                   'ingredients': text_area,
                   'recipe': text_area,
                   'image': file_input,
                   'category': select,
                   'auhtor': text_input}
