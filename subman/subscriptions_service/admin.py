# admin.py
from django.contrib import admin
from .models import (
    SubscriptionAccount,
    Module,
    AddOn,
    PricingConfiguration,
    SubscriptionPlan,
    PlanModule,
    PlanModuleSelectedAddon,
)

@admin.register(SubscriptionAccount)
class SubscriptionAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoicing_country', 'invoicing_currency')
    search_fields = ('invoicing_country', 'invoicing_currency')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'applicable_account_type')
    search_fields = ('name',)
    list_filter = ('applicable_account_type',)

@admin.register(AddOn)
class AddOnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'module')
    search_fields = ('name',)
    list_filter = ('module',)

@admin.register(PricingConfiguration)
class PricingConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'add_on', 'currency', 'tier', 'effective_date', 'monthly_price', 'annual_price')
    list_filter = ('module', 'add_on', 'currency', 'tier', 'effective_date')
    search_fields = ('module__name', 'add_on__name')
    ordering = ('-effective_date',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'tier', 'is_monthly', 'start_date', 'end_date')
    list_filter = ('tier', 'is_monthly',)
    search_fields = ('account__invoicing_country', 'tier')

@admin.register(PlanModule)
class PlanModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan', 'module', 'pricing', 'discount_percentage', 'custom_price')
    list_filter = ('module', 'plan', 'pricing')
    search_fields = ('plan__account__invoicing_country', 'module__name', 'pricing__tier')

@admin.register(PlanModuleSelectedAddon)
class PlanModuleSelectedAddonAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan_module', 'add_on', 'pricing', 'discount_percentage', 'custom_price')
    list_filter = ('plan_module', 'add_on', 'pricing')
    search_fields = ('plan_module__plan__account__invoicing_country', 'add_on__name', 'pricing__tier')