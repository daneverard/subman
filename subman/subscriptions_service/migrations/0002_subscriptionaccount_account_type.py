# Generated by Django 4.2.16 on 2025-03-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionaccount',
            name='account_type',
            field=models.CharField(choices=[('CONSUMER', 'Consumer'), ('LENDER', 'Lender'), ('FUNDER', 'Funder')], default='CONSUMER', max_length=50),
        ),
    ]
