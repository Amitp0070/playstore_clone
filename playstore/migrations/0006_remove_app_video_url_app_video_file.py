# Generated by Django 4.2.6 on 2024-08-25 07:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playstore", "0005_alter_app_video_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="app",
            name="video_url",
        ),
        migrations.AddField(
            model_name="app",
            name="video_file",
            field=models.FileField(
                blank=True,
                upload_to="articles/videos",
                validators=[django.core.validators.URLValidator()],
                verbose_name="Video file",
            ),
        ),
    ]
