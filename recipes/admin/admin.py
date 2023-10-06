from typing import Any

from django.contrib import admin
from django.http import HttpRequest

from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from ..models import *
from .actions import comment_accept, comment_reject


class RecipeCommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ("text",)
    readonly_fields = ("text",)
    can_delete = True
    verbose_name = "комментарий"
    verbose_name_plural = "комментарии"
    ordering = ("-created_at",)


class RecipeIngredientAdminInline(SortableTabularInline):
    model = RecipeIngredient
    ordering = ["position"]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("ingredient", "measure")


@admin.register(Recipe)
class RecipeAdmin(SortableAdminBase, admin.ModelAdmin):
    list_filter = ("category",)
    search_fields = ("name",)
    inlines = (RecipeIngredientAdminInline, RecipeCommentInline)


class MeasureWeightAdminInline(admin.TabularInline):
    model = MeasureWeight


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = (MeasureWeightAdminInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("state", "recipe", "text", "created_at")
    list_filter = ("state",)
    search_fields = ("text",)
    ordering = ("-created_at",)
    actions = (comment_accept, comment_reject)

    def get_queryset(self, request: HttpRequest) -> Any:
        return super().get_queryset(request).select_related("recipe")


# Register your models here.
admin.site.register([Measure, MeasureWeight, Program, RecipeIngredient, Category])
