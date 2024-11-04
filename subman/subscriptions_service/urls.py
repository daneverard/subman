from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.account_list, name='account_list'),
    path('modules/', views.module_list, name='module_list'),
    path('pricings/', views.pricing_list, name='pricing_list'),
    path('accounts/create/', views.account_create, name='account_create'),
    path('modules/create/', views.module_create, name='module_create'),
    path('pricings/create/', views.pricing_create, name='pricing_create'),
]