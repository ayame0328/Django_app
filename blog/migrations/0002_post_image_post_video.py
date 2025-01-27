# Generated by Django 4.2.5 on 2024-06-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="post",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to="videos/"),
        ),
    ]
