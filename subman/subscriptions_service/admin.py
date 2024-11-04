# admin.py
from django.contrib import admin
from .models import (
    SubscriptionAccount,
    Module,
    PricingConfiguration,
    SubscriptionPlan,
    PlanModule,
)

@admin.register(SubscriptionAccount)
class SubscriptionAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'invoicing_country', 'invoicing_currency')
    search_fields = ('invoicing_country', 'invoicing_currency')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'applicable_account_type')
    search_fields = ('name','parent',)
    list_filter = ('applicable_account_type',)

@admin.register(PricingConfiguration)
class PricingConfigurationAdmin(admin.ModelAdmin):
    list_display = ('module', 'currency', 'tier', 'effective_date', 'monthly_price', 'annual_price')
    list_filter = ('module', 'currency', 'tier', 'effective_date')
    search_fields = ('module__name',)
    ordering = ('-effective_date',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('account', 'tier', 'is_monthly', 'start_date', 'end_date')
    list_filter = ('tier', 'is_monthly',)
    search_fields = ('account__invoicing_country', 'tier')

@admin.register(PlanModule)
class PlanModuleAdmin(admin.ModelAdmin):
    list_display = ('plan', 'module', 'pricing', 'discount_percentage', 'custom_price')
    list_filter = ('module', 'plan',)
    search_fields = ('plan__account__invoicing_country', 'module__name', 'pricing__tier')