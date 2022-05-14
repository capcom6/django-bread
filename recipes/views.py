from django.views.generic import ListView, DetailView
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

    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return (
            models.Recipe.objects.filter(pk=pk)
            .select_related("category", "program")
            .prefetch_related(
                "ingredients__ingredient",
                "ingredients__measure",
            )
        ).get()
