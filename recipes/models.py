from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000)
    steps = models.TextField(max_length=1000)
    preparation_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(RecipeCategory)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
