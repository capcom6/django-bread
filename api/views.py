from django import http, shortcuts
from rest_framework import generics, viewsets
from api import serializers

from recipes import models, repositories


# Create your views here.
class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = repositories.CategoriesRepository.select()
    serializer_class = serializers.CategorySerializer


class ProgramsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = repositories.ProgramsRepository.select()
    serializer_class = serializers.ProgramSerializer


class RecipesListView(generics.ListAPIView):
    queryset = repositories.RecipesRepository.select()
    serializer_class = serializers.RecipesListSerializer


class RecipeDetailsView(generics.RetrieveAPIView):
    queryset = repositories.RecipesRepository.get_queryset()
    serializer_class = serializers.RecipeDetailsSerializer


class CommentsListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def _get_recipe(self) -> models.Recipe:
        recipe_id = self.kwargs.get("pk")

        return shortcuts.get_object_or_404(
            repositories.RecipesRepository.get_queryset(prefetch_related=False),
            pk=recipe_id,
        )

    def get_queryset(self):
        recipe = self._get_recipe()

        return repositories.CommentsRepository.select_for_recipe(
            recipe=recipe, state=models.Comment.STATE_ACCEPTED
        )

    def perform_create(self, serializer):
        recipe = self._get_recipe()

        serializer.save(recipe=recipe)
