# Generated by Django 5.1.1 on 2024-09-06 09:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("expertise", models.CharField(max_length=255)),
                (
                    "introduce",
                    models.TextField(
                        validators=[
                            django.core.validators.MinLengthValidator(100),
                            django.core.validators.MaxLengthValidator(500),
                        ]
                    ),
                ),
                ("nickname", models.CharField(blank=True, max_length=50, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "schedule",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("09:00-10:00", "09:00 - 10:00 AM"),
                            ("10:00-11:00", "10:00 - 11:00 AM"),
                            ("11:00-12:00", "11:00 - 12:00 PM"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
