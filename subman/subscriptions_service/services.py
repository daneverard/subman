from django.utils import timezone
from .util import logging
from .models import Module, SubscriptionPlan, PlanModule, PricingConfiguration
from django.core.exceptions import ObjectDoesNotExist

logger = logging.get_logger(__name__)

class SubscriptionService:
    
    @staticmethod
    def assign_module_to_plan(plan, module_slug):
        """Assign a module to a plan using the active pricing configuration for the module and the plan's price tier."""
        try:
            # Get the module
            module = Module.objects.get(slug=module_slug)
            
            # Get active pricing for the module based on the plan's tier
            active_pricing = PricingConfiguration.objects.filter(
                module=module,
                tier=plan.tier,
                effective_date__lte=timezone.now().date()
            ).order_by('-effective_date').first()
            
            if not active_pricing:
                raise ObjectDoesNotExist("No active pricing configuration found.")
            
            # Create and save the PlanModule entry
            plan_module = PlanModule(plan=plan, module=module, pricing=active_pricing)
            plan_module.save()
            return plan_module
        except ObjectDoesNotExist as e:
            logger.warn(f"Assignment failed: {e}")
            return None
    
    @staticmethod
    def remove_module_from_plan(plan, module_slug):
        """Remove a module from a plan by setting the end date to today."""
        try:
            # Get the PlanModule instance
            plan_module = PlanModule.objects.get(plan=plan, module__slug=module_slug)
            
            # Set the end date to today to indicate removal
            plan_module.end_date = timezone.now().date()
            plan_module.save()
            return plan_module
        except ObjectDoesNotExist:
            logger.warn(f"Removal failed: PlanModule with slug {module_slug} not found in plan {plan}.")
            return None