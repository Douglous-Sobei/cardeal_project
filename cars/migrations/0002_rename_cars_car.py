# Generated by Django 4.1.7 on 2023-03-05 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cars",
            new_name="Car",
        ),
    ]
