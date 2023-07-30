from rest_framework import serializers

from recipes import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("pk", "name")


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        fields = ("pk", "name", "duration")


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ("pk", "name")


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measure
        fields = ("short_name", "name")


class RecipeIngredientSerializer(serializers.ModelSerializer):
    measure = MeasureSerializer()
    ingredient = IngredientSerializer()

    class Meta:
        model = models.RecipeIngredient
        fields = (
            "position",
            "ingredient",
            "quantity",
            "measure",
            "volume",
            "weight",
            "comment",
        )


class RecipesListSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = models.Recipe
        fields = (
            "pk",
            "name",
            "crust",
            "description",
            "weight",
            "thumbnail",
            "category",
            "program",
            "ingredients",
            "created_at",
            "updated_at",
        )


class CommentSerializer(serializers.ModelSerializer):
    state = serializers.ReadOnlyField()

    class Meta:
        model = models.Comment
        fields = ("pk", "state", "text", "created_at", "updated_at")


class RecipeDetailsSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)
    # comments = serializers.SerializerMethodField()

    # def get_comments(self, obj):
    #     return CommentSerializer(
    #         obj.comments.filter(state=models.Comment.STATE_ACCEPTED), many=True
    #     ).data

    class Meta:
        model = models.Recipe
        fields = (
            "pk",
            "name",
            "crust",
            "description",
            "weight",
            "thumbnail",
            "category",
            "program",
            "ingredients",
            "comments",
            "created_at",
            "updated_at",
        )
