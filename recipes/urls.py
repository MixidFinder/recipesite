from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/add', views.add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/edit', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:recipe_id>/delete', views.delete_recipe, name='delete_recipe'),
    path('recipes/<int:recipe_id>', views.recipe, name='recipe'),
    path('recipes/all', views.all_recipes, name='all_recipes'),
    path('recipes/<str:username>', views.user_recipes, name='user_recipes'),
]
