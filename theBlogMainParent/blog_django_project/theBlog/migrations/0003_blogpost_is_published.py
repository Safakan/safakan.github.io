# Generated by Django 4.2.5 on 2023-09-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("theBlog", "0002_blogpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]
