# Generated by Django 4.2.6 on 2024-08-26 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("playstore", "0007_alter_app_video_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("title", models.CharField(max_length=100, verbose_name="Game title")),
                (
                    "image",
                    models.ImageField(
                        upload_to="games/images", verbose_name="Game image"
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("rating", models.FloatField(default=0)),
                ("rating_count", models.IntegerField(default=0)),
                (
                    "video_file",
                    models.FileField(
                        upload_to="games/videos", verbose_name="Video file"
                    ),
                ),
                (
                    "likes",
                    models.PositiveIntegerField(default=0, verbose_name="Total likes"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="playstore.device",
                    ),
                ),
            ],
        ),
    ]
