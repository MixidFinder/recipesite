import logging

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from recipes.forms import AddRecipeForm, EditRecipeForm
from recipes.models import Recipe

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index page called')
    random_recipes = Recipe.objects.order_by('?')[:6]
    context = {'recipes': random_recipes}
    return render(request, 'recipes/index.html', context)


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe.html', {'recipe': recipe})


# Create your views here.
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            steps = form.cleaned_data['steps']
            preparation_time = form.cleaned_data['preparation_time']
            image = form.cleaned_data['image']

            logger.info(
                f'Получили {name=}, {description=}, {steps=} {preparation_time=}, {image=}.'
            )

            recipe = Recipe(
                category=category,
                name=name,
                description=description,
                steps=steps,
                preparation_time=preparation_time,
                image=image,
                author=request.user,
            )

            recipe.save()

            recipe.ingredients.set(ingredients)

            messages.success(request, f'Рецепт: {name}, успешно создан!')

            return redirect('/')
    else:
        form = AddRecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form})


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if recipe.author != request.user:
        messages.success(request, 'Вы не можете редактировать данный рецепт')
        return redirect('/')

    if request.method == 'POST':
        form = EditRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, f'Рецепт "{recipe.name}" успешно обновлен!')
            return redirect('/')
    else:
        form = EditRecipeForm(instance=recipe)

    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if recipe.author != request.user:
        messages.success(request, 'Вы не можете удалить данный рецепт')
        return redirect('/')

    recipe.delete()

    messages.success(request, f'Рецепт "{recipe.name}" успешно удален!')

    return redirect('/')


def user_recipes(request, username):
    user = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(author=user)

    return render(
        request,
        'recipes/user_recipes.html',
        {'recipes': recipes, 'username': username},
    )


def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/all_recipes.html', context)
