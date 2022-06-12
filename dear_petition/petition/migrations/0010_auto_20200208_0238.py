# Generated by Django 2.2.4 on 2020-02-08 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("petition", "0009_auto_20200208_0237"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="batch",
            name="records",
        ),
        migrations.AlterField(
            model_name="ciprsrecord",
            name="batch",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="records",
                to="petition.Batch",
            ),
        ),
    ]
