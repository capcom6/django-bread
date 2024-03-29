# Copyright 2022 Aleksandr Soloshenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from . import views

app_name = "recipes"
urlpatterns = [
    path("", cache_page(60)(views.RecipesListView.as_view()), name="list"),
    path("recipe/random", views.RandomRecipeView.as_view(), name="random"),
    path(
        "recipe/<int:pk>/",
        cache_page(3600)(views.RecipeDetailsView.as_view()),
        name="details",
    ),
    path(
        "recipe/<int:recipe_id>/comment",
        views.CommentAddView.as_view(),
        name="comment_add",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
