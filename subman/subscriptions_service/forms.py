from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import SubscriptionAccount, Module, PricingConfiguration, SubscriptionPlan, PlanModule

class SubscriptionAccountForm(forms.ModelForm):
    class Meta:
        model = SubscriptionAccount
        fields = ['name', 'invoicing_country', 'invoicing_currency']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'parent', 'description', 'applicable_account_type']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

class PricingConfigurationForm(forms.ModelForm):
    class Meta:
        model = PricingConfiguration
        fields = ['module', 'currency', 'tier', 'effective_date', 'monthly_price', 'annual_price']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))