# Generated by Django 4.1.10 on 2023-10-06 16:04

from django.db import migrations, models
import recipes.storage


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0011_alter_comment_options_alter_category_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="position",
            field=models.PositiveIntegerField(verbose_name="№"),
        ),
        migrations.AddIndex(
            model_name="recipeingredient",
            index=models.Index(
                fields=["recipe", "position"], name="idx_recipeingredient_position"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="recipeingredient",
            name="unique_recipeingredient_position",
        ),
    ]
