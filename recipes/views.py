from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
class RecipesListView(ListView):
    model = models.Recipe
