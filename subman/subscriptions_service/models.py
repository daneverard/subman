from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .util import logging
from .util.country_currency import country_to_currency, CountryChoices, CurrencyChoices
from .util.subscription_config import AccountType, PricingTiers

logger = logging.get_logger(__name__)

class SubscriptionAccount(models.Model):
    name = models.CharField(max_length=255)
    invoicing_country = models.CharField(
        max_length=50,
        choices=CountryChoices.choices,
        default=CountryChoices.DENMARK,
    )
    invoicing_currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices.choices,
        default=country_to_currency[CountryChoices.DENMARK],
    )
    account_type = models.CharField(
        max_length=50,
        choices=AccountType.choices,
        default=AccountType.choices[0][0],
    )

    @staticmethod
    def get_active_modules_for_account(account: SubscriptionAccount):
        plans = SubscriptionPlan.objects.filter(account=account)
        modules = PlanModule.objects.filter(
                plan__in = plans
            )
        return [module.slug for module in modules]

    def __str__(self):
        return f"{self.name} ({self.invoicing_country},{self.invoicing_currency})"

class Module(models.Model):
    """ Represents the configuration for an available module within the platform """
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True,
        on_delete=models.PROTECT,
        related_name='submodules'
        )
    description = models.TextField(blank=True)
    applicable_account_type = models.CharField(
        max_length=50,
        choices=AccountType.choices,
        default=AccountType.choices[0][0],
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    @staticmethod
    def get_available_modules_for_account_list(account: SubscriptionAccount):
        """Get a list of available module slugs for a given account."""
        try:
            modules = Module.objects.filter(
                applicable_account_type=account.account_type
            )
            return [module.slug for module in modules]
        except ObjectDoesNotExist:
            return []

    @staticmethod
    def get_all_available_modules_list():
        """Get a list of all module slugs."""
        try:
            modules = Module.objects.all()
            return [module.slug for module in modules]
        except ObjectDoesNotExist:
            return []

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug from the name field
            base_slug = slugify(self.name).upper()
            slug = base_slug
            num = 2

            # Ensure the slug is unique by appending a number if it already exists
            while Module.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def get_active_pricing(self):
        today = timezone.now().date()
        try:
            active_pricing = PricingConfiguration.objects.filter(module=self, effective_date__lte=today).order_by('-effective_date').first()
            return active_pricing
        except ObjectDoesNotExist:
            logger.WARN("No active pricing configuration!")

    def __str__(self):
        return f"{self.parent}.{self.name}" if self.parent else self.name

class PricingConfiguration(models.Model):
    """ 
    A "WORM" read-only model representing a pricing configuration for a module or add-on
    Updating base pricing requires that a new pricing instance is created with the appropriate effecrtive_date
    An account's pricing will be based upon a specific instance of the pricing, to be updated when a plan renews
    """
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.PROTECT)
    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices.choices,
        default=CurrencyChoices.DKK,
    )
    tier = models.CharField(
        max_length=50,
        choices=PricingTiers.choices,
        default=PricingTiers.choices[0][0],
    )
    effective_date = models.DateField()
    monthly_price = models.DecimalField(max_digits=15, decimal_places=2)
    annual_price = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.pk:  # Instance exists, prevent update
            raise ValidationError("This record is read-only and cannot be modified.")
        super().save(*args, **kwargs)  # Allow creation if no primary key (first save only)

    def delete(self, *args, **kwargs):
        raise ValidationError("This record is read-only and cannot be deleted.")
    
    def __str__(self):
        return f"{self.module}:{self.currency}:{self.tier}:{self.effective_date}"


class SubscriptionPlan(models.Model):
    account = models.ForeignKey(SubscriptionAccount, on_delete=models.PROTECT)
    tier = models.CharField(
        max_length=50,
        choices=PricingTiers.choices,
        default=PricingTiers.choices[0][0],
    )
    is_monthly = models.BooleanField(default=True)  # True for monthly, False for annual
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    @property
    def is_active(self):
        return self.start_date < timezone.now().date() < self.end_date if self.end_date else self.start_date < timezone.now().date()

    def __str__(self):
        return f"{self.account.name}:{self.tier}:{self.start_date}"

class PlanModule(models.Model):
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
    pricing = models.ForeignKey(PricingConfiguration, on_delete=models.PROTECT)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    custom_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def update_base_pricing(self):
        # Find the most recent PricingConfiguration instance where effective_date <= today
        active_pricing = self.module.get_active_pricing()
        if active_pricing:
            self.pricing = active_pricing
            self.save()

    def __str__(self):
        return f"{self.plan}:{self.module.name}"