# Generated by Django 4.1.5 on 2023-02-14 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_field_projectpost_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectpost',
            old_name='fields',
            new_name='topic',
        ),
    ]