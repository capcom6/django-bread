from turtle import mode
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
class RecipesListView(ListView):
    model = models.Recipe

class RecipeDetailsView(DetailView):
    model = models.Recipe
