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

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from ..models import Recipe


class RecipesTestCase(TestCase):
    fixtures = ["categories.json", "programs.json", "recipes.json"]

    def test_recipes_list(self):
        response: HttpResponse = self.client.get(reverse("recipes:list"))  # type: ignore

        recipes = Recipe.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_list.html")
        self.assertCountEqual(response.context["object_list"], recipes)

    def test_recipes_list_category(self):
        response: HttpResponse = self.client.get(
            reverse("recipes:list"), {"category": 1}
        )  # type: ignore

        recipes = Recipe.objects.filter(category__id=1)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_list.html")
        self.assertCountEqual(response.context["object_list"], recipes)

    def test_recipes_details(self):
        response: HttpResponse = self.client.get(
            reverse("recipes:details", kwargs={"pk": 1})
        )  # type: ignore

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_detail.html")
        self.assertEqual(response.context["object"], Recipe.objects.get(id=1))

    def test_recipes_random(self) -> None:
        response = self.client.get(reverse("recipes:random"))

        self.assertEqual(response.status_code, 302)

        # self.assertRedirects(
        #     response,
        #     reverse("recipes:details", kwargs={"pk": 1}),
        #     status_code=302,
        # )

    def test_recipes_random_404(self) -> None:
        Recipe.objects.all().delete()

        response = self.client.get(reverse("recipes:random"))
        self.assertEqual(response.status_code, 404)

    def test_recipes_details_404(self):
        response: HttpResponse = self.client.get(
            reverse("recipes:details", kwargs={"pk": 100})
        )  # type: ignore

        self.assertEqual(response.status_code, 404)
