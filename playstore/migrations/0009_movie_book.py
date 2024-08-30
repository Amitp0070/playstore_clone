# Generated by Django 4.2.6 on 2024-08-28 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("playstore", "0008_game"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=100, verbose_name="Movie title")),
                (
                    "image",
                    models.ImageField(
                        upload_to="movies/images", verbose_name="Movie poster image"
                    ),
                ),
                (
                    "content",
                    models.TextField(max_length=200, verbose_name="Movie description"),
                ),
                (
                    "director_name",
                    models.CharField(max_length=100, verbose_name="Director name"),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("rating", models.FloatField(default=0)),
                ("rating_count", models.IntegerField(default=0)),
                (
                    "video_file",
                    models.FileField(
                        upload_to="movies/videos", verbose_name="Trailer file"
                    ),
                ),
                (
                    "likes",
                    models.PositiveIntegerField(default=0, verbose_name="Total likes"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100, verbose_name="Book title")),
                (
                    "image",
                    models.ImageField(
                        upload_to="books/images", verbose_name="Book cover image"
                    ),
                ),
                (
                    "content",
                    models.TextField(max_length=200, verbose_name="Book description"),
                ),
                (
                    "author_name",
                    models.CharField(max_length=100, verbose_name="Author name"),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("rating", models.FloatField(default=0)),
                ("rating_count", models.IntegerField(default=0)),
                (
                    "likes",
                    models.PositiveIntegerField(default=0, verbose_name="Total likes"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
