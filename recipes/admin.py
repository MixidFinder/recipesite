from django.contrib import admin

from recipes import models


class CategorytAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class IngredientAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
    ordering = ['creation_date']
    search_fields = ['name', 'author']


# Register your models here.
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Category, CategorytAdmin)
