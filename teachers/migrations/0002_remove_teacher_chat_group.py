# Generated by Django 5.1.1 on 2024-09-18 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="chat_group",
        ),
    ]
