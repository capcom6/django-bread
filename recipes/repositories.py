import abc
import random
import typing

import django.db.models as djmodels

import recipes.models as models


class BaseRepository(abc.ABC):
    model: djmodels.base.ModelBase

    @classmethod
    def select(cls):
        return cls.model.objects.all()  # type: ignore


class CategoriesRepository(BaseRepository):
    model = models.Category


class ProgramsRepository(BaseRepository):
    model = models.Program


class RecipesRepository(BaseRepository):
    model = models.Recipe

    @classmethod
    def select(cls, *, prefetch_related=True):
        query = super().select()
        if prefetch_related:
            query = query.prefetch_related("ingredients__ingredient")

        return query

    @classmethod
    def get_queryset(cls, *, prefetch_related=True):
        query = cls.select(prefetch_related=prefetch_related)
        if prefetch_related:
            query = query.prefetch_related(
                "ingredients__ingredient__measureweight_set__measure",
                "ingredients__measure",
            )

        return query

    @classmethod
    def get_random(cls) -> typing.Union[models.Recipe, None]:
        max_id = models.Recipe.objects.aggregate(max_id=djmodels.Max("id"))["max_id"]
        if max_id is None:
            return None

        random_id = random.randint(1, max_id)

        return models.Recipe.objects.filter(id__gte=random_id).order_by("id").first()


class CommentsRepository(BaseRepository):
    model = models.Comment

    @classmethod
    def select_for_recipe(
        cls, recipe: models.Recipe, *, state: typing.Union[str, None] = None
    ) -> djmodels.Manager[models.Comment]:
        query = models.Comment.objects.filter(recipe=recipe)
        if state:
            query = query.filter(state=state)
        return query  # type: ignore
