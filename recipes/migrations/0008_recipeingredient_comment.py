# Generated by Django 4.0.2 on 2022-05-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_category_recipe_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='comment',
            field=models.CharField(blank=True, max_length=64, verbose_name='комментарий'),
        ),
    ]
