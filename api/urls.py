from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.SimpleRouter(trailing_slash=False)
# router.register("recipe", views.RecipesViewSet)
router.register("categories", views.CategoriesViewSet)
router.register("programs", views.ProgramsViewSet)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("recipes", views.RecipesListView.as_view(), name="recipe-list"),
    path("recipes/<int:pk>", views.RecipeDetailsView.as_view(), name="recipe-detail"),
    path(
        "recipes/<int:pk>/comments",
        views.CommentsListCreateView.as_view(),
        name="recipe-comments-list",
    ),
]
