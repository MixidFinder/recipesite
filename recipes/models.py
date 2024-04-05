from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    default_categories = ['Легко', 'Средне', 'Сложно']
    for category in default_categories:
        Category.objects.get_or_create(name=category)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@receiver(post_migrate)
def create_default_ingredients(sender, **kwargs):
    default_ingredients = [
        'Сахар',
        'Соль',
        'Мука',
        'Растительное масло',
        'Белый хлеб',
        'Яйца',
        'Молоко',
        'Сливочное масло',
        'Сода',
        'Уксус',
        'Лук',
        'Чеснок',
        'Картофель',
        'Морковь',
        'Томаты',
        'Огурцы',
        'Лимон',
        'Яблоки',
        'Бананы',
        'Груши',
        'Перец',
        'Базилик',
        'Петрушка',
        'Укроп',
        'Кинза',
        'Розмарин',
        'Тимьян',
        'Шоколад',
        'Какао',
        'Ваниль',
        'Корица',
        'Мускатный орех',
        'Гвоздика',
        'Имбирь',
        'Карри',
        'Куркума',
        'Паприка',
        'Чили',
        'Соевый соус',
        'Томатный соус',
        'Майонез',
        'Кетчуп',
        'Горчица',
        'Васаби',
        'Сыр',
        'Сметана',
        'Творог',
        'Йогурт',
        'Кефир',
        'Мед',
        'Орехи',
        'Миндаль',
        'Фисташки',
        'Грецкие орехи',
        'Кешью',
        'Арахис',
        'Изюм',
        'Курага',
        'Чернослив',
        'Финики',
        'Мясо',
        'Курица',
        'Рыба',
        'Морепродукты',
        'Бекон',
        'Колбаса',
        'Говядина',
        'Свинина',
        'Баранина',
        'Индейка',
        'Утка',
        'Креветки',
        'Мидии',
        'Кальмары',
        'Лосось',
        'Тунец',
        'Сельдь',
        'Сардина',
        'Треска',
        'Карп',
        'Окунь',
        'Щука',
        'Сом',
        'Осетр',
        'Белуга',
        'Семга',
        'Макароны',
        'Рис',
        'Гречка',
        'Овсянка',
        'Кукуруза',
        'Горох',
        'Фасоль',
        'Чечевица',
        'Соя',
        'Чай',
        'Кофе',
        'Какао',
        'Сок',
        'Вода',
        'Молоко',
        'Кефир',
        'Компот',
        'Квас',
    ]
    for ingredient in default_ingredients:
        Ingredient.objects.get_or_create(name=ingredient)


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200)
    steps = models.TextField(max_length=10000)
    preparation_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
