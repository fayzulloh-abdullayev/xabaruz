# Generated by Django 5.0.4 on 2024-05-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="slug",
            field=models.SlugField(default="", null=True),
        ),
    ]
