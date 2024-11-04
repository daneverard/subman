from django.db import models

class AccountType(models.TextChoices):
    """ Predefined account types. Subclass this to override with your own account types """
    CONSUMER = 'CONSUMER', 'Consumer'
    LENDER = 'LENDER', 'Lender'
    FUNDER = 'FUNDER', 'Funder'

class PricingTiers(models.TextChoices):
    """ Pricing tiers. Subclass this to override with your own platform pricing tiers e.g. bronze, silver, golg etc. """
    S = "SMALL", "Small"
    M = "MEDIUM", "Medium"
    L = "LARGE", "Large"