# Generated by Django 4.1.7 on 2023-04-26 16:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "topic_name",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MaxLengthValidator(5)],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Webpage",
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
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(5),
                            django.core.validators.MaxLengthValidator(10),
                        ],
                    ),
                ),
                ("url", models.URLField()),
                (
                    "topic_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.topic"
                    ),
                ),
            ],
        ),
    ]
