import os
from decimal import Decimal
from io import BytesIO

from django.core.files import File
from django.db import models
from PIL import Image

from .storage import photoStorage

# Create your models here.


class TimestampedModel(models.Model):
    created_at = models.DateTimeField("создан", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("обновлен", auto_now=True, editable=False)

    class Meta:
        abstract = True


class Comment(TimestampedModel):
    STATE_NEW = "new"
    STATE_ACCEPTED = "accepted"
    STATE_REJECTED = "rejected"

    STATE_CHOICES = [
        (STATE_NEW, "новый"),
        (STATE_ACCEPTED, "принят"),
        (STATE_REJECTED, "отклонен"),
    ]

    state = models.CharField(
        "состояние", max_length=8, choices=STATE_CHOICES, blank=False, default=STATE_NEW
    )
    text = models.TextField("текст", blank=False)
    # author = models.ForeignKey(
    #     "auth.User", on_delete=models.CASCADE, related_name="comments"
    # )
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="рецепт",
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        ordering = ("-created_at",)


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


class Category(TimestampedModel):
    name = models.CharField("наименование", max_length=64)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Recipe(TimestampedModel):
    CRUST_LIGHT = "light"
    CRUST_MEDIUM = "medium"
    CRUST_DARK = "dark"

    CRUST_COLOR_CHOICES = [
        (CRUST_LIGHT, "Светлая"),
        (CRUST_MEDIUM, "Средняя"),
        (CRUST_DARK, "Темная"),
    ]

    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
        verbose_name="категория",
        related_name="recipes",
        blank=False,
        null=True,
    )
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
        super().save(*args, **kwargs)

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
    position = models.PositiveIntegerField("№")
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.RESTRICT, verbose_name="ингредиент"
    )
    quantity = models.DecimalField("кол-во", max_digits=10, decimal_places=3)
    measure = models.ForeignKey(Measure, on_delete=models.RESTRICT, verbose_name="ЕИ")
    comment = models.CharField("комментарий", max_length=64, blank=True)

    def volume(self):
        return self.quantity * self.measure.volume

    def weight(self):
        for mw in self.ingredient.measureweight_set.all():
            if mw.measure == self.measure and mw.ingredient == self.ingredient:
                return self.quantity * Decimal(mw.weight)
        return None

    def save(self, *args, **kwargs):
        self.position = self.position or (
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
