from typing import Any
from django.contrib import admin
from django.forms import ModelChoiceField
from django.http import HttpRequest
from django.db.models import ForeignKey

from .models import *


class RecipeIngredientAdminInline(admin.TabularInline):
    model = RecipeIngredient

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("ingredient", "measure")


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    inlines = (RecipeIngredientAdminInline,)


class MeasureWeightAdminInline(admin.TabularInline):
    model = MeasureWeight


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = (MeasureWeightAdminInline,)


# Register your models here.
admin.site.register([Measure, MeasureWeight, Program, RecipeIngredient, Category])
