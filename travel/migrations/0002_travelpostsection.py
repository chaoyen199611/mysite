# Generated by Django 4.1.5 on 2023-04-14 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPostSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_num', models.IntegerField(null=True)),
                ('section_title', models.CharField(blank=True, max_length=100, null=True)),
                ('section_context', models.TextField(blank=True, null=True)),
                ('section_image', models.ImageField(blank=True, null=True, upload_to='images/travels/')),
                ('belongPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.travelpost')),
            ],
        ),
    ]
