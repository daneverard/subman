from django.shortcuts import render, get_object_or_404, redirect
from .models import SubscriptionAccount, Module, PricingConfiguration
from .forms import SubscriptionAccountForm, ModuleForm, PricingConfigurationForm

def account_list(request):
    accounts = SubscriptionAccount.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module_list.html', {'modules': modules})

def pricing_list(request):
    pricings = PricingConfiguration.objects.all()
    return render(request, 'pricing_list.html', {'pricings': pricings})

def account_create(request):
    if request.method == "POST":
        form = SubscriptionAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = SubscriptionAccountForm()
    return render(request, 'account_form.html', {'form': form})

def module_create(request):
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForm()
    return render(request, 'module_form.html', {'form': form})

def pricing_create(request):
    if request.method == "POST":
        form = PricingConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pricing_list')
    else:
        form = PricingConfigurationForm()
    return render(request, 'pricing_form.html', {'form': form})