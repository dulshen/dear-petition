# Generated by Django 2.2.27 on 2022-04-17 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("petition", "0044_auto_20220320_1736"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="petition",
            name="parent",
        ),
    ]