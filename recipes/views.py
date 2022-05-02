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

        return query.all()


class RecipeDetailsView(DetailView):
    model = models.Recipe
