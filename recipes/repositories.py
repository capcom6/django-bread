import random
import typing

import django.db.models as djmodels

import recipes.models as models


class RecipesRepository:
    @classmethod
    def get_random(cls) -> typing.Union[models.Recipe, None]:
        max_id = models.Recipe.objects.aggregate(max_id=djmodels.Max("id"))["max_id"]
        random_id = random.randint(1, max_id)

        return models.Recipe.objects.filter(id__gte=random_id).first()
