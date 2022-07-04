from typing import Any
from django.contrib import admin
from django.forms import ModelChoiceField
from django.http import HttpRequest
from django.db.models import ForeignKey

from ..models import *


class RecipeCommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ("text",)
    readonly_fields = ("text",)
    can_delete = True
    verbose_name = "комментарий"
    verbose_name_plural = "комментарии"
    ordering = ("-created_at",)


class RecipeIngredientAdminInline(admin.TabularInline):
    model = RecipeIngredient

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("ingredient", "measure")


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    inlines = (RecipeIngredientAdminInline, RecipeCommentInline)


class MeasureWeightAdminInline(admin.TabularInline):
    model = MeasureWeight


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = (MeasureWeightAdminInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("recipe", "text", "created_at")
    list_filter = ("recipe",)
    search_fields = ("text",)
    ordering = ("-created_at",)

    def get_queryset(self, request: HttpRequest) -> Any:
        return super().get_queryset(request).select_related("recipe")


# Register your models here.
admin.site.register([Measure, MeasureWeight, Program, RecipeIngredient, Category])
