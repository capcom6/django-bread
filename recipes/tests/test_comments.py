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

from django.http import HttpResponse, HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from ..models import Comment


class CommentsTestCase(TestCase):
    fixtures = ["categories.json", "programs.json", "recipes.json", "comments.json"]

    RECIPE_ADD_ID = 2

    def test_add_comment(self):
        response: HttpResponseRedirect = self.client.post(reverse("recipes:comment_add", kwargs={"recipe_id": self.RECIPE_ADD_ID}), {"text": "test"})  # type: ignore

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url, reverse("recipes:details", kwargs={"pk": self.RECIPE_ADD_ID})
        )

        comments = Comment.objects.filter(recipe_id=self.RECIPE_ADD_ID)

        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0].text, "test")
        self.assertEqual(comments[0].state, Comment.STATE_NEW)

    def test_public_comments_list(self):
        response: HttpResponse = self.client.get(reverse("recipes:details", kwargs={"pk": 1}))  # type: ignore

        comments = list(
            Comment.objects.filter(recipe_id=1, state=Comment.STATE_ACCEPTED).all()
        )

        self.assertEqual(response.status_code, 200)

        self.assertListEqual(list(response.context["comments"]), comments)

    def test_comments_str(self) -> None:
        comment = Comment.objects.get(id=1)
        self.assertEqual(str(comment), comment.text)
