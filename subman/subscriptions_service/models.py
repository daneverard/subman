from django.db import models
from django.contrib.auth import get_user_model

class AccountType(models.TextChoices):
    # Consider refactoring as abstract base class for overriding in consumer projects
    CONSUMER = 'CONSUMER', 'Consumer'
    LENDER = 'LENDER', 'Lender'
    FUNDER = 'FUNDER', 'Funder'

class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class Module(models.Model):
    """
    Represents the configuration for an available module within the platform

    Attributes:
        name (OneToOneField): The public and internal name of the module
        applicable_account_types (CharField): which type of account can have access to this module
        name (CharField): The name of the account holder.
        created_at (DateTimeField): The date and time the account was created.

    Methods:
        __str__: Returns a string representation of the account.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    applicable_account_type = models.ForeignKey(AccountType)
    plans = models.ManyToManyField(Plan, related_name='modules', through='PlanModule')

class AddOn(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    applicable_account_types = models.ManyToManyField(AccountType)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='addons')

class CountryCurrency(models.Model):
    country_code = models.CharField(max_length=3)
    currency_code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=5)

class Pricing(models.Model):
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.CASCADE)
    addon = models.ForeignKey(AddOn, null=True, blank=True, on_delete=models.CASCADE)
    country_currency = models.ForeignKey(CountryCurrency, on_delete=models.CASCADE)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    annual_price = models.DecimalField(max_digits=10, decimal_places=2)

class AccountPlan(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class PlanModule(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

class PlanModuleSelectedAddons(models.Model):
    plan_module = models.ForeignKey(PlanModule, on_delete=models.CASCADE)


class Pricing(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    custom_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_monthly = models.BooleanField(default=True)  # True for monthly, False for annual