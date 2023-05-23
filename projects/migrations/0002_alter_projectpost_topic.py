# Generated by Django 4.2 on 2023-05-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpost',
            name='topic',
            field=models.CharField(choices=[('Machine Learning', 'Machine Learning'), ('BlockChain ', 'BlockChain'), ('3D Art', '3D Art'), ('Side Project', 'Side Project')], max_length=20),
        ),
    ]
