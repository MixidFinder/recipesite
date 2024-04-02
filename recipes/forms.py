from django import forms

from recipes.models import Recipe


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'category',
            'name',
            'description',
            'ingredients',
            'steps',
            'preparation_time',
            'image',
        ]
        widgets = {
            'category': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название рецепта',
                }
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Введите описание'}
            ),
            'ingredients': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            ),
            'steps': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                }
            ),
            'preparation_time': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Время приготовления (в минутах)',
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
