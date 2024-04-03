from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/add', views.add_recipe, name='add_recipe'),
    path('recipes/all', views.all_recipes, name='all_recipes'),
]
