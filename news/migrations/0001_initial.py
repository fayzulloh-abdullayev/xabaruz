# Generated by Django 5.0.4 on 2024-05-02 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("slug", models.SlugField()),
                ("image", models.ImageField(upload_to="news")),
                ("text", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                (
                    "publish",
                    models.CharField(
                        choices=[("Bekor qilish", "Cancel"), ("To'g'ri", "Success")],
                        default="Bekor qilish",
                        max_length=30,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="news.category"
                    ),
                ),
            ],
        ),
    ]