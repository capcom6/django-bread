from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class RecipesListView(ListView):
    model = models.Recipe

class RecipeDetailsView(DetailView):
    model = models.Recipe
