# Generated by Django 3.2.13 on 2023-06-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("petition", "0056_offenserecord_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="ciprsrecord",
            name="has_additional_offenses",
            field=models.BooleanField(default=False),
        ),
    ]
