from django import urls
from rest_framework import test

from recipes import models


# Create your tests here.
class ApiTestCase(test.APITestCase):
    fixtures = ["categories.json", "programs.json", "recipes.json", "comments.json"]

    def test_recipe_comments_get(self):
        url = urls.reverse("api:recipe-comments-list", kwargs={"pk": 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data["results"]), 1)
        self.assertEqual(data["results"][0]["text"], "Опубликованный комментарий")

    def test_recipe_comments_post(self):
        url = urls.reverse("api:recipe-comments-list", kwargs={"pk": 1})
        count_before = models.Comment.objects.count()

        response = self.client.post(url, {"text": "test"})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["text"], "test")

        self.assertEqual(models.Comment.objects.count(), count_before + 1)
        self.assertEqual(
            models.Comment.objects.get(text="test").state, models.Comment.STATE_NEW
        )
