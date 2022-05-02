from django.contrib import admin

from .models import *


class RecipeIngredientAdminInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    inlines = (RecipeIngredientAdminInline,)


admin.site.register(Recipe, RecipeAdmin)


class MeasureWeightAdminInline(admin.TabularInline):
    model = MeasureWeight


class IngredientAdmin(admin.ModelAdmin):
    inlines = (MeasureWeightAdminInline,)


admin.site.register(Ingredient, IngredientAdmin)

# Register your models here.
admin.site.register([Measure, MeasureWeight, Program, RecipeIngredient, Category])
