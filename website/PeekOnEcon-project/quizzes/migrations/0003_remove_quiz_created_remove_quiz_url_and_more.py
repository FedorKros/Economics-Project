# Generated by Django 4.2.2 on 2023-11-05 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0002_remove_quiz_datecompleted"),
    ]

    operations = [
        migrations.RemoveField(model_name="quiz", name="created",),
        migrations.RemoveField(model_name="quiz", name="url",),
        migrations.AlterField(
            model_name="quiz", name="description", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="quiz", name="title", field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name="Question",
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
                ("text", models.CharField(max_length=255)),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="quizzes.quiz",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Choice",
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
                ("text", models.CharField(max_length=255)),
                ("is_correct", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="choices",
                        to="quizzes.question",
                    ),
                ),
            ],
        ),
    ]
