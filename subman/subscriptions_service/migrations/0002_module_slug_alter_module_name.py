# Generated by Django 4.2.16 on 2024-11-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
