# Generated by Django 4.1.5 on 2023-02-18 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_fields_projectpost_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPostSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(blank=True, max_length=100, null=True)),
                ('section_context', models.TextField(blank=True, null=True)),
                ('section_image', models.ImageField(blank=True, null=True, upload_to='images/projects/')),
                ('belongPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectpost')),
            ],
        ),
    ]