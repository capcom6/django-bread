# Copyright 2022 Aleksandr Soloshenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict

from django.contrib.messages.views import SuccessMessageMixin
import django.http as http
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from recipes import repositories

from . import forms, models


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

        return get_object_or_404(
            models.Recipe.objects.filter(pk=pk)
            .select_related("category", "program")
            .prefetch_related(
                "ingredients__ingredient",
                "ingredients__ingredient__measureweight_set__measure",
                "ingredients__measure",
            )
        )


class RandomRecipeView(View):
    def get(self, request: http.HttpRequest, *args, **kwargs) -> http.HttpResponse:
        recipe = repositories.RecipesRepository.get_random()
        if not recipe:
            raise http.Http404()

        return http.HttpResponseRedirect(
            reverse("recipes:details", kwargs={"pk": recipe.pk})
        )


class CommentAddView(SuccessMessageMixin, CreateView):
    model = models.Comment
    form_class = forms.CommentForm
    success_message: str = "Комментарий добавлен. Он будет отображен после модерации."

    def post(self, request: http.HttpRequest, *args, **kwargs) -> http.HttpResponse:
        if "recipe_id" not in kwargs:
            return http.HttpResponseBadRequest()
        recipe_id = kwargs["recipe_id"]
        self.recipe = models.Recipe.objects.get(pk=recipe_id)
        if not self.recipe:
            return http.HttpResponseNotFound()

        return super().post(request, *args, **kwargs)

    def form_valid(self, form: forms.CommentForm):
        form.instance.recipe = self.recipe
        # form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("recipes:details", kwargs={"pk": self.recipe.pk})
