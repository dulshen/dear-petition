# Generated by Django 4.2.9 on 2024-08-13 16:29

from django.conf import settings
from django.db import migrations, models, transaction
import django.db.models.deletion
import django.db.models.manager

from dear_petition.petition.management.commands.convert_agency_table import convert_contacts_to_agency_objects

def forwards(apps, schema_editor):
    if schema_editor.connection.alias != "default":
        return

    ContactModel = apps.get_model('petition', 'Contact')
    AgencyModel = apps.get_model('petition', 'Agency')
    convert_contacts_to_agency_objects(ContactModel, AgencyModel)


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("petition", "0063_offenserecord_agency"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="user",
        ),
        migrations.AddField(
            model_name="client",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="The user associated with this contact (only applicable for Clients)",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clients",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Agency",
            fields=[
                (
                    "contact_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="petition.contact",
                    ),
                ),
                ("is_sheriff", models.BooleanField(default=False)),
            ],
            bases=("petition.contact",),
            managers=[
                ("agencies_with_sherriff_office", django.db.models.manager.Manager()),
            ],
        ),
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
