# Generated by Django 4.2.2 on 2023-11-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quiz",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("datecompleted", models.DateTimeField(blank=True, null=True)),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]
