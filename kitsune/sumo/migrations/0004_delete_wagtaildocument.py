# Generated by Django 4.2.16 on 2024-10-14 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sumo", "0003_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="WagtailDocument",
        ),
    ]