# Generated by Django 5.0.3 on 2024-04-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_ingredient_name_remove_recipe_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
