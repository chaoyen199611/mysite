# Generated by Django 4.1.5 on 2023-06-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_postbase_description_alter_postbase_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postbase',
            name='description',
            field=models.TextField(blank=True, default='default', null=True),
        ),
    ]