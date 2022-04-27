from decimal import Decimal
from io import BytesIO
import os
from pathlib import Path
from django.db import models
from .storage import photoStorage
from PIL import Image
from django.core.files import File

# Create your models here.


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Measure(TimestampedModel):
    name = models.CharField("наименование", max_length=32, unique=True)
    short_name = models.CharField("краткое наименование", max_length=32)
    volume = models.PositiveIntegerField("объем в миллилитрах", null=True, blank=True)

    def __str__(self):
        if self.volume:
            return f"{self.name} ({self.volume} мл)"
        else:
            return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "единицу измерения"
        verbose_name_plural = "единицы измерения"


class Ingredient(TimestampedModel):
    name = models.CharField(max_length=64, unique=True)
    measures = models.ManyToManyField(Measure, through="MeasureWeight")

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "ингредиент"
        verbose_name_plural = "ингредиенты"


class MeasureWeight(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    weight = models.FloatField("вес в граммах")

    def __str__(self) -> str:
        return f"1 {self.measure.short_name} {self.ingredient.name} = {self.weight} гр."

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["ingredient", "measure"], name="unique_ingredient_measure"
            )
        ]
        verbose_name = "вес ЕИ"
        verbose_name_plural = "вес ЕИ"


class Program(TimestampedModel):
    name = models.CharField("наименование", max_length=64, unique=True)
    duration = models.DurationField("продолжительность, мин")

    def __str__(self) -> str:
        return f"{self.name} ({self.duration})"

    class Meta:
        ordering = ["name"]
        verbose_name = "программу"
        verbose_name_plural = "программы"


class Recipe(TimestampedModel):
    CRUST_LIGHT = "light"
    CRUST_MEDIUM = "medium"
    CRUST_DARK = "dark"

    CRUST_COLOR_CHOICES = [
        (CRUST_LIGHT, "Светлая"),
        (CRUST_MEDIUM, "Средняя"),
        (CRUST_DARK, "Темная"),
    ]

    name = models.CharField("наименование", max_length=64, unique=True)
    crust = models.CharField(
        "корочка", max_length=8, choices=CRUST_COLOR_CHOICES, blank=True
    )
    description = models.TextField("описание")
    program = models.ForeignKey(
        Program, on_delete=models.RESTRICT, verbose_name="программа"
    )
    weight = models.PositiveIntegerField("вес в граммах")
    photo = models.ImageField("фотография", blank=True, null=True, storage=photoStorage)
    thumbnail = models.ImageField(
        "фотография", blank=True, null=True, storage=photoStorage, editable=False
    )
    steps = models.TextField("подготовка", blank=True)
    after = models.TextField("завершение", blank=True)

    def save(self, *args, **kwargs) -> None:

        if self.photo and not (
            self.thumbnail
            and self.thumbnail.name.startswith(self.photo.name + "_thumb")
        ):
            buffer = BytesIO()

            img = Image.open(self.photo)
            img.thumbnail(
                (
                    256,
                    256,
                )
            )
            img.save(buffer, "JPEG")

            self.thumbnail = File(
                buffer, os.path.splitext(self.photo.name)[0] + "_thumb.jpg"
            )
        super().save(args, kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "рецепт"
        verbose_name_plural = "рецепты"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="рецепт",
        related_name="ingredients",
    )
    position = models.PositiveIntegerField("№", editable=False)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.RESTRICT, verbose_name="ингредиент"
    )
    quantity = models.DecimalField("кол-во", max_digits=10, decimal_places=3)
    measure = models.ForeignKey(Measure, on_delete=models.RESTRICT, verbose_name="ЕИ")

    def volume(self):
        return self.quantity * self.measure.volume

    def weight(self):
        mw = (
            MeasureWeight.objects.all()
            .filter(
                ingredient=self.ingredient,
                measure=self.measure,
            )
            .get()
        )
        if not mw:
            return None
        return self.quantity * Decimal(mw.weight)

    def save(self, *args, **kwargs):
        self.position = (
            RecipeIngredient.objects.all().filter(recipe=self.recipe).count() + 1
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} {self.measure.name} {self.ingredient.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "position"], name="unique_recipeingredient_position"
            )
        ]
        ordering = ["recipe", "position"]
        verbose_name = "ингредиент рецепта"
        verbose_name_plural = "ингредиенты рецепта"
