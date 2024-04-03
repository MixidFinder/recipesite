import logging

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render

from recipes.forms import AddRecipeForm
from recipes.models import Recipe

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index page called')
    random_recipes = Recipe.objects.order_by('?')[:5]
    context = {'recipes': random_recipes}
    return render(request, 'recipes/index.html', context)


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

            fs = FileSystemStorage()
            fs.save(image.name, image)

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


def all_recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/all_recipes.html', context)
