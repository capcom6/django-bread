# Generated by Django 4.0.2 on 2022-04-27 13:37

from django.db import migrations, models
import recipes.storage


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_after_recipe_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='crust',
            field=models.CharField(blank=True, choices=[('light', 'Светлая'), ('medium', 'Средняя'), ('dark', 'Темная')], max_length=8, verbose_name='корочка'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=recipes.storage.PhotoStorage(), upload_to='', verbose_name='фотография'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, storage=recipes.storage.PhotoStorage(), upload_to='', verbose_name='фотография'),
        ),
    ]
