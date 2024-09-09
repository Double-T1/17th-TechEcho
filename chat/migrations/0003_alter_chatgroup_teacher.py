# Generated by Django 5.1.1 on 2024-09-08 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_alter_groupmessage_options_and_more"),
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatgroup",
            name="teacher",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="teachers.teacher"
            ),
        ),
    ]
