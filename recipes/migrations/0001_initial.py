# Generated by Django 4.0.2 on 2022-02-20 09:27

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'ингредиент',
                'verbose_name_plural': 'ингредиенты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='наименование')),
                ('short_name', models.CharField(max_length=32, verbose_name='краткое наименование')),
                ('volume', models.PositiveIntegerField(blank=True, null=True, verbose_name='объем в миллилитрах')),
            ],
            options={
                'verbose_name': 'единицу измерения',
                'verbose_name_plural': 'единицы измерения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='наименование')),
                ('duration', models.DurationField(verbose_name='продолжительность, мин')),
            ],
            options={
                'verbose_name': 'программу',
                'verbose_name_plural': 'программы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='наименование')),
                ('crust', models.CharField(choices=[('light', 'Светлая'), ('medium', 'Средняя'), ('dark', 'Темная')], max_length=8, verbose_name='корочка')),
                ('description', models.TextField(verbose_name='описание')),
                ('weight', models.PositiveIntegerField(verbose_name='вес в граммах')),
                ('photo', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='', verbose_name='фотография')),
            ],
            options={
                'verbose_name': 'рецепт',
                'verbose_name_plural': 'рецепты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(editable=False, verbose_name='№')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='кол-во')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.ingredient', verbose_name='ингредиент')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.measure', verbose_name='ЕИ')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='рецепт')),
            ],
            options={
                'verbose_name': 'ингредиент рецепта',
                'verbose_name_plural': 'ингредиенты рецепта',
                'ordering': ['recipe', 'position'],
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.RecipeIngredient', to='recipes.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.program', verbose_name='программа'),
        ),
        migrations.CreateModel(
            name='MeasureWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(verbose_name='вес в граммах')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.measure')),
            ],
            options={
                'verbose_name': 'вес ЕИ',
                'verbose_name_plural': 'вес ЕИ',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measures',
            field=models.ManyToManyField(through='recipes.MeasureWeight', to='recipes.Measure'),
        ),
        migrations.AddConstraint(
            model_name='recipeingredient',
            constraint=models.UniqueConstraint(fields=('recipe', 'position'), name='unique_recipeingredient_position'),
        ),
        migrations.AddConstraint(
            model_name='measureweight',
            constraint=models.UniqueConstraint(fields=('ingredient', 'measure'), name='unique_ingredient_measure'),
        ),
    ]