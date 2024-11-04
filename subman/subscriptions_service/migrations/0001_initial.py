# Generated by Django 4.2.16 on 2024-11-04 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('applicable_account_type', models.CharField(choices=[('CONSUMER', 'Consumer'), ('LENDER', 'Lender'), ('FUNDER', 'Funder')], default='CONSUMER', max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='submodules', to='subscriptions_service.module')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('invoicing_country', models.CharField(choices=[('United States', 'United States'), ('Canada', 'Canada'), ('United Kingdom', 'United Kingdom'), ('Japan', 'Japan'), ('Australia', 'Australia'), ('Switzerland', 'Switzerland'), ('China', 'China'), ('India', 'India'), ('Brazil', 'Brazil'), ('Russia', 'Russia'), ('South Africa', 'South Africa'), ('Mexico', 'Mexico'), ('Sweden', 'Sweden'), ('Norway', 'Norway'), ('Denmark', 'Denmark'), ('Singapore', 'Singapore'), ('Hong Kong', 'Hong Kong'), ('New Zealand', 'New Zealand'), ('South Korea', 'South Korea'), ('Saudi Arabia', 'Saudi Arabia'), ('Turkey', 'Turkey'), ('Argentina', 'Argentina'), ('Nigeria', 'Nigeria'), ('Israel', 'Israel'), ('United Arab Emirates', 'Uae'), ('Thailand', 'Thailand'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Cyprus', 'Cyprus'), ('Estonia', 'Estonia'), ('Finland', 'Finland'), ('France', 'France'), ('Germany', 'Germany'), ('Greece', 'Greece'), ('Ireland', 'Ireland'), ('Italy', 'Italy'), ('Latvia', 'Latvia'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Malta', 'Malta'), ('Netherlands', 'Netherlands'), ('Portugal', 'Portugal'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Spain', 'Spain')], default='Denmark', max_length=50)),
                ('invoicing_currency', models.CharField(choices=[('USD', 'US Dollar'), ('CAD', 'Canadian Dollar'), ('GBP', 'Pound Sterling'), ('JPY', 'Yen'), ('AUD', 'Australian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Yuan Renminbi'), ('INR', 'Rupee'), ('BRL', 'Real'), ('RUB', 'Ruble'), ('ZAR', 'Rand'), ('MXN', 'Peso'), ('SEK', 'Swedish Krona'), ('NOK', 'Norwegian Krone'), ('DKK', 'Danish Krone'), ('SGD', 'Singapore Dollar'), ('HKD', 'Hong Kong Dollar'), ('NZD', 'New Zealand Dollar'), ('KRW', 'Won'), ('SAR', 'Riyal'), ('TRY', 'Lira'), ('ARS', 'Peso'), ('NGN', 'Naira'), ('ILS', 'Shekel'), ('AED', 'Dirham'), ('THB', 'Baht'), ('EUR', 'Euro')], default='DKK', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large')], default='SMALL', max_length=50)),
                ('is_monthly', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions_service.subscriptionaccount')),
            ],
        ),
        migrations.CreateModel(
            name='PricingConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('CAD', 'Canadian Dollar'), ('GBP', 'Pound Sterling'), ('JPY', 'Yen'), ('AUD', 'Australian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Yuan Renminbi'), ('INR', 'Rupee'), ('BRL', 'Real'), ('RUB', 'Ruble'), ('ZAR', 'Rand'), ('MXN', 'Peso'), ('SEK', 'Swedish Krona'), ('NOK', 'Norwegian Krone'), ('DKK', 'Danish Krone'), ('SGD', 'Singapore Dollar'), ('HKD', 'Hong Kong Dollar'), ('NZD', 'New Zealand Dollar'), ('KRW', 'Won'), ('SAR', 'Riyal'), ('TRY', 'Lira'), ('ARS', 'Peso'), ('NGN', 'Naira'), ('ILS', 'Shekel'), ('AED', 'Dirham'), ('THB', 'Baht'), ('EUR', 'Euro')], default='DKK', max_length=3)),
                ('tier', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large')], default='SMALL', max_length=50)),
                ('effective_date', models.DateField()),
                ('monthly_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('annual_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='subscriptions_service.module')),
            ],
        ),
        migrations.CreateModel(
            name='PlanModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('custom_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions_service.module')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions_service.subscriptionplan')),
                ('pricing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions_service.pricingconfiguration')),
            ],
        ),
    ]
