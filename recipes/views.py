from typing import Any, Dict
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from django.urls import resolve, reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from . import forms
from . import models

# Create your views here.
class RecipesListView(ListView):
    model = models.Recipe

    def get_queryset(self):
        category_id = self.request.GET.get("category")

        query = models.Recipe.objects
        if category_id:
            query = query.filter(category__id=category_id)

        return query.prefetch_related("category", "ingredients__ingredient").all()


class RecipeDetailsView(DetailView):
    model = models.Recipe

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        kwargs["comment_form"] = forms.CommentForm()

        data = super().get_context_data(**kwargs)

        data["comments"] = models.Comment.objects.filter(
            recipe=data["object"], state=models.Comment.STATE_ACCEPTED
        )

        return data

    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return (
            models.Recipe.objects.filter(pk=pk)
            .select_related("category", "program")
            .prefetch_related(
                "ingredients__ingredient",
                "ingredients__ingredient__measureweight_set__measure",
                "ingredients__measure",
            )
        ).get()


class CommentAddView(CreateView):
    model = models.Comment
    form_class = forms.CommentForm

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if "recipe_id" not in kwargs:
            return HttpResponseBadRequest()
        recipe_id = kwargs["recipe_id"]
        self.recipe = models.Recipe.objects.get(pk=recipe_id)
        if not self.recipe:
            return HttpResponseNotFound()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.recipe = self.recipe
        # form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("recipes:details", kwargs={"pk": self.recipe.pk})
